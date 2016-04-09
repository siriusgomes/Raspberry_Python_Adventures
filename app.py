#!/usr/bin/env python
from flask import Flask, render_template, request, url_for, redirect

# Library for the 1602A Display with PCF8574 display. Got from: http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
import I2C_LCD_driver

# Library for the GPIO ports of the raspberry pi 3
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) #I'm using port 17 to control my relay

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('template.html')

@app.route('/light/<status>')
def light(status):
    if status == "1":
        GPIO.output(17,True)
    elif status == "0":
        GPIO.output(17,False)
    return status

@app.route('/display', methods=['POST'])
def display():
    mylcd = I2C_LCD_driver.lcd()
    mylcd.lcd_display_string(request.form['firstline'], 1)
    mylcd.lcd_display_string(request.form['secondline'], 2)
    print request.form['firstline']
    print request.form['secondline']
    return redirect(url_for('index')) 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

