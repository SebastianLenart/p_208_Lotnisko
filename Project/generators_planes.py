import time
from client import Client
import random
from threading import Thread


class GeneratorPlanes:
    def __init__(self):
        self.number_of_flight = 0
        # zrob deamona i automatyczne generowanie samolotow

    def add_manual_planes(self):
        add_planes = -1
        add_planes = int(input("Wpisz liczbe ile samolotow chcesz dodac: "))
        for _ in range(add_planes):
            t = Thread(target=self.add_Client, args=(self.number_of_flight,))
            t.start()
            self.number_of_flight += 1
            time.sleep(8)

    def add_Client(self, number_flight):
        plane = Client(number_flight)
        while True:
            if plane.finish:
                del plane
                break
            # time.sleep(5) # z tym gorzej


if __name__ == '__main__':
    generator = GeneratorPlanes()
    generator.add_manual_planes()
