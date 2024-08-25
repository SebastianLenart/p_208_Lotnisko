import datetime
import socket
import threading
import json
from connection_db import Database
from pprint import pprint
from follow_track import FollowTrack
import time
from visualization import Space3D


class Server:
    HOST = "127.0.0.1"
    PORT = 65432

    def __init__(self):
        self.stopFlag = False
        self.db = None
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.bind((self.HOST, self.PORT))
        self.lsock.listen()
        print(f"Listening on {(self.HOST, self.PORT)}")
        self.db = Database()
        self.db.create_table()
        self.db.remove_data_from_plane()
        self.active_planes = 0
        # airport = Space3D() # nie dziala bo blokuje program
        # self.Deeamon_animation = threading.Thread(target=self.add_point_animation, daemon=True)
        # self.Deeamon_animation.start()

    def read_write(self, connection):  # ta funkcja jest oddzielna dla kazdego samolotu, wykonuje sie wielowatkowo
        self.active_planes += 1
        if self.active_planes > 4:
            self.active_planes -= 1
            data = connection.recv(1024)
            print("Przekierwano Lot: ", json.loads(data.decode(encoding="utf8"))["number_flight"])
            return
        follow_track = FollowTrack()

        while True:  # w kazdym watku klienta musi byc petla

            answer_to_send = {"command": "",
                              "number_flight": "",
                              "pos_x": "",
                              "pos_y": "",
                              "pos_z": "",
                              "velocity": "",
                              "fuel": -1,
                              "tunnel": "",
                              "crash": False}
            try:
                data = connection.recv(1024)
                if data:
                    answer_to_send = json.loads(data.decode(encoding="utf8"))
                else:
                    print("no data received")
                    break
            except json.decoder.JSONDecodeError:
                print("Error")
            if (not answer_to_send or self.stopFlag or answer_to_send["command"] == "landing_finish"
                    or answer_to_send["command"] == "test"):
                print("FINISHHHH", answer_to_send["number_flight"])
                break
            print("number_flight: ", answer_to_send["number_flight"])
            if self.crash_plane(answer_to_send):
                answer_to_send["command"] = "crash"
                answer_to_send["crash"] = True
            self.save_data_to_track(follow_track, answer_to_send)
            self.add_or_change_data_plane(answer_to_send)
            try:
                answer_to_send2 = json.dumps(answer_to_send).encode(encoding='utf8')
                connection.sendall(answer_to_send2)
            except BrokenPipeError:
                print("Client removed", answer_to_send["number_flight"])
                break
            print(self.active_planes)  # dziala

        self.active_planes -= 1

        # delete db

    def crash_plane(self, answer_to_send):
        flag = False
        if answer_to_send["fuel"] <= 0:
            self.db.update_crash_plane(answer_to_send["number_flight"])
            flag = True
        data = self.db.get_points_to_crash_distance()
        for i in range(len(data) - 1):
            if (abs(data[i][1] - data[i + 1][1]) < 100) and (abs(data[i][2] - data[i + 1][2]) < 100):
                print("--------------->>>>>", data[i], " -- ", data[i + 1])
                print("CRASH: ", "nr:", data[i][0], "and", data[i + 1][0], " x:", data[i][1], data[i + 1][1], " y:",
                      data[i][2], data[i + 1][2])
                self.db.update_crash_plane(data[i][0])
                self.db.update_crash_plane(data[i + 1][0])
                flag = True
        return flag

    def save_data_to_track(self, follow_track, answer_to_send):
        follow_track.load_data_plane(answer_to_send)
        if not follow_track.chosen_tunnel:
            follow_track.choose_tunnel()
            answer_to_send["tunnel"] = follow_track.data_plane["tunnel"]

    def add_point_animation(self):
        pass

    def add_or_change_data_plane(self, data):
        if self.db.get_points(data["number_flight"]):
            self.db.update_data_plane(data)
        else:
            self.db.add_data_plane(data)

    def run(self):
        while True:
            print("waiting to accept")
            conn, addr = self.lsock.accept()  # Should be ready to read
            print(f"Accepted connection from {addr}")
            thread_from_client_to_server = threading.Thread(target=self.read_write, args=(conn,))
            thread_from_client_to_server.start()

    def cancel_plane(self):
        return "to_many_planes"
        # answer_to_send2 = json.dumps(answer_to_send).encode(encoding='utf8')
        # connection.sendall(answer_to_send2)


if __name__ == '__main__':
    server = Server()
    server.run()
