int val = 0, i, buzzer;
void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(9, OUTPUT);	
  pinMode(7, INPUT);
}

void loop()
{
  val = digitalRead(7);
  Serial.println(val);
  if(val == HIGH)
  {
    digitalWrite(13, HIGH);
  }
  else
  {
    digitalWrite(13, LOW);
  }
  for( int i=0; i<255; i++)
  {
    analogWrite(buzzer, i);
    delay(10);
  }
 for(i=255; i>0; i--)
  {
    analogWrite(buzzer, i);
    delay(10);
  }
}