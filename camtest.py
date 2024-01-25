import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the Haar Cascade XML files for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Create a window to display the video feed
cv2.namedWindow('Gaze Tracking')
x=[]
y=[]
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
scatter = ax.scatter(x, y)  # Create scatter plot with empty data
plt.title('Gaze Tracking Scatter Plot')
# Open the webcam (you may need to change the index)
cap = cv2.VideoCapture(0)

# Create a text file to save gaze coordinates
file = open('gaze_coordinates.txt', 'w')
file.write("X"+";"+"Y\n")
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face and eye detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Crop the region of interest (ROI) to detect eyes
        roi_gray = gray[y:y + h, x:x + w]

        # Detect eyes within the ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            # Calculate the approximate gaze point based on the center of the detected eyes
            gaze_x = x + ex + ew // 2
            gaze_y = y + ey + eh // 2


            sensitivity = 10
            ax.set_xlim(0, 300*sensitivity)  # Adjust the limits as needed
            ax.set_ylim(0, 300*sensitivity)  # Adjust the limits as needed
            scatter.set_offsets(np.column_stack((x*sensitivity, y*sensitivity)))
            plt.pause(0.001)  # Add a small pause to allow the plot to update

            font = cv2.FONT_HERSHEY_SIMPLEX
            text1 = "X:"
            text2 = "Y:"
            position1 = (25, 25)  # (x, y) coordinates
            position2 = (25, 50)  # (x, y) coordinates
            font_scale = 0.5
            font_color = (255, 0, 0)  # BGR color (blue in this case)
            thickness = 1
            # Put the text on the frame
            cv2.putText(frame, text1+str(gaze_x), position1, font, font_scale, font_color, thickness)
            cv2.putText(frame, text2+str(gaze_y), position2, font, font_scale, font_color, thickness)
            # Write gaze_x and gaze_y to the text file separated by a colon
            file.write(f'{gaze_x};{gaze_y}\n')

            # Draw a rectangle around each detected eye
            cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)

            # Draw a circle at the estimated gaze point
            cv2.circle(frame, (gaze_x, gaze_y), 5, (0, 0, 255), -1)



    # Display the frame with detected faces, eyes, and estimated gaze point
    cv2.imshow('Gaze Tracking', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam, close the window, and close the text file
cap.release()
cv2.destroyAllWindows()
file.close()
