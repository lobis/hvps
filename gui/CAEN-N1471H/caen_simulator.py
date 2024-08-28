import threading
import time
import random


# class that simulates the channel of the caen by giving a random value to its attriutes vmon, imon and
class ChannelSimulator:
    def __init__(self, trip_probability=0.02):
        # private attributes (they do not exist in the real device)
        self._trip_probability = trip_probability
        self._vset = 100

        # public attributes (they exist in the real device)
        self.vset = 100
        self.iset = 0.6  # uA # functionality not implemented
        self.vmon = self.vset
        self.imon = self.vset / 10e3  # (uA) lets say there is a resistance of 10 MOhm
        self.imdec = 3  # channel imon number of decimal digits (2 HR, 3 LR)
        self.rup = 3  # V/s
        self.rdw = 10  # V/s
        self.pdwn = "RAMP"  # 'KILL' or 'RAMP'
        self.stat = {
            "ON": True,
            "RUP": False,
            "RDW": False,
            "OVC": False,
            "OVV": False,
            "UNV": False,
            "MAXV": False,
            "TRIP": False,
            "OVP": False,
            "OVT": False,
            "DIS": False,
            "KILL": False,
            "ILK": False,
            "NOCAL": False,
        }

    def _randomize(self):
        if self.stat["KILL"] or self.stat["DIS"]:
            self.stat["ON"] = False
            self.vmon = 0
            self.imon = 0
            return

        if self.stat["TRIP"] or self.stat["ILK"]:
            self.stat["ON"] = False
            if self.pdwn == "KILL":
                self.stat["KILL"] = (
                    True  # not sure if it behaves like this in KILL mode
                )
                self.vmon = 0
                self.imon = 0
                return

        self.vmon = random.gauss(self._vset, 1.0 / 3)  # 0.3 V standard deviation
        self.imon = random.gauss(
            self.vmon / 10e3, self.vmon / 100e3
        )  # (uA) lets say there is a resistance of 10 MOhm and 10% standard deviation

        if not self.stat["ON"]:
            self._vset -= self.rdw
            self.imon = -self.imon * 10
            # self.stat["RDW"] = True # not sure
            if self._vset <= 0:
                self._vset = 0
                self.vmon = 0
                self.imon = 0
            return

        if not self.stat["TRIP"]:
            self.stat["TRIP"] = random.random() < self._trip_probability

        # simulate ramp up and ramp down when the channel is ON
        if self._vset < self.vset:
            self.stat["RUP"] = True
            self.stat["RDW"] = False
            self._vset += self.rup
            self.imon = self.imon * 10
            if self._vset > self.vset:
                self._vset = self.vset
        elif self._vset > self.vset:
            self.stat["RDW"] = True
            self.stat["RUP"] = False
            self._vset -= self.rdw
            self.imon = -self.imon * 10
            if self._vset < self.vset:
                self._vset = self.vset
        else:
            self.stat["RUP"] = False
            self.stat["RDW"] = False

    def turn_on(self):
        self.stat["ON"] = True
        self.stat["TRIP"] = False
        self.stat["KILL"] = False
        self.stat["ILK"] = False

    def turn_off(self):
        self.stat["ON"] = False
        self.stat["KILL"] = False
        self.stat["TRIP"] = False
        self.stat["ILK"] = False  # not sure


# =========================================================


class ModuleSimulator:
    def __init__(self, nChannels, trip_probability=0.05):
        self.name = "N1471H SIMULATOR"
        self.number_of_channels = nChannels
        self.channels = [
            ChannelSimulator(
                1 - (1 - trip_probability) ** (1.0 / self.number_of_channels)
            )
            for i in range(self.number_of_channels)
        ]
        self.board_alarm_status = {
            "CH0": False,
            "CH1": False,
            "CH2": False,
            "CH3": False,
            "PWFAIL": False,
            "OVP": False,
            "HVCKFAIL": False,
        }
        self.interlock_status = False
        self.interlock_mode = "CLOSED"

        # Start the device reading thread
        self.randomize_thread = threading.Thread(
            target=self.__continous_randomize, daemon=True
        ).start()

    def clear_alarm_signal(self):
        self.board_alarm_status = {k: False for k in self.board_alarm_status.keys()}
        for ch in self.channels:
            ch.stat["TRIP"] = False
            ch.stat["ILK"] = False

    def _randomize(self):
        # print(self.board_alarm_status, self.interlock_status)
        # check for trips and set the alarm signal
        for i, ch in enumerate(self.channels):
            if ch.stat["TRIP"]:
                self.board_alarm_status["CH" + str(i)] = True
                # print(f"Channel {i} trip")

        # do the alarm-intlck connection and act the interlock
        self.__connection_alarm_intlck()
        if self.interlock_status:
            for ch in self.channels:
                ch.stat["ILK"] = True

        # randomize the channels
        for ch in self.channels:
            ch._randomize()

    def __continous_randomize(self, wait_seconds=1):
        while True:
            self._randomize()
            time.sleep(wait_seconds)

    def __connection_alarm_intlck(self):
        self.interlock_status = any([v for k, v in self.board_alarm_status.items()])
