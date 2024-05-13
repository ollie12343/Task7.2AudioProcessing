import speech_recognition as sr
import RPi.GPIO as GPIO
import time

num_files = 2

# Set up RPi
PIN = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

recogniser = sr.Recognizer()

for i in range(num_files):
    print(f"file {i + 1}")
    text = None
    while not text:
        try:
            with sr.AudioFile(f"test{i}.wav") as source:
                recogniser.adjust_for_ambient_noise(source, duration=0.2)
                audio = recogniser.record(source)
                
                text = recogniser.recognize_google(audio)
                text = text.lower()

                print(f"Recognised: {text}")
                if text == "light on":
                    GPIO.output(PIN, GPIO.HIGH)
                elif text == "light off":
                    GPIO.output(PIN, GPIO.LOW)
                elif text == "exit":
                    pass
                else:
                    print(text)
        except KeyboardInterrupt:
           break
        except Exception as e:
            print(e)
            recogniser = sr.Recognizer()
            continue
    time.sleep(2)
