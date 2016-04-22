#!/usr/bin/env python
from flask import Flask, render_template, request, url_for, redirect
from threading import Thread
import logging
import time
import os
# Library for the 1602A Display with PCF8574 display. Got from: http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
import I2C_LCD_driver

# Library for the GPIO ports of the raspberry pi 3
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# Ports
RELAY_PORT=26
SPEAKER_PORT=27

GPIO.setup(RELAY_PORT, GPIO.OUT) #I'm using port 26 to control my relay
GPIO.setup(SPEAKER_PORT, GPIO.OUT) #I'm using port 27 to control my speaker


# Speaker things.
BUZZER_REPETITIONS = 1000
BUZZER_DELAY = 0.001
PAUSE_TIME = 0.3


# Logging configs
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('template.html')

@app.route('/light/<status>')
def light(status):
    if status == "1":
        GPIO.output(RELAY_PORT,True)
    elif status == "0":
        GPIO.output(RELAY_PORT,False)
    return status

@app.route('/display', methods=['POST'])
def display():
    #mylcd = I2C_LCD_driver.lcd()
    #mylcd.lcd_display_string(request.form['firstline'], 1)
    #mylcd.lcd_display_string(request.form['secondline'], 2)
    logging.debug(request.form['firstline'])
    logging.debug(request.form['secondline'])
    #t = Thread(target=messageThread, args=(request.form['firstline'], request.form['secondLine'],))
    #t.start()
    os.system("killall python")
    os.system("./display.py \"" + request.form['firstline'] + "\" \"" + request.form['secondline'] + "\" &")
    ring_speaker()
    return redirect(url_for('index'))

def ring_speaker():
    # Buzzer time
    for _ in xrange(BUZZER_REPETITIONS):
        for value in [True, False]:
            GPIO.output(27, value)
            time.sleep(BUZZER_DELAY)
    time.sleep(PAUSE_TIME)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
