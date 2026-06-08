<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/b72a9d21-b2a3-441d-a71e-553f2cddb7a2" /># My First Project: PC CPU Temperature Monitor with ESP32 🌡️

Hello! This is my very first software-hardware integration project, built after completing my first year in Management Information Systems (YBS) at Kadir Has University. 

This year I learned Python and C programming. I wanted to combine both languages to create a real-world product. This project reads my PC's CPU temperature using Python and sends it to an ESP32 microcontroller to display it on an OLED screen and light up different LEDs based on the temperature.

## How It Works
1. **Getting the Data:** A background program called Libre Hardware Monitor creates a local web server with JSON data about my PC components.
2. **Python Part:** My Python script reads this JSON data, finds the CPU temperature value, and sends it to the serial port (USB). It also has a simple desktop window (GUI) made with CustomTkinter to start and stop the system.
3. **ESP32 (C) Part:** The ESP32 receives the temperature value via serial communication. It prints the temperature on a 128x64 OLED screen and turns on:
   * **Green LED** if the CPU is cool (< 60°C)
   * **Blue LED** if the CPU is warm (60°C - 85°C)
   * **Red LED** if the CPU is hot (> 85°C)

##  Technologies Used
* **Languages:** Python, C (Arduino IDE)
* **Libraries:** CustomTkinter (for Python GUI), Serial, JSON, Adafruit GFX/SSD1306 (for OLED screen)
* **Hardware:** ESP32 Microcontroller, SSD1306 OLED Display, 3 LEDs (Green, Blue, Red), Breadboard and wires

## 📸 Project Photos

### Desktop App UI
<img width="683" height="617" alt="WhatsApp Image 2026-06-08 at 17 17 34" src="https://github.com/user-attachments/assets/b7e221b9-83ce-4a4f-a8f8-967beb787ea4" />


### Hardware Setup
<img width="554" height="626" alt="image" src="https://github.com/user-attachments/assets/932b0273-1587-4fbe-ba4a-f0ce2addb4e5" />


## 💡 What I Learned
* How to connect Python scripts with physical hardware.
* How to read and parse JSON data from a local server.
* Basic serial communication (UART) between PC and a microcontroller.
* Moving from simple console codes to structured applications.
