from datetime import datetime
from os import path

import cv2


def detect_face(img_path: str, save_folder_path:str):
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces; outputs (x, y, w, h) for each face
    faces_positions = cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces_positions:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    timestamp = datetime.now().isoformat()
    cv2.imwrite(path.join(save_folder_path, "latest.jpg"), img)
    cv2.imwrite(path.join(save_folder_path, f"{timestamp}.jpg"), img)
