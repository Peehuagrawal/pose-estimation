import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self,mode=False, upBody=False, smooth=True, detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.upBody=upBody
        self.smooth=smooth
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mpDraw= mp.solutions.drawing_utils
        self.myPose= mp.solutions.pose
        self.pose = self.myPose.Pose(
                    static_image_mode=self.mode,
                    model_complexity=1,
                    smooth_landmarks=self.smooth,
                    enable_segmentation=False,
                    min_detection_confidence=self.detectionCon,
                    min_tracking_confidence=self.trackCon
                )

    
    def findPose(self, img, draw=True):
        imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results= self.pose.process(imgRGB)
        #print(results.pose_landmarks)
        if draw:
            if results.pose_landmarks:
                self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.myPose.POSE_CONNECTIONS)
                
        return img
    
    def getPosition(self, img, draw=True):
        for id, lm in enumerate(self.results.pose_landmarks.landmark):
                    h,w,c=img.shape
                    print(id, lm)



def main():
    cap = cv2.VideoCapture("PoseVideos/5.mp4")
    pTime = 0
    detector= poseDetector()

    while True:
        success, img = cap.read()
        detector.findPose(img)
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




if __name__== "__main__":
    main()