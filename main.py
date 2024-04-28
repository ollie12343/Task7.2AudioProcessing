import speech_recognition as sr
import RPi.GPIO as GPIO


# Set up RPi
PIN = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

recogniser = sr.Recognizer()


def recog():
    text = None
    while not text:
        try:
            with sr.Microphone() as mic:
                recogniser.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recogniser.listen(mic)
                
                text = recogniser.recognize_google(audio)
                text = text.lower()                

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)
            recogniser = sr.Recognizer()
            continue
        
def main():
    while True:
        text = recog()
        if text == "light on":
            GPIO.output(PIN, GPIO.HIGH)
        elif text == "light off":
            GPIO.output(PIN, GPIO.LOW)
        elif text == "exit":
            break