from time import sleep
from can_message import CANMessage
from config import *

class ECUDashboard:
    def __init__(self, bus):
        self.bus = bus

