import RPi.GPIO as GPIO
try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(11, GPIO.OUT)
    while True:
        user_input=input("Ligar(1) Desligar(0) :")
        user_input=int(user_input)
        if user_input==1:
            GPIO.output(11, GPIO.HIGH)
        else:
            GPIO.output(11, GPIO.LOW) 
finally:
    GPIO.cleanup()
