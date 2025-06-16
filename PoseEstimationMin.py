import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture("PoseVideos/1.mp4")
pTime = 0

while True:
    success, img = cap.read()

    if not success or img is None:
        print("Video has ended. Press any key to exit.")
        cv2.waitKey(0)  # Wait indefinitely for a key press
        break

    cTime = time.time()
    time_diff = cTime - pTime
    fps = 1 / time_diff if time_diff > 0 else 0
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (70, 50),
                cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)

    # Break on 'q' key
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
