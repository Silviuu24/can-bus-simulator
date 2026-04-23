from time import sleep
from src.can_message import CANMessage
from src.config import *

class ECUEngine:
    def __init__(self, bus, rpm, temperature):
        self.bus = bus
        self.set_rpm(rpm)
        self.set_temperature(temperature)

    def set_rpm(self, rpm):
        if not (RPM_MIN <= rpm <= RPM_MAX):
            raise ValueError("RPM out of range")
        self.rpm = rpm

    def set_temperature(self, temperature):
        if not (TEMPERATURE_MIN <= temperature <= TEMPERATURE_MAX):
            raise ValueError("TEMPERATURE out of range")
        self.temperature = temperature

    def _encode_value(self, value, dlc):
        data = []
        while value:
            data.append(value & 0xFF)
            value >>= 8

        while len(data) < dlc:
            data.append(0)

        data.reverse()

        return data

    def send_rpm(self, rpm_value):
        data = self._encode_value(rpm_value, DLC_RPM)

        msg = CANMessage(ID_RPM, data)
        self.bus.send(msg)

    def send_temperature(self, temperature_value):
        temperature_value += TEMPERATURE_OFFSET

        data = self._encode_value(temperature_value, DLC_TEMPERATURE)

        msg = CANMessage(id=ID_TEMPERATURE, data=data)
        self.bus.send(msg)

    def run(self):
        counter=0
        while True:
            if counter == 10:
                self.send_temperature(self.temperature)
                counter = 0
            self.send_rpm(self.rpm)
            sleep(0.01)
            counter += 1