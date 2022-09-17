import json
from Elevator import *

class Building:
    def __init__(self,minFloor,maxFloor):
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._elevList = []

    def from_json(self, fileName):
        with open(fileName, "r") as fp:
            d_temp = json.load(fp)
            self._minFloor = d_temp["_minFloor"]
            self._maxFloor = d_temp["_maxFloor"]
            for e in d_temp["_elevators"]:
                id = int(e["_id"])
                speed = float(e["_speed"])
                minFloor = int(e["_minFloor"])
                maxFloor = int(e["_maxFloor"])
                closeTime = float(e["_closeTime"])
                openTime = float(e["_openTime"])
                startTime = float(e["_startTime"])
                stopTime = float(e["_stopTime"])
                self._elevList.append(Elevator(id,speed,minFloor,maxFloor,closeTime,openTime,startTime,stopTime))

    def __str__(self):
        return f"This building's min floor is {self._minFloor}, max floor is {self._maxFloor} and has {len(self._elevList)} elevators"

    def __repr__(self):
        return f"This building's min floor is {self._minFloor}, max floor is {self._maxFloor} and has {len(self._elevList)} elevators"