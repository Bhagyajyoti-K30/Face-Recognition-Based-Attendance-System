import cv2
import numpy as np
import face_recognition
from datetime import datetime

# Function to mark attendance in a CSV file
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        
        # Only mark if the name is not already in the list
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
            print(f"Attendance Marked for {name}")

# This section represents where the webcam logic would be
# cap = cv2.VideoCapture(0)
# while True:
#     success, img = cap.read()
#     # Face detection logic here...
