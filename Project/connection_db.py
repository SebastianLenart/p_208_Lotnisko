import os.path
from threading import Thread, Semaphore
import time
from queue import Empty, Queue, Full
from dotenv import load_dotenv
from configparser import ConfigParser
from pprint import pprint
import psycopg2
from contextlib import contextmanager

CREATE_TABLE = """create TABLE IF NOT exists plane (plane_id serial primary key, number_flight INT, pos_x INT, pos_y INT,
pos_z INT, velocity INT, fuel INT, tunnel INT, finish BOOL, crash BOOL);"""
ADD_DATA_PLANE = """insert into plane (number_flight, pos_x, pos_y, pos_z, velocity, fuel, tunnel, finish, crash) 
values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
UPDATE_DATA_PLANE = """UPDATE plane set pos_x = %s, pos_y = %s, pos_z = %s, velocity = %s, 
fuel = %s, tunnel = %s, finish = %s, crash = %s WHERE number_flight = %s"""
UPDATE_CRASH = """UPDATE plane set crash = true WHERE number_flight = %s;"""
REMOVE_TABLE_PLANE = """DELETE FROM plane"""
SELECT_POINTS_BY_NUMBER_FLIGHT = """select pos_x, pos_y, pos_z
from plane
where number_flight = (%s)
order by plane_id 
limit 1"""
SELECT_POINTS = """select pos_x, pos_y, pos_z, number_flight from plane
order by number_flight"""
SELECT_POINTS_TO_CRASH = """select number_flight, pos_x, pos_y, pos_z 
from plane
where finish = false and crash = false and pos_z > 100
ORDER BY pos_y, pos_x;"""



class Database:
    def __init__(self):
        self.max_connections = 90
        self.min_connections = 5
        self.active_connections = 0
        self.standard_amount_of_connections = 0
        self.queue = Queue(maxsize=self.max_connections)
        self.semaphore = Semaphore()
        self.params = self.config()
        self.conn = None
        self.init_default_connections()

    def init_default_connections(self):
        while self.queue.qsize() < self.min_connections:
            self.add_to_queue_connection(psycopg2.connect(**self.params))

    def add_to_queue_connection(self, connection):
        if self.active_connections < self.max_connections:
            try:
                self.queue.put(connection)
            except:
                pass
        else:
            print("Too much active connections")

    def release_connection(self, conn):
        with self.semaphore:
            try:
                if conn is not None:
                    self.add_to_queue_connection(conn)
                    self.active_connections -= 1
                    # print("Active:", self.active_connections)
            except:
                print("except release")
                pass

    def config(self, filename='.env', section='postgresql'):  # zbedne database.ini
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        print("****************")
        pprint(db)
        return db

    def get_connection(self):
        with self.semaphore:
            conn = None
            try:
                conn = self.queue.get(block=False)
                self.active_connections += 1
            except Empty:
                print("empty")
                if self.add_to_queue_connection(psycopg2.connect(**self.params)):
                    conn = self.queue.get()
                    self.active_connections += 1
            # print("active:", self.active_connections)
            return conn

    @contextmanager
    def get_cursor(self):
        conn = self.get_connection()
        with conn:  # z tym dziala
            with conn.cursor() as cursor:
                yield cursor
        self.release_connection(conn)
# -------------------------------------------------------------------------------------------------------------------
    def create_test_table(self):
        with self.get_cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS borrower
(borrower_id SERIAL PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT, debt INTEGER);""")
            time.sleep(5)

    def create_table(self):
        with self.get_cursor() as cursor:
            cursor.execute(CREATE_TABLE)

    def add_data_plane(self, data):
        with self.get_cursor() as cursor:
            number_flight = data["number_flight"]
            pos_x = data["pos_x"]
            pos_y = data["pos_y"]
            pos_z = data["pos_z"]
            velocity = data["velocity"]
            fuel = data["fuel"]
            if data["tunnel"] == "":
                tunnel = 0
            elif data["tunnel"][0][1] == 4000:
                tunnel = 1
            else:
                tunnel = 2
            if data["command"] == "landing_finish":
                finish = True
            else:
                finish = False
            cursor.execute(ADD_DATA_PLANE, (number_flight, pos_x, pos_y, pos_z, velocity,
                                            fuel, tunnel, finish, False))

    def update_data_plane(self, data):
        with self.get_cursor() as cursor:
            number_flight = data["number_flight"]
            pos_x = data["pos_x"]
            pos_y = data["pos_y"]
            pos_z = data["pos_z"]
            velocity = data["velocity"]
            fuel = data["fuel"]
            if data["tunnel"] == "":
                tunnel = 0
            elif data["tunnel"][0][1] == 4000:
                tunnel = 1
            else:
                tunnel = 2
            if data["command"] == "landing_finish":
                finish = True
            else:
                finish = False
            cursor.execute(UPDATE_DATA_PLANE, (pos_x, pos_y, pos_z, velocity,
                                               fuel, tunnel, finish, data["crash"], number_flight,))
    def update_crash_plane(self, number_flight):
        with self.get_cursor() as cursor:
            cursor.execute(UPDATE_CRASH, (number_flight,))

    def remove_data_from_plane(self):
        with self.get_cursor() as cursor:
            cursor.execute(REMOVE_TABLE_PLANE)

    def get_points(self, number_flight):
        with self.get_cursor() as cursor:
            cursor.execute(SELECT_POINTS_BY_NUMBER_FLIGHT, (number_flight,))
            return cursor.fetchall()

    def get_points_to_visu(self):
        with self.get_cursor() as cursor:
            cursor.execute(SELECT_POINTS)
            return cursor.fetchall()

    def get_points_to_crash_distance(self):
        with self.get_cursor() as cursor:
            cursor.execute(SELECT_POINTS_TO_CRASH)
            return cursor.fetchall()


if __name__ == '__main__':
    db = Database()
    if db.get_points(3):
        print("3")
    if db.get_points(0):
        print("0")
    print(db.get_points(3))


    # threads = []
    # for _ in range(5):
    #     t = Thread(target=db.create_table)
    #     threads.append(t)
    #     t.start()
    # for t in threads:
    #     t.join()
