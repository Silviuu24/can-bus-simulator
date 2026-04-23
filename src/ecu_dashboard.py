from src.config import *

class ECUDashboard:
    def __init__(self, bus):
        self.bus = bus
        self.rpm = 0
        self.temperature = 0

    def _decode(self, data):
        value = 0
        for byte in data:
            value <<= 8
            value += byte
        return value

    def run(self):
        while True:

            try:
                msg = self.bus.receive()
                if msg is not None:
                    id_received = msg.arbitration_id

                    if id_received == ID_RPM:
                        self.rpm = self._decode(msg.data)
                        print(f"RPM: {self.rpm}")
                    elif id_received == ID_TEMPERATURE:
                        self.temperature = self._decode(msg.data) - TEMPERATURE_OFFSET
                        print(f"TEMPERATURE: {self.temperature}")
                    else:
                        print("unknown id")
            except Exception as e:
                print(e)
                break