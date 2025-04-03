# Eagle Eye - Attendance Monitoring System

## 📌 Overview
Eagle Eye is a smart attendance monitoring system designed for employees and students. It leverages facial recognition technology to ensure accurate and efficient attendance tracking. The system is built using Python and integrates advanced libraries like OpenCV, dlib, and face_recognition for facial detection and recognition. The GUI is developed using Tkinter, providing a user-friendly interface.

## 🚀 Features
- 📸 **Facial Recognition**: Uses OpenCV and face_recognition to detect and verify faces.
- 🔍 **Real-time Detection**: Captures live video feed for attendance marking.
- 📏 **Facial Feature Measurement**: Analyzes the distances between key facial landmarks and stores them in an array for identification.
- 💾 **Database Management**: Stores and retrieves attendance records efficiently.
- 📊 **Attendance Reports**: Generates detailed reports for analysis.
- 🎨 **User-friendly Interface**: Developed using Tkinter for easy navigation.
- 🔐 **Secure & Reliable**: Ensures accurate attendance tracking with minimal errors.

## 🛠️ Tech Stack
- **Python** 🐍
- **OpenCV** 👀
- **dlib** 📌
- **face_recognition** 🏷️
- **Tkinter** 🖥️

## 📷 How It Works
1. **Capture Faces**: The system captures images of individuals and registers them.
2. **Extract Facial Features**: It measures distances between key facial landmarks (e.g., eyes, nose, mouth) and stores them as a numerical array.
3. **Recognize Faces**: During attendance, it detects faces in real-time and matches them with stored feature data.
4. **Mark Attendance**: If a match is found, attendance is recorded automatically.
5. **Generate Reports**: Users can view and export attendance logs.

## 📦 Installation
1. Clone the repository:
   git clone https://github.com/your-username/EagleEye.git
   cd Eagle-Ey
2. Install dependencies:
   pip install opencv-python dlib face_recognition tkinter
3. Run the application:
   python login.py
