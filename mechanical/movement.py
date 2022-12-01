#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

pwm=GPIO.PWM(13, 50)
pwm.start(0)

in1 = 17
in2 = 18
in3 = 27
in4 = 22

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002
step_loc = 0 
step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°
 
direction = True # True for clockwise, False for counter-clockwise
move = False #True for any movement, False for stopping 

theta = 0
phi = 0

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]
 
# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )
# initializing
GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )
 
 
motor_pins = [in1,in2,in3,in4]
motor_step_counter = 0 

def move_steps(steps):
    global motor_step_counter 
    global step_loc
    i = 0
    for i in range(steps): 
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin])
        if direction==True:
            motor_step_counter = (motor_step_counter - 1) % 8
        elif direction==False:
            motor_step_counter = (motor_step_counter + 1) % 8
        else: # defensive programming
            print( "uh oh... direction should *always* be either True or False" )
            cleanup()
            exit( 1 )
        time.sleep( step_sleep )

def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    pwm.stop()
    GPIO.cleanup()

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    #subscribe to location topic
    client.subscribe("starryStarry/calibrate")
    client.subscribe("starryStarry/coordinates")
    client.message_callback_add("starryStarry/calibrate", on_calibrate)
    client.message_callback_add("starryStarry/coordinates", on_coordinate)

def on_calibrate(client, userdata, message):
    cal_str = message.payload.decode()
    global move, direction, theta, motor_step_counter 
    if cal_str == "left":
        move = True 
        direction = False 
    elif cal_str == "right": 
        move = True
        direction = True 
    elif cal_str == "release":
        move = False 
        theta = 0
        motor_step_coutner = 0

def on_coordinate(client, userdata, message):
    global theta, phi, direction
    cstr = message.payload.decode()
    if cstr != "":
        coord_str = cstr.split(',')
        print(coord_str)
        goal_theta = coord_str[0]
        goal_phi = coord_str[1]
        step_count = ((float(goal_theta)-theta)/360)*4096
        q_phi = 10-float(goal_phi)/18

        if step_count >= 0:
            direction = True
            move_steps(step_count)
        else:
            direction = False
            move_steps(-step_count)

        pwm.ChangeDutyCycle(q_phi) 
        theta = float(goal_theta)
        phi = float(goal_phi)


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()
    while True: 
        if move:
            move_steps(1)
            #time.sleep(0.002)
    

 