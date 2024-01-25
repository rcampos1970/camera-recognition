# STILL ON DEVELOPMENT
# Gaze Tracking with Haar Cascades

This Python script uses OpenCV to perform gaze tracking using Haar Cascade classifiers for face and eye detection. It also utilizes Matplotlib to visualize the gaze coordinates in real-time on a scatter plot.

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Matplotlib (`pip install matplotlib`)
- NumPy (`pip install numpy`)

## Setup
1. Install the required dependencies using the following command:
   ```bash
   pip install opencv-python matplotlib numpy
   ```

2. Run the script:
   ```bash
   python gaze_tracking_haar.py
   ```

3. The script will open a window displaying the webcam feed with detected faces, eyes, and an estimated gaze point. The gaze coordinates will be saved in a text file named `gaze_coordinates.txt`.

## Code Explanation
- The script initializes Haar Cascade classifiers for face and eye detection and opens a webcam feed.
- It uses the detectors to identify faces in each frame and eyes within the detected faces.
- Gaze coordinates are estimated based on the center of the detected eyes.
- The real-time gaze coordinates are plotted on a Matplotlib scatter plot.
- The script also displays the webcam feed with rectangles around detected faces, eyes, and a circle at the estimated gaze point.
- Press 'q' to exit the application.

# Face Detection using dlib

This Python script uses the dlib library to perform face detection using the frontal face detector provided by dlib.

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- dlib (`pip install dlib`)

## Setup
1. Install the required dependencies using the following command:
   ```bash
   pip install opencv-python dlib
   ```

2. Run the script:
   ```bash
   python face_detection_dlib.py
   ```

3. The script will open a window displaying the webcam feed with rectangles around detected faces.

## Code Explanation
- The script initializes the dlib frontal face detector and opens a webcam feed.
- It uses the detector to identify faces in each frame.
- Rectangles are drawn around detected faces in the webcam feed.
- Press 'Esc' key to exit the application.
