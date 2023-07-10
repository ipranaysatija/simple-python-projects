import RPi.GPIO as GPIO          
from time import sleep
from pynput import keyboard

#PINS
in1 = 24
in2 = 23
in3 = 21
in4 = 22
en = 25
en2 = 26
#PIN SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
#SPEED
p=GPIO.PWM(en,1000)
p2=GPIO.PWM(en2,1000)
p.start(25)
p2.start(25)
print("\n")

print("pranay's teleoping tool:")
print("manouver:      w")
print("            a  s  d ")
print("speed:  e -> medium") 
print("        r -> high")
print("stop: x")  
print("quit: q")           


while(1):
 with keyboard.Events() as events:
     event = events.get(1e6)


     if event.key == keyboard.KeyCode.from_char('w'): #FORWARD
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         event.key='z'
     elif event.key == keyboard.KeyCode.from_char('s'): #BACKWARD
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        event.key='z'
     elif event.key == keyboard.KeyCode.from_char('x'): #STOP
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        event.key='z'
     elif event.key == keyboard.KeyCode.from_char('a'): #LEFT
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        event.key='z'
     elif event.key == keyboard.KeyCode.from_char('d'): #RIGHT
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        event.key='z'

     elif event.key == keyboard.KeyCode.from_char('e'): #medium SPEED
        p.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        event.key='z'

     elif event.key == keyboard.KeyCode.from_char('r'): #high SPEED
        p.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        event.key='z'
     
    
     elif event.key == keyboard.KeyCode.from_char('q'): #quit
        GPIO.cleanup()
        break
    
     else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")