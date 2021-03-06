#
# Simple mock object for the GPIO module, allows to test the code
# without executing it on an actual Raspberry Pi
#

BOARD = "BOARD"
IN = "INPUT"
OUT = "OUTPUT"


def setmode(mode):
    print("Set mode {0}".format(mode))


def setwarnings(mode):
    print("Set warnings as {0}".format(mode))


def setup(pin, mode):
    print("Set pin {0} as {1}".format(pin, mode))


def output(pin, value):
    print("Output {0} to pin {1}".format(value, pin))


def input(pin):
    print("Input 0 to pin {0}".format(s))
    return 0


def cleanup():
    print("Cleanup done")
