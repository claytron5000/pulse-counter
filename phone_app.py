# import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from cgitb import handler
import keyboard
# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
# GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 18 to be an input pin

# class Gate:
#     passedMessage = False
#     def __init__(self, message, handler):
#         self.message = message
#         self.handler = handler
#     def getMessage(self):
#         self.passedMessage = True
#         return self.message
#     def process(self):
#         if handler():
#             if not self.passedMessage:
#                 print(self.getMessage())
#         else:
#             self.passedMessage = False

class Counter:
    count = 0
    def add(self):
        self.count += 1
    def getCount(self):
        return self.count

        
class Gate:
    message_sent = False
    def __init__(self, callback, message, inner_gate=False) -> None:
        self.callback = callback
        self.message = message
        self.inner_gate = inner_gate
    def process(self):
        if self.callback():
            if not self.message_sent:
                print(self.getMessage())
            if self.inner_gate:
                self.inner_gate.process()
        else:
            self.message_sent = False
    def getMessage(self):
        self.message_sent = True
        return self.message

class CountingGate(Gate):
    count = 0
    def addCounter(self, counter):
        self.counter = counter
    def increment(self):
        self.count += 1
    def process(self):
        if self.callback():
            if not self.message_sent:
                print(self.getMessage())
            if self.inner_gate:
                self.inner_gate.process()
        else:
            self.message_sent = False

def wKeyPress():
    return keyboard.is_pressed('w')

def qKeyPress():
    return keyboard.is_pressed('q')

wKeyGate = Gate(wKeyPress, "W was pressed")
qKeyGate = CountingGate(qKeyPress, "Q was pressed", wKeyGate)
while True:
    qKeyGate.process()
        

    
            


# tog = True
# dialing = Gate()
# pulsing = Gate()
# while True:
#     dialing.set(GPIO.input(10) == GPIO.HIGH)
#     if dialing.check():
#         print("Start Dial")
#         pulsing.set(GPIO.input(18) == GPIO.HIGH)
#         if pulsing.check():
#             print("Pulsing")

