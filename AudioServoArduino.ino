#include <Servo.h>

Servo myservo;  // Create a servo object
int servoState = 0;  // Variable to store the state of the servo (0 for IDLE, 1 for FORWARD, 2 for BACKWARD)

void setup() {
  myservo.attach(9);  // Attach the servo to pin 9
  Serial.begin(9600);  // Initialize serial communication
  servoState = 0;  // Set initial state to IDLE
  myservo.write(90);  // Move servo to initial position (IDLE position)
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read the incoming command from serial
    if (command == 'F') {  // If command is 'F' (Forward)
      servoState = 1;  // Update servo state to FORWARD
    } else if (command == 'B') {  // If command is 'B' (Backward)
      servoState = 2;  // Update servo state to BACKWARD
    }
  }

  // Move the servo based on the current state
  if (servoState == 1) {  // If servo state is FORWARD
    myservo.write(0);  // Move servo to forward position (0 degrees)
  } else if (servoState == 2) {  // If servo state is BACKWARD
    myservo.write(180);  // Move servo to backward position (180 degrees)
  } else {  // If servo state is IDLE
    myservo.write(90);  // Move servo to idle position (90 degrees)
  }

  delay(10);  // Delay for servo to reach the position
}
