//defining Pins for LED
int Red_pin =11;
int Green_pin=10;
int Blue_pin=9;

//variables
int RED_Value;
int GREEN_Value;
int BLUE_Value;

//creating a function in order to controll the color of LED

void ControlColor(int Red, int Green, int Blue){
  analogWrite(Red_pin, Red);
  analogWrite(Green_pin, Green);
  analogWrite(Blue_pin, Blue);
  
}

void setup(){
  Serial.begin(9600);
  pinMode(Red_pin, OUTPUT);
  pinMode(Green_pin, OUTPUT);
  pinMode(Blue_pin, OUTPUT);
//  checking The LED at the First
//Trun on Red at Full Brightness
  analogWrite(Red_pin, 255);
  analogWrite(Green_pin, 0);
  analogWrite(Blue_pin, 0);
  delay(300);
//  Trun on the Blue at Full Brightness
  analogWrite(Red_pin, 0);
  analogWrite(Green_pin, 255);
  analogWrite(Blue_pin, 0);
  delay(300);
//  Turn on Green At Full Brightness   
  analogWrite(Red_pin, 0);
  analogWrite(Green_pin, 0);
  analogWrite(Blue_pin, 255);
  delay(300);
//  Turn off All 
  analogWrite(Red_pin, 0);
  analogWrite(Green_pin, 0);
  analogWrite(Blue_pin, 0);
}
void loop(){

//  checking if Serial is available or not
if (Serial.available()>0){
//Reading The Red color Value
  if (Serial.read()=='R'){ //R200
//    R200G20B0
    RED_Value = Serial.parseInt();
//    Reading R ends    
  }
//Reading the Green Color Value
if (Serial.read()=='G'){
GREEN_Value=Serial.parseInt();
//reading G ends   
}
//Reading the Blue Color Value 
if (Serial.read()=='B'){
  BLUE_Value = Serial.parseInt();
//  reading B ends 
}

ControlColor(RED_Value, GREEN_Value, BLUE_Value);
delay(100);

//Serail Available Ends
}

  //Setup Ends
}
