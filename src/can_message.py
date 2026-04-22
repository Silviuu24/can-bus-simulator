import can

class CANMessage:
    def __init__(self, id, data, extend=False):

        if not extend:
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

        self.message = can.Message(arbitration_id=id, data=data, is_extended_id=extend)
