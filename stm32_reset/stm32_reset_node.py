import signal
import RPi.GPIO as GPIO
import time

#exit_f = False

#def ctrlc_handler(signum, frame):
#    if GPIO.input(24) == GPIO.HIGH:         # Resetting rpi_status to not ready when existing the node
#        GPIO.output(24, GPIO.LOW)  
#    if GPIO.input(4) == GPIO.LOW:           # Ensure init status of STM32 signal is high after  exsiting the node 
#        GPIO.out(4, GPIO.HIGH)
#    exit_f = True
#    print("You have pressed Ctrl-c. Exited.")
#    exit(0)

def pin_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(24, GPIO.OUT)  # For informing STM32 raspi is ready, to prevent raspi freezed during boot
                              # due to serial connection between raspi and STM32 that u-boot freezed when
                              # serial is active during boot time.
                              # RPI4 GPIO 9 to 27 default state us LOW
    GPIO.setup(4, GPIO.OUT)   # For resetting STM32 to allow that micro-ros-agent (STM32) and raspi 
                              # connection.
                              # RPI4 GPIO pin 1 to 8 detult state is HIGH

def main():
    # initiaize
    pin_setup()
#    signal.signal(signal.SIGINT, ctrlc_handler)

    # Sending rpi ready status
    time.sleep(1) 
#    GPIO.output(24, GPIO.HIGH)  
    # time.sleep(3)                   

    # Sending reset signal to reset STM32
    GPIO.output(4, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(4, GPIO.HIGH)
#    print('Hi from rpi_status.')
#    while (exit_f == False):
#       pass

if __name__ == '__main__':
    main()
