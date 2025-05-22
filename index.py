from machine import Pin, PWM
from time import sleep

# Initialize PWM on Pin 1
pwm = PWM(Pin(16))
pwm.freq(50)  # Set frequency to 50 Hz for servo control

# Initialize PIR sensor on Pin 17
pir = Pin(17, Pin.IN, Pin.PULL_DOWN)

# Initialize LEDs
led_red = Pin(2, Pin.OUT)
led_green = Pin(3, Pin.OUT)

status = 0  # Motion detection status
print("Starting up the PIR Module")
sleep(1)
print("Ready")

while True:
    sleep(1)  # Wait 1 second between readings
    if pir.value() == 1:  # Motion detected
        print("Motion Detected")
        led_green.value(1)
        if status == 0:
            print("open")
            status = 1
            # Move servo from 0° to 90°
            for position in range(1600, 4750, 50):  # Adjust range for your servo
                pwm.duty_u16(position)
                sleep(0.01)  # Smooth movement

    else:
        print("Motion Not Detected")
        led_green.value(0)
        if status == 1:
            print("close")
            led_red.value(1)
            status = 0
            # Move servo back from 90° to 0°
            for position in range(4750, 1600, -50):
                pwm.duty_u16(position)
                sleep(0.01)  # Smooth movement
            break

pwm.duty_u16(0)
sleep(0.1)
led_red.value(0)
