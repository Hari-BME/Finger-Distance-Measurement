import cv2
import mediapipe as mp
import numpy as np
import math
import subprocess

# Install required libraries using pip
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

def calculate_thumb_to_index_finger_distance():
    video_path = input("Enter the video file path: ")
    KNOWN_DISTANCE = float(input("Enter the known distance from camera to step length measurement in cm: "))
    KNOWN_HEIGHT = float(input("Enter the known height of the step length measurement in cm: "))
    FOCAL_LENGTH = float(input("Enter the focal length of the camera used: "))

    cap = cv2.VideoCapture(video_path)

    # Load the Mediapipe Hand model
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    resize_display = input("Do you want to resize the output display? (y/n): ")
    if resize_display.lower() == "y":
        display_width = int(input("Enter the desired width of the output display: "))
        display_height = int(input("Enter the desired height of the output display: "))
    else:
        display_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        display_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    wait_key = int(input("Enter the waitkey value (0 to pause indefinitely, or a positive integer for milliseconds): "))

    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break

            height, width, _ = image.shape
            if resize_display.lower() == "y":
                image = cv2.resize(image, (display_width, display_height))

            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]

                x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width)
                y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
                x2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width)
                y2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)

                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) * KNOWN_DISTANCE / FOCAL_LENGTH * height / KNOWN_HEIGHT

                cv2.putText(image, f"Dis btw Thumb,Index finger: {distance:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

                cv2.imshow("Output Display", image)
                key = cv2.waitKey(wait_key)
                if key == ord('q'):
                    break

    cap.release()
    cv2.destroyAllWindows()

calculate_thumb_to_index_finger_distance()
