# Face-Recognition-Based-Attendance-System
Developed a real-time face recognition attendance system using OpenCV and the face_recognition library. Used NumPy and Pandas for data handling and attendance logs, with datetime for timestamping. The system improved accuracy and reduced proxy attendance.
# 🎯 Face Recognition Based Attendance System

## 📌 Project Overview

This project automates the attendance process using real-time **face recognition**. It captures live video input through a webcam, detects and recognizes faces, and logs attendance with timestamps. The system eliminates manual entry, improves accuracy, and reduces proxy attendance.

---

## 🛠 Technologies & Libraries Used

- **Python 3.x**
- **OpenCV** – for capturing video and detecting faces
- **face_recognition** – for encoding and recognizing faces
- **NumPy** – for handling image data arrays
- **Pandas** – for managing and exporting attendance logs
- **datetime** – for timestamping attendance
- **Visual Studio Code** – as the development environment

---

## 🚀 Features

- Real-time face detection and recognition via webcam
- Automatic attendance logging with date and time
- Saves attendance records in `.csv` format
- Scalable for classrooms, offices, or secured areas
- Simple and intuitive codebase for beginners in computer vision

---

## 🧠 How It Works

1. Encode known faces and store them in memory.
2. Activate webcam and detect faces in real-time.
3. Match detected faces with stored encodings.
4. Record name, date, and time in an attendance file if matched.

---

---

## 📝 Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/face-recognition-attendance.git
   cd face-recognition-attendance
   
2. Install the required packages:
bash
Copy
Edit
pip install -r requirements.txt

3. Add known face images in the data/ folder.

4. Run the system:
bash
Copy
Edit
python main.py

Learning Outcomes
Applied concepts of face detection & recognition using Python
Learned how to work with OpenCV and image encodings
Gained experience with data handling and automation using Pandas
