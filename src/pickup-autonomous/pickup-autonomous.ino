// Define pin numbers
const int trigPin = 9;
const int echoPin = 10;

// Define variables
float duration;
float distance;

void setup() {
  // Set trigPin as Output and echoPin as Input
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Clear trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Set trigPin to HIGH for 10 ms
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read echoPin
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.343 / 2;

  // Print distance to Serial Monitor
  Serial.print("Distance: ");
  Serial.println(distance);

  if (digitalRead(trigPin) == HIGH) {
    Serial.print("signal");
  }
}
