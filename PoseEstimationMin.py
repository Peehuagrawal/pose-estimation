import cv2
import mediapipe as mp
import time

myPose= mp.solutions.pose
pose= myPose.Pose()
cap = cv2.VideoCapture("PoseVideos/4.mp4")
pTime = 0
mpDraw= mp.solutions.drawing_utils


while True:
    success, img = cap.read()
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results= pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, myPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            print(id, lm)

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
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
