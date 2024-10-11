import os, sys, requests
import json

class Circuit:
    def __init__(self, jsor: str):
        self.jso = json.loads(jsor)
        self.CircuitID = self.jso["CircuitID"]
        self.PowerCapacity = self.jso["PowerCapacity"]
        self.PowerProduction = self.jso["PowerProduction"]
        self.PowerConsumed = self.jso["PowerConsumed"]
        self.PowerMaxConsumed = self.jso["PowerMaxConsumed"]
        self.BatteryDifferential = self.jso["BatteryDifferential"]
        self.BatteryPercent = self.jso["BatteryPercent"]
        self.BatteryCapacity = self.jso["BatteryCapacity"]
        self.BatteryTimeEmpty = self.jso["BatteryTimeEmpty"]
        self.BatteryTimeFull = self.jso["BatteryTimeFull"]
        self.FuseTriggered = self.jso["FuseTriggered"]

class Player:
    def __init__(self, jsor: str):
        self.jso = json.loads(jsor)
        self.name = self.jso["PlayerName"]
        self.ColorR = self.jso["TagColor"]["R"]
        self.ColorG = self.jso["TagColor"]["G"]
        self.ColorB = self.jso["TagColor"]["B"]

class APIHandler:
    def __init__(self):
        print("Starting API")

    def __get(self, path: str) -> str:
        r = requests.get(f"http://localhost:8080{path}")

        return r.text
    
    def GetPower(self):
        power = self.__get("/getPower")
        j = json.loads(power)
        circuits: list[Circuit] = []

        for circuit in j:
            cir = Circuit(json.dumps(circuit))
            circuits.append(cir)

        return circuits