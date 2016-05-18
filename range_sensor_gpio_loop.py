import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)


def read_once():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    return distance

dist_list = []

for i in range(30):
    distance = read_once()
    dist_list.append(distance)
    print "Distance:",distance,"cm"
    time.sleep(0.4)


import matplotlib.pyplot as plt
import numpy as np
myarray = np.array(read_list)

plt.figure(1)
plt.clf()
plt.plot(myarray)

plt.show()

GPIO.cleanup()
