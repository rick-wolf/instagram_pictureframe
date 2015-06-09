import sys
import time
import RPi.GPIO as io
import subprocess

io.setmode(io.BCM)

SWITCH_PIN = 18       # 22 on the board

def main():
    io.setup(SWITCH_PIN, io.IN, pull_up_down=io.PUD_UP)
    turned_off = False


    while True:
        if io.input(SWITCH_PIN):
            if turned_off:
                turned_off = False
                subprocess.call("tvservice -c 'PAL 4:3' && fbset -depth 8 && fbset -depth 16", shell=True)
            
        elif not turned_off:
            turned_off = True
            subprocess.call("tvservice -o", shell=True)
            

        time.sleep(.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()