# Face Recognition-Based Attendance System with live database

This project is a real-time face recognition attendance system that automates the process of marking student attendance using a webcam and facial recognition technology. Built using Python, OpenCV, and the face_recognition library, it provides a seamless and efficient way to manage and log attendance without manual input.

When the system runs, it accesses the webcam feed and processes each frame to detect and recognize student faces. It compares detected faces against a set of pre-encoded facial data to identify registered students. If a match is found, the system fetches the corresponding student’s information from Firebase Realtime Database, such as name, ID, major, and academic standing.

To maintain accuracy and prevent duplicate attendance entries, the system includes a timestamp check. If the student’s last recorded attendance time was more than 30 seconds ago, it updates the Firebase database with the new attendance time and increments their total attendance count. If not, it notifies that the attendance has already been marked recently.

The interface is designed to be clear and interactive. It includes a static background with designated areas to display the webcam feed and various attendance modes. These modes visually guide the user through stages like loading, attendance marked, or already marked. The display includes the student’s name, ID, total attendance count, major, standing, year, and starting year.

The system uses cvzone for drawing clean visual overlays like corner rectangles around recognized faces and text boxes for better clarity. All image assets, including background and mode screens, are stored in a structured folder and loaded dynamically.

This project provides a scalable and efficient solution for educational institutions to automate attendance tracking with minimal hardware and maximum accuracy. It reduces administrative overhead, improves security, and makes attendance monitoring more transparent and tamper-proof.

The project can be expanded with additional features like anti-spoofing, support for multiple cameras, and analytics dashboards for real-time monitoring.

Required installations: 
```bash
pip install opencv-python face_recognition firebase-admin numpy cmake cvzone dlib
```

Reference for file structure:


![image](https://github.com/user-attachments/assets/e155bc11-ef5d-4446-ab79-271d71f345ea)
