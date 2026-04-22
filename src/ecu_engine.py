from time import sleep
from can_message import CANMessage
from config import *


class ECUEngine:
    def __init__(self, bus):
        self.bus = bus

    def send_rpm(self, data):
        msg = CANMessage(ID_RPM, data)
        self.bus.send(msg)

    def send_temperature(self, data):
        msg = CANMessage(ID_TEMPERATURE, data)
        self.bus.send(msg)

    def run(self):
        while True:
            self.send_rpm([900])
            sleep(0.1)
            self.send_temperature([90])
            sleep(0.1)