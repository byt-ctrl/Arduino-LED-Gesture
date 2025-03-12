# 🖐 Control Your Arduino LEDs with Hand Gestures!

Ever dreamt of controlling your Arduino LEDs just by raising your hand? With this project, it's possible! Using a webcam, the system will count how many fingers you are holding up and light the LEDs accordingly. No physical buttons, just gestures with your hand! 

---

## 🚀 What are the Features :

1. **Hand tracking with a webcam**: No more extra equipment except the webcam. 
2. **Control 5 LEDs with gestures**: Easily toggle LEDs on or off according to how many fingers you are holding up. 
3. **Real-time response**: The Python and Arduino system will be communicating in real-time for smooth control. 
4. **Extendable**: Extend the project to cover more LEDs or devices easily. 

---

## 🛠️ What You’ll Need :

### --🔌 Hardware--

1. Arduino Uno
2. 5 LEDs
3. Jumper Wires
4. USB Cable (for connecting Arduino) (Type A to B)
5. Webcam (built-in or external)

### -- 💻 Software --

1. Arduino IDE (to upload Firmata firmware)
2. Python (for the gesture recognition script)
3. Required Python Libraries:
   ```bash
   pip install opencv-python mediapipe pyfirmata

## 🔧 Setup Guide:

### 1️⃣ Upload Standard Firmata to Arduino

1. Open the Arduino IDE.
2. Go to **File > Examples > Firmata > StandardFirmata**.
3. Select your Arduino Uno and the correct port.
4. Click **Upload** to upload the Firmata firmware to your Arduino.

### 2️⃣ Clone the Repository

1. Open terminal and run:
   ```bash
   git clone https://github.com/byt-ctrl/Arduino-LED-Gesture.git
   cd Arduino-LED-Gesture
   
### 3️⃣ Upload the Python Script

1. Open `controller.py` in a code editor.
2. Make sure the Arduino port is specified to it.
3. Save any changes if necessary in future.
4. Upload the `controller.py` file into Arduino.
5. Now run the main Python script i.e , (`main-python-file.py`) to start controlling LEDs using hand gestures.

---

## 🖐 How It Works:

Simply raise your fingers in front of the webcam, and the LEDs will turn on as follows:

1. **Thumb (1 finger)** = LED 1 ON
2. **Thumb + Index (2 fingers)** = LED 1 & 2 ON
3. **Thumb + Index + Middle (3 fingers)** = LED 1, 2 & 3 ON
4. **Thumb + Index + Middle + Ring (4 fingers)** = LED 1, 2, 3 & 4 ON
5. **All 5 Fingers** = All LEDs ON

---

## 🤝 Contributing:

If u have any idea's feel free to contribute   
Fork the repository if needed , make your changes, and submit a pull request.

---

## 📜 License:

This project is licensed under the **Apache 2.0 License**.
