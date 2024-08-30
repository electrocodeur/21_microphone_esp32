from machine import Pin
import time

# Pin definitions
DO = 34
LED_pin = 2

# Variables to track the last event time and LED state
last_event = 0
LED_state = False

# Define pin modes
led = Pin(LED_pin, Pin.OUT)
do_pin = Pin(DO, Pin.IN)

while True:
    # Read the digital input
    output = do_pin.value()
    
    if output == 0:  # LOW condition
        current_time = time.ticks_ms()
        if current_time - last_event > 50:  # Debounce period
            LED_state = not LED_state  # Toggle LED state
            led.value(1 if LED_state else 0)  # Write the LED state
            last_event = current_time  # Update last event time
