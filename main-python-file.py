# MAIN PYTHON EXECUTION FILE


import cv2
from controller import led  # Import the led function from the controller
from cvzone.HandTrackingModule import HandDetector

# Initialize the hand detector
detector=HandDetector(detectionCon=0.8, maxHands=1)

# Start video capture
video=cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    if not ret:
        break

    # Flip the frame to create a mirror effect
    frame = cv2.flip(frame,1)

    # Detect hands in the frame
    hands,img = detector.findHands(frame)

    if hands:  # Check if a hand is detected
        lmList=hands[0]['lmList']  # Accessing 'lmList' via dictionary key
        fingerUp=detector.fingersUp(hands[0])  # Pass the hand dictionary to fingersUp()

        # Print the detected finger positions (for debugging purposes)
        print(fingerUp)
        
        # Call the LED function from the controller with the finger count (or gesture)
        led(fingerUp)

        # Display the number of fingers detected with smaller text
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(img, 'Finger count: 0', (20, 460), cv2.FONT_ITALIC, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [1, 0, 0, 0, 0]:
            cv2.putText(img, 'Finger count: 1 (Thumb)', (20, 460), cv2.FONT_ITALIC, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(img, 'Finger count: 2 (Index & Middle)', (20, 460), cv2.FONT_ITALIC, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 0]:
            cv2.putText(img, 'Finger count: 3 (Index, Middle & Ring)', (20, 460), cv2.FONT_ITALIC, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 1]:
            cv2.putText(img, 'Finger count: 4 (All but No Thumb)', (20, 460), cv2.FONT_ITALIC, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(img, 'Finger count: 5 (All fingers)', (20, 460), cv2.FONT_ITALIC, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        else:
            cv2.putText(img, 'Unknown Combination', (20, 460), cv2.FONT_ITALIC, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
    
    # Display the processed frame
    cv2.imshow("frame",img)

    # Break the loop if 'k' is pressed
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

# Release resources
video.release()
cv2.destroyAllWindows()
