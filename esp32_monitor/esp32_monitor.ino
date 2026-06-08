#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 display(128, 64, &Wire, -1);

int cpu_heat = 0;
int gpu_heat = 0;

int green = 25;
int blue = 26;
int red = 27;

void setup() {

  Serial.begin(115200);

  pinMode (green, OUTPUT);
  pinMode (blue, OUTPUT);
  pinMode (red, OUTPUT);

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    for(;;);
  }

  display.clearDisplay();
  display.setTextColor(WHITE);

  display.setTextSize (2);
  display.setCursor (15, 20);
  display.print ("SYSTEM OK");

  display.display();

}

void loop () {

  if (Serial.available() > 0) {
    
    String incoming_packet = Serial.readStringUntil('\n');
    

    cpu_heat = incoming_packet.toInt();
    
    display.clearDisplay();
    display.setCursor(10, 20);
    display.print("CPU: ");
    display.print(cpu_heat);
    display.print(" C");
    display.display();
  }

  if (cpu_heat < 60) {
    digitalWrite(blue, LOW);
    digitalWrite(red, LOW);
    digitalWrite(green, HIGH);
  } 
  else if (cpu_heat < 85 && cpu_heat >= 60) {
    digitalWrite(green, LOW);
    digitalWrite(red, LOW);
    digitalWrite(blue, HIGH);
  }
  else {
    digitalWrite(green, LOW);
    digitalWrite(blue, LOW);
    digitalWrite(red, HIGH);
  }
}