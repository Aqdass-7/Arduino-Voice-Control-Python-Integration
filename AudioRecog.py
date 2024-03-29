import speech_recognition as sr
import serial

# Initialize the speech recognizer and microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Open serial connection to Arduino
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's serial port

# Main loop
while True:
    print("Listening... (say 'ON' or 'OFF')")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Recognize the speech command
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        # Send command to Arduino based on the recognized keyword
        if "on" in command:
            ser.write(b'H')  # Send 'H' command to turn LED on
            print("LED ON")
        elif "off" in command:
            ser.write(b'L')  # Send 'L' command to turn LED off
            print("LED OFF")
        else:
            print("Keyword not recognized.")

    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
