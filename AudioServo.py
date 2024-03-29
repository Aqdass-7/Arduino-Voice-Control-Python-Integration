import speech_recognition as sr
import serial
import time

# Initialize the serial connection to Arduino
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's serial port
time.sleep(2)  # Wait for Arduino to initialize

# Initialize the speech recognizer
r = sr.Recognizer()

# Function to send commands to Arduino
def send_command(command):
    ser.write(command.encode())
    time.sleep(0.5)  # Adjust delay if needed

# Main function to listen for voice commands
def listen_for_commands():
    with sr.Microphone() as source:
        print("Listening... (say 'Forward' or 'Backward')")
        r.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        command = r.recognize_google(audio).lower()
        print("You said:", command)

        if 'forward' in command:
            print("Command recognized: FORWARD")
            send_command('F')  # Send 'F' command to Arduino to move servo forward
        elif 'backward' in command:
            print("Command recognized: BACKWARD")
            send_command('B')  # Send 'B' command to Arduino to move servo backward
        else:
            print("Unknown command")

    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Main loop
while True:
    listen_for_commands()
