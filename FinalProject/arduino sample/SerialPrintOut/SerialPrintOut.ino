void setup() 
{
  Serial.begin(115200);
  while(!Serial);

  Serial.print("Arduino Starting");
  
}

void loop() 
{
  int byte;
  if(Serial.available() > 0)
  {
    byte = Serial.read();
    Serial.print("Received: ");
    Serial.println(byte, DEC);
  }
}
