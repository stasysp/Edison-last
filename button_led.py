import mraa
import time

class State:
    state = False

args = []

def change_state(args):
    print("You have just pushed the button!")
    s.state = not s.state
    led.write(s.state)
    time.sleep(0.3)

s = State()

button = mraa.Gpio(4)
led = mraa.Gpio(8)

button.dir(mraa.DIR_IN)
led.dir(mraa.DIR_OUT)
led.write(s.state)
button.isr(mraa.EDGE_BOTH, change_state, args)

while True:
    print "I'm working..."
    time.sleep(2)