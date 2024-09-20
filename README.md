Gyro Actuated Bot

Project Overview:
This project demonstrates a system that uses a smartphone’s built-in gyroscopic sensor to control the movement of two servo motors via an ESP32 microcontroller. By capturing pitch and roll angles from the phone's gyroscope and transmitting the data wirelessly (via Bluetooth or Wi-Fi), the system allows real-time servo motor control, offering precise and intuitive movement.

Features:
Real-time Control: Uses pitch and roll data from a smartphone’s gyroscope to control two servo motors.
Wireless Communication: Transmits data between the smartphone and the ESP32 microcontroller using Bluetooth or Wi-Fi.
Cross-Platform Interface: MATLAB-based mobile application for easy interaction.
Modular Design: Supports future expansion with additional sensors and actuators.

Components:
ESP32 DEVKIT V1 Module
Orange OT90R Servo Motor
TowerPro SG90 Mini Servo Motor
Jumper Wires
PLA

Software Used:
MATLAB: For signal processing and wireless transmission.
Arduino IDE: To program the ESP32 for data reception and servo control.
Fusion 360: For 3D design modeling of the components.
SnapMaker Luben: For 3D printing tasks.

Installation and Setup:
Hardware Setup:
Connect the servo motors to the ESP32 via GPIO pins.
Ensure proper power supply for both the ESP32 and servo motors.

Software Setup:
MATLAB: Install MATLAB on your smartphone to read the gyro sensor data and transmit it via Wi-Fi/Bluetooth.
Arduino IDE: Install the necessary ESP32 libraries and upload the control code for the servo motors.
Calibrate the system to ensure accurate and smooth servo movements in response to smartphone tilts.

Usage Instructions:
Open the MATLAB mobile app and run the script to capture gyroscope data.
Connect your smartphone to the ESP32 using Wi-Fi or Bluetooth.
Control the servo motors by tilting your phone; the ESP32 will process the pitch and roll data to adjust the motor angles accordingly.
Future Enhancements

Advanced Algorithms: 
Incorporate machine learning to enhance control precision.
Multi-Sensor Integration: Add more sensors like accelerometers for improved data accuracy.
Enhanced User Interface: Improve the smartphone app for better real-time feedback and control options.

License:
This project is for educational purposes. Feel free to modify and share under the open-source MIT License.

Authors:
Gourinandhan Saijush (4NM21RI017)
Sirisha R (4NM21RI048)
