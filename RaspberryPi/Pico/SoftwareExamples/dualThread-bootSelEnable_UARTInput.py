# RP-2040 Input/Output Multi-threaded operational proof
import machine, utime, _thread, sys, rp2

# Setup the LED and obtain initial BOOTSEL button state
LED = machine.Pin(25, machine.Pin.OUT)
BOOTSEL = rp2.bootsel_button()

# The serial input
def serialRX_thread():
    while True:
        rxValue = sys.stdin.buffer.readline()
        if rxValue and (rxValue.decode() != "\n"):
            print(rxValue)
        else:
            pass

# Function to start the thread
def startThread():
    # This creates a new thread using:
    # - function name [argument 1]
    # - parameters you want to pass to it [argument 2]
    _thread.start_new_thread(serialRX_thread, ())

# The main function
if __name__ == "__main__":
    while True:
        # Check BOOTSEL button state
        BOOTSEL = rp2.bootsel_button()
        
        if BOOTSEL:
            startThread()
            
        LED.toggle()
        print("LED")
        utime.sleep(0.25)
