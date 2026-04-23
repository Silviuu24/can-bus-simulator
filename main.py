import threading
from src.can_bus import CANBus
from src.ecu_dashboard import ECUDashboard
from src.ecu_engine import ECUEngine

bus = CANBus()
engine = ECUEngine(bus,1100,90)
dashboard = ECUDashboard(bus)

en = threading.Thread(target=engine.run)
db = threading.Thread(target=dashboard.run)

en.daemon = True
db.daemon = True

en.start()
db.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    bus.shutdown()
