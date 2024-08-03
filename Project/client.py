from threading import Thread
import socket
import time
import datetime
import random
import json
from pprint import pprint
import math


class Client:
    HOST = "127.0.0.1"
    PORT = 65432

    def __init__(self, number_of_flight):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect_ex((self.HOST, self.PORT))
        self.finish = False
        self.number_of_flight = number_of_flight
        # self.pos_x = None
        # self.pos_y = None
        # self.pos_z = None
        # self.velocity = None
        # self.target_point = None
        self.fuel = random.randint(60, 130)  # sec
        self.start_life = datetime.datetime.now()
        self.json = {"command": "",
                     "number_flight": self.number_of_flight,
                     "pos_x": 0,
                     "pos_y": 0,
                     "pos_z": 0,
                     "velocity": 0,
                     "fuel": 0,
                     "tunnel": ""}
        self.flag_change_axis = False
        self.load_random_position()
        self.step_to_target = - 1
        self.step_move_x = 0
        self.step_move_y = 0
        self.step_move_z = 0
        self.step_move_v = 250
        self.target_x = None
        self.target_y = None
        self.target_z = None
        self.target_v = None
        self.next_step_to_point = 0
        self.landing_finish = False
        self.Deeamon_send_text = Thread(target=self.send_receive, daemon=True)
        self.Deeamon_send_text.start()

    def __del__(self):
        print("removed object: ", self.number_of_flight)

    def send_receive(self):
        while True:
            self.fuel -= 1
            self.json["fuel"] = self.fuel
            try:
                self.sock.sendall(json.dumps(self.json).encode(encoding='utf8'))
            except BrokenPipeError:
                print("BROKEN PIPE")
                self.finish = True
                break
            try:
                json_from_server = self.sock.recv(1024)
            except ConnectionResetError:
                self.finish = True
                break
            if json_from_server:
                self.json = json.loads(json_from_server.decode(encoding="utf8"))
            else:
                print("CONTINUE: ", self.number_of_flight)
                continue
            self.check_to_many_planes(self.json)
            self.check_crash(self.json)
            self.specify_direction()
            print(self.json["number_flight"], "---", self.number_of_flight)
            if self.finish:
                break
            time.sleep(1)

    def check_crash(self, response):
        if response["command"] == "crash":
            print("crash")
            self.finish = True
            return

    def load_random_position(self):
        if self.flag_change_axis:
            self.json["pos_x"] = random.choice([0, 10000])
            self.json["pos_y"] = random.randint(0, 10000)
            self.flag_change_axis = False
        else:
            self.json["pos_y"] = random.choice([0, 10000])
            self.json["pos_x"] = random.randint(0, 10000)
            self.flag_change_axis = True
        self.json["pos_z"] = random.randint(2000, 5000)
        self.json["velocity"] = random.randint(250, 300)

    # def check_fuel(
    #         self):  # to bedzie jednak po stronie servera, a kkolizje miedzy samolotami zrobie na podtsawie bazy danych
    #     if self.fuel < 0:
    #         # self.finish = True
    #         print("COLLISION")
    #         # TO DO

    def check_to_many_planes(self, response):
        print("odp:", response["command"])
        if response["command"] == "to_many_planes":
            print("To many planes > 4 nr.", self.number_of_flight)
            # self.json["command"] = "landing_finish"
            self.finish = True

    def specify_direction(self):
        if self.landing_finish:
            self.json["command"] = "landing_finish"
            self.finish = True
            return
        if self.step_to_target <= 0:
            self.check_target_point_achive()
        else:
            self.move_position()
            self.step_to_target -= 1

    def check_target_point_achive(self):
        try:
            self.target_x, self.target_y, self.target_z, self.target_v = self.json["tunnel"][self.next_step_to_point]
            self.next_step_to_point += 1
        except IndexError:
            self.landing_finish = True
            self.json["pos_x"], self.json["pos_y"], self.json["pos_z"], self.json["velocity"] = self.json["tunnel"][-1]
            return
        delta_x = abs(self.json["pos_x"] - self.target_x)
        delta_y = abs(self.json["pos_y"] - self.target_y)
        delta_z = abs(self.json["pos_z"] - self.target_z)
        delta_v = abs(self.json["velocity"] - self.target_v)
        distance = math.sqrt(delta_x * delta_x + delta_y * delta_y)
        self.step_to_target = self.compute_time_to_achive_point(distance)
        self.specify_step_xyz(delta_x, delta_y, delta_z, delta_v)

    def compute_time_to_achive_point(self, distance):
        time = (distance + 1737.71) / 244.999  # od 20 do 40 sec, w zaleznosci gdzie sie pojawi samolot
        return time

    def specify_step_xyz(self, x, y, z, v):
        self.step_move_x = x / self.step_to_target
        self.step_move_y = y / self.step_to_target
        self.step_move_z = z / self.step_to_target
        self.step_move_v = v / self.step_to_target
        # print("step: ", self.step_move_x)

    def move_position(self):
        if self.json["pos_x"] > self.target_x:
            self.json["pos_x"] -= int(self.step_move_x)
            if self.json["pos_x"] < int(self.target_x): self.json["pos_x"] = int(self.target_x)
        else:
            self.json["pos_x"] += int(self.step_move_x)
            if self.json["pos_x"] > int(self.target_x): self.json["pos_x"] = int(self.target_x)
        if self.json["pos_y"] > self.target_y:
            self.json["pos_y"] -= int(self.step_move_y)
            if self.json["pos_y"] < int(self.target_y): self.json["pos_y"] = int(self.target_y)
        else:
            self.json["pos_y"] += int(self.step_move_y)
            if self.json["pos_y"] > int(self.target_y): self.json["pos_y"] = int(self.target_y)
        if self.json["pos_z"] > self.target_z:
            self.json["pos_z"] -= int(self.step_move_z)
            if self.json["pos_z"] < int(self.target_z): self.json["pos_z"] = int(self.target_z)
        else:
            self.json["pos_z"] += int(self.step_move_z)
            if self.json["pos_z"] > int(self.target_z): self.json["pos_z"] = int(self.target_z)
        self.json["velocity"] -= int(self.step_move_v)
        if self.json["velocity"] < int(self.step_move_v):
            self.json["velocity"] = int(self.step_move_v)
