# Thumb to Index Finger Distance Measurement

This project calculates the distance between the thumb and index finger in a video using the Mediapipe library and computer vision techniques.

## Installation

To install the required libraries, run the following command: 

pip install -r requirements.txt



## Usage Instruction

## Description

The `calculate_thumb_to_index_finger_distance` function in the code calculates the distance between the thumb and index finger based on the hand landmarks detected by the MediaPipe library. The calculation requires the following variables:

- `KNOWN_DISTANCE`: The known distance from the camera to the finger in centimeters. This can be measured using a measuring tape or any other reliable method.

- `KNOWN_HEIGHT`: The known height of the finger from the camera in centimeters. This is the distance from the camera lens to the tip of the finger and can be measured using a measuring tape or any other reliable method.

- `FOCAL_LENGTH`: The focal length of the camera used in millimeters. This determines the field of view and perspective of the camera. The focal length can usually be found in the camera specifications or obtained from the manufacturer.

## Usage

1. Install the required libraries by running `pip install -r requirements.txt`.

2. Run the script `finger_distance_measurement.py`.
   
3. Choose the video file or use the webcam to capture the hand gestures.

4. Provide the path to the video file when prompted.

5. Enter the known distance, known height, and focal length when prompted.

6. Choose whether to resize the output display. If yes, enter the desired width and height.

7. Enter the waitkey value to control the display duration (0 to pause indefinitely, or a positive integer for milliseconds).

8. The calculated distance between the thumb and index finger will be displayed in centimeters.

9. Press 'q' to exit the program.

## Troubleshooting

If you encounter any issues or errors, try the following troubleshooting steps:

- Ensure the video file path is correct and accessible.
- Verify that the required libraries are installed by running `pip list` and checking for the presence of the dependencies mentioned in `requirements.txt`.
- Make sure the video file format is supported by OpenCV.

## Contributing

Contributions to this project are welcome! If you find any bugs, have feature requests, or want to make improvements, please open an issue or submit a pull request.

## Contact

For any questions or inquiries, feel free to reach out to harikrishnanbme@gmail.com.


