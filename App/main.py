from api import APIHandler
import sys, os

api = APIHandler()

try:
    while True:
        circuits = api.GetPower()
        os.system("cls")

        for cir in circuits:
            print(f"Circuit ID: {cir.CircuitID}")
            print(f"Power Capacity: {int(cir.PowerCapacity)}")
            print(f"Power Production: {int(cir.PowerProduction)}")
            print(f"Power Current Consumed: {int(cir.PowerConsumed)}")
            print(f"Power Maximum Consumption: {int(cir.PowerMaxConsumed)}")
            print(f"Battery Percent: {int(cir.BatteryPercent)}%")
            print(f"Battery Capacity: {cir.BatteryCapacity} MW")
            if cir.BatteryDifferential > 0:
                print(f"Time Till Full: {cir.BatteryTimeFull}")
            elif cir.BatteryDifferential < 0:
                print(f"Time Till Empty: {cir.BatteryTimeEmpty}")
            else:
                print("Batteries Not In Use")
            if cir.FuseTriggered == True:
                print(f"Fuse Triggered: Yes")
            else:
                print(f"Fuse Triggered: No")

            print("----------------------------------------------")
except KeyboardInterrupt:
    exit()