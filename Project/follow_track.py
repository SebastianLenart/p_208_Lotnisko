import math


class FollowTrack:

    def __init__(self):
        self.runway = {"first line": [[6000, 4000], [8000, 4000]],  # x, y - poczatek pasa, koniec pasa pierwszego
                       "second line": [[6000, 6000], [8000, 6000]]}  # -//-
        self.first_tunnel = [[3000, 4000, 1000, 200], [4000, 4000, 500, 180],
                             [5000, 4000, 250, 150], [6000, 4000, 150, 100], [7000, 4000, 0, 0]]  # x, y, z, velocity
        self.second_tunnel = [[3000, 6000, 1000, 200], [4000, 6000, 500, 180],
                              [5000, 6000, 250, 150], [6000, 6000, 150, 100], [7000, 6000, 0, 0]]  # x, y, z, velocity
        self.dimension_board = [10000, 10000, 5000]  # x, y, z
        self.chosen_tunnel = False
        self.data_plane = None

    def load_data_plane(self, dict):
        self.data_plane = dict

    def return_answer(self):
        pass  # zwracaj slownik

    def choose_tunnel(self):
        a1 = abs(self.data_plane["pos_x"] - self.first_tunnel[0][0])
        a2 = abs(self.data_plane["pos_x"] - self.second_tunnel[0][0])
        b1 = abs(self.data_plane["pos_y"] - self.first_tunnel[0][1])
        b2 = abs(self.data_plane["pos_y"] - self.second_tunnel[0][1])
        c1 = math.sqrt(a1 * a1 + b1 * b1)
        c2 = math.sqrt(a2 * a2 + b2 * b2)
        if c1 < c2:
            self.data_plane["tunnel"] = self.first_tunnel
        else:
            self.data_plane["tunnel"] = self.second_tunnel
        self.chosen_tunnel = True
