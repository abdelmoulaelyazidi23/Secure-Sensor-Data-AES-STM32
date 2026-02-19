# Secure Sensor Data using AES-128 on STM32L475

## Overview

This project demonstrates secure transmission of temperature data
from the onboard HTS221 sensor using AES-128 software encryption.

The encrypted data is transmitted via UART and decrypted on a PC using Python.

The goal of this project is educational:
to understand the internal structure of AES and implement it in software
on an embedded system.

---

## Hardware

- STM32L475 IoT Discovery (B-L475E-IOT01A2)
- Onboard HTS221 temperature sensor (I2C)

---

## Software Tools

- STM32CubeMX
- STM32CubeIDE
- Python 3
- PyCryptodome
- PySerial

---

## System Architecture

HTS221 (I2C)
    ↓
STM32L475
    - Temperature acquisition
    - Data formatting ("T=XX.XX")
    - AES-128 encryption (ECB mode)
    - HEX encoding
    - UART transmission
    ↓
PC
    - Serial reception
    - HEX to bytes conversion
    - AES-128 decryption
    - Display original temperature

---

## AES Implementation

- AES-128
- Software implementation in C
- Mode: ECB
- Block size: 16 bytes
- Static shared key

The AES implementation is based on an open-source C implementation
integrated into the STM32 project.

---

## Project Structure

Core/ → STM32 application source code
Drivers/ → HAL drivers
PC_Decryption/ → Python decryption script
tempchiffrée.ioc → CubeMX configuration file


---

## Example Output

Encrypted (UART):
C49E6FC59DC3990399B7738161BF3E40


Decrypted (PC):
T=25.34


---

## How to Run

### STM32

1. Open the project in STM32CubeIDE
2. Build and flash the board
3. Open a serial monitor at 115200 baud

### PC

1. Install dependencies:

pip install pycryptodome pyserial


2. Update the COM port in the Python script
3. Run:

python decrypt.py


---

## Educational Purpose

This project focuses on:

- Embedded sensor acquisition
- Software implementation of AES
- Secure serial communication
- Interoperability between embedded C and Python

For real-world applications, hardware crypto acceleration and secure key management are recommended.
