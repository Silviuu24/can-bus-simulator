import can

class CANMessage:
    def __init__(self, id, data, is_extended_id=False):

        if not is_extended_id:
            if not (0x0 <= id <= 0x7FF):
                raise ValueError("Invalid ID")
        else:
            if not (0x0 <= id <= 0x1FFFFFFF):
                raise ValueError("Invalid ID")

        if len(data) > 8:
            raise ValueError("Too many bytes")
        for byte in data:
            if not (0x00 <= byte <= 0xFF):
                raise ValueError("Invalid byte")

        self.CANmsg = can.Message(arbitration_id=id, data=data, is_extended_id=is_extended_id)

    @property
    def arbitration_id(self):
        return self.CANmsg.arbitration_id

    @property
    def data(self):
        return self.CANmsg.data
