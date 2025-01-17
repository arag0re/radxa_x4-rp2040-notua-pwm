from machine import lightsleep, Pin, PWM, ADC
from time import sleep

# Initialize the temperature sensor (connected to ADC pin 4)
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

# Initialize the temperature sensor (connected to ADC pin 4)
sensor_temp = ADC(4)
MAX_DUTY_CYCLE = 65_535
FORTY_PERCENT_DUTY_CYCLE = (MAX_DUTY_CYCLE * 2) // 5

# PWM fans use a frequency of 25 kHz.
PWM_FAN_FREQUENCY = 25_000

ONE_MILLISECOND = 0.001

# For PWM use GPIO pin #29, which is pin A0 on the Adafruit QT Py RP2040.
# PWM_PIN = 29

# For PWM use GPIO pin #15, which is pin #20 on the Raspberry Pi Pico.
PWM_PIN = 20

pwm0 = PWM(Pin(PWM_PIN))

pwm0.freq(PWM_FAN_FREQUENCY)

# Reduce the speed of the fan to 40% by setting the PWM duty cycle to 40%.
pwm0.duty_u16(FORTY_PERCENT_DUTY_CYCLE)


# Wait 15 seconds before initiating light sleep.
# This allows accessing the board for the first 15 seconds after it it receives power.
sleep(15)
# Function to calculate the temperature in Celsius from the sensor reading (integrated into rp2040)
def read_temperature():
    reading_in_volts = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading_in_volts - 0.706) / 0.001721
    return temperature

# Function to control fan speed based on temperature
def control_fan_speed(temperature):
    # Set PWM duty cycle based on temperature
    if temperature < 50:  # Below 25°C, fan is off or at minimum speed
        pwm0.duty_u16(0)
    elif temperature > 50:  # Between 25°C and 30°C, fan is at low speed
        pwm0.duty_u16(32767)  # Duty cycle around 50%
    elif temperature > 55 :  # Between 30°C and 35°C, fan is at medium speed
        pwm0.duty_u16(49151)  # Duty cycle around 75%
    else:  # Above 35°C, fan is at full speed
        pwm0.duty_u16(65535)  # Duty cycle 100%

while True:
    temperature = read_temperature()
    print("Temperature: {:.2f} C".format(temperature))
    control_fan_speed(temperature)
    sleep(2)
