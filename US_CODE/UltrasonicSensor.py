import time
import numpy as np
import RPi.GPIO as GPIO

class UltrasonicSensor():
    def __init__(self, validity_thresh=7, trig=23, echo=24):
        self._half_speed_of_sound = 17150           # half the speed of sound; used for distance calculation
        self._num_measurements    = 5               # number of measurements to take for averaging
        self._validity_thresh     = validity_thresh # distance (cm) comparison above which the measurement is invalid
        self._max_distance        = 575             # the maximum distance the ultrasonic sensor can measure
        self._min_distance        = 2               # the minimum distance the ultrasonic sensor can measure
        self._trig                = trig            # trig GPIO pin number
        self._echo                = echo            # echo GPIO pin number

        # set GPIO config vals
        GPIO.setmode(GPIO.BCM)       # set GPIO pin numbering 
        GPIO.setup(trig, GPIO.OUT)   # set pin as GPIO out
        GPIO.setup(echo, GPIO.IN)    # set pin as GPIO in

    def getUltrasonicDistance(self):
        print("Distance measurement in progress")

        # take distance measurement num_measurement
        # times and store them in an array for averaging
        distances = []
        for i in range(self._num_measurements):
          # set TRIG as low
          GPIO.output(self._trig, False)
          print("Waitng For Sensor To Settle")
          time.sleep(0.03)

          # set TRIG as high
          GPIO.output(self._trig, True)
          time.sleep(0.00001)

          # set TRIG as low
          GPIO.output(self._trig, False)

          # check whether the ECHO is low
          while GPIO.input(self._echo)==0:
            # save last known time of low pulse
            pulse_start = time.time()

          # check whether the ECHO is high
          while GPIO.input(self._echo)==1:
            # save last know time of high pulse
            pulse_end = time.time()

          pulse_duration = pulse_end - pulse_start

          # multiply pulse duration by 17150 to get distance
          distance = round(pulse_duration * self._half_speed_of_sound, 2)

          # validate the distance measurement before appending it
          # to the list of other measurements
          if distance > self._min_distance and distance < self._max_distance:
            valid_distance = True
            for d in distances:
                if abs(distance - d) > self._validity_thresh:
                    valid_distance = False
                    break

            # if the distance is valid, add to list
            if valid_distance:
                distances.append(distance)

        # return average of valid distance measurements
        return np.mean(distances)
