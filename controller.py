# controller.py FILE
import pyfirmata  # Importing pyFirmata library

comport='COM5'  # Define the communication port for Arduino (change this to the correct one for your system)

# Initialize the Arduino board COM Port
board=pyfirmata.Arduino(comport)


led_pins = {
    'led_pin_1': board.get_pin('d:8:o'),
    'led_pin_2': board.get_pin('d:9:o'),                        # It Defines Pin allocation to arduino
    'led_pin_3': board.get_pin('d:10:o'),
    'led_pin_4': board.get_pin('d:11:o'),
    'led_pin_5': board.get_pin('d:12:o')
}

# Function to control LEDs based on finger states
def led(fingerUp):
    
    """
    This function turns on/off the LEDs based on the finger states provided.
    fingerUp: A list of 5 elements representing whether each finger is up (1) or down (0).

    """
    # Turn off all LEDs initially
    for led in led_pins.values():
        led.write(0)

    # Loop through each finger state and turn on the corresponding LED if the finger is up
    for a in range(len(fingerUp)):
        if fingerUp[a]==1:  # Check if the finger is up
            led_pins[f'led_{a+1}'].write(1)  # Turn on the corresponding LED
