# AI-Hand-Gesture-Recognition-Using-Webcam
Real-time AI-based hand gesture recognition using Python, OpenCV, and MediaPipe to detect Open Hand, Fist, Thumbs Up, and Victory/Peace gestures through a webcam.

📌 Project Overview

AI Hand Gesture Recognition Using Webcam is a real-time computer vision application that detects and recognizes basic hand gestures using a webcam.

The system uses MediaPipe Hand Landmarker to detect 21 hand landmarks and OpenCV to capture and display webcam frames. The landmark positions are analyzed to identify the user's gesture.

Supported Gestures
Gesture	Recognition
✋	Open Hand
✊	Fist
👍	Thumbs Up
✌️	Victory / Peace
🎯 Objective

The main objective of this project is to develop a simple AI-based system capable of recognizing hand gestures in real time through a webcam.

The project demonstrates the use of:

Computer Vision
Hand Landmark Detection
Real-Time Image Processing
Gesture Classification
Python-based AI application development
✨ Features
🎥 Real-time webcam input
✋ Hand detection
📍 21-point hand landmark detection
🤖 AI-based hand tracking using MediaPipe
🔍 Gesture classification
🖥️ Real-time gesture display
⚡ Fast processing
📸 Screenshot-ready output
🎬 Working demonstration video
🛠️ Technologies Used
Python

Python is used as the primary programming language for implementing the application.

OpenCV

OpenCV is used for:

Webcam access
Video capture
Frame processing
Drawing landmarks
Displaying the output
MediaPipe

MediaPipe Hand Landmarker detects and tracks the hand and provides 21 hand landmark coordinates.

NumPy

NumPy provides numerical processing support for the computer vision environment.

🔄 System Workflow
             Webcam
                ↓
        Capture Video Frame
                ↓
             OpenCV
                ↓
       MediaPipe Hand Detection
                ↓
        21 Hand Landmarks
                ↓
       Gesture Recognition
                ↓
 ┌──────────────┼───────────────┐
 ↓              ↓               ↓
Open Hand      Fist        Thumbs Up
                ↓
        Victory / Peace
                ↓
       Display on Screen
📂 Project Structure
AI-Hand-Gesture-Recognition/
│
├── main.py
├── hand_detector.py
├── gesture_recognizer.py
├── config.py
├── hand_landmarker.task
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── open_hand.png
│   ├── fist.png
│   ├── thumbs_up.png
│   ├── victory_peace.png
│   └── no_hand_detected.png
│
└── demo/
    ├── AI_Hand_Gesture_Recognition_Demo.mp4
    
💻 System Requirements
Hardware
Laptop/Desktop
Webcam
Minimum 4 GB RAM
Intel Core i3 or equivalent processor
At least 1 GB available storage
Software
Windows 10/11, Linux, or macOS
Python 3.10 or above
VS Code / PyCharm
Git
GitHub
📦 Installation
1. Clone the Repository
git clone https://github.com/Priyadharshinipalanisami/AI-Hand-Gesture-Recognition.git
cd AI-Hand-Gesture-Recognition
2. Install Dependencies
python -m pip install -r requirements.txt

The requirements.txt contains:

opencv-python
mediapipe
numpy
📥 MediaPipe Model

The project requires the MediaPipe Hand Landmarker model:

hand_landmarker.task

Download the model and place it in the root directory:

AI-Hand-Gesture-Recognition/
│
├── hand_landmarker.task
├── main.py
├── hand_detector.py
├── gesture_recognizer.py
└── ...
▶️ Running the Project

Run the following command:

python main.py

The webcam window will open automatically.

Show different gestures in front of the camera.

Expected Results

Open Hand

Gesture:
Open Hand

Fist

Gesture:
Fist

Thumbs Up

Gesture:
Thumbs Up

Victory / Peace

Gesture:
Victory / Peace

Press Q to close the application.

📸 Screenshots
Open Hand

Fist

Thumbs Up

Victory / Peace

No Hand Detected

🎬 Working Demo

A working demonstration video is included in:

demo/AI_Hand_Gesture_Recognition_Demo.mp4

The demonstration shows:

No Hand Detected
       ↓
Open Hand
       ↓
Fist
       ↓
Thumbs Up
       ↓
Victory / Peace
🧪 Testing
Test Case	Input	Expected Output
TC01	No hand	No Hand Detected
TC02	Open palm	Open Hand
TC03	Closed hand	Fist
TC04	Thumb raised	Thumbs Up
TC05	Two fingers raised	Victory / Peace
📊 Advantages
Simple and easy to use
Real-time recognition
No special hardware required
Uses a standard webcam
Lightweight implementation
Easy to extend with additional gestures
Useful for human-computer interaction applications
🚀 Future Enhancements

The project can be extended to support:

More hand gestures
Two-hand recognition
Gesture-controlled applications
Media player control
Presentation control
Virtual mouse
Sign language recognition
Voice output
Machine-learning-based gesture classification
Gesture-based smart home control
🎓 Applications

This technology can be used in:

Human-computer interaction
Touchless interfaces
Smart devices
Presentation control
Gaming
Accessibility systems
Virtual mouse systems
Sign language applications
Educational applications
👨‍💻 Author

Priyadharshini

Project

AI Hand Gesture Recognition Using Webcam

GitHub
https://github.com/Priyadharshinipalanisami/AI-Hand-Gesture-Recognition
📄 License

This project is licensed under the MIT License.

⭐ Acknowledgement

This project uses OpenCV for computer vision and MediaPipe for real-time hand landmark detection and tracking.
