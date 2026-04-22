import can

class CANBus:
    def __init__(self, timeout=1.0):
        self.bus = can.Bus(interface="virtual", channel="can0")
        self.timeout = timeout

    def send(self, message):
        self.bus.send(message)

    def receive(self):
        return self.bus.recv(timeout=self.timeout)

    def shutdown(self):
        self.bus.shutdown()