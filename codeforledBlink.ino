// Define the pin for the LED
const int ledPin = 13;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  // Set the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Check if data is available to read from serial
  if (Serial.available() > 0) {
    // Read the incoming byte
    char receivedChar = Serial.read();
    
    // Check the received command
    if (receivedChar == 'H') {
      // Turn on the LED
      digitalWrite(ledPin, HIGH);
    } else if (receivedChar == 'L') {
      // Turn off the LED
      digitalWrite(ledPin, LOW);
    }
  }
}
