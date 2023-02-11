from doctest import debug
from sys import getallocatedblocks
import keyboard


class Gate:
    gated = False
    def __init__(self, checker, callback) -> None:
        self.checker = checker
    def execute(self):
        if self.checker():
            print("pressed" + str(self.gated))
            if not self.gated:
                self.gated = True
        else:
            print("3" + str(self.gated))
            if self.gated:
                print("4")
                self.callback(5)
                self.gated = False
    

def pressQ():
    # print(keyboard.is_pressed('q'))
    # return False
    return keyboard.is_pressed('q')

digits = []
pulseCount = 0
dialing = False
pulsing = False

def appendNumber(num):
    digits.append(num)

while True:
    gate = Gate(pressQ, appendNumber)
    gate.execute()
    # if keyboard.is_pressed("q"):
    #     if not dialing:
    #         dialing = True
    # else:
    #     if dialing:
    #         digits.append(5)
    #         dialing = False


    if len(digits) == 7:
        print(digits)
        break
