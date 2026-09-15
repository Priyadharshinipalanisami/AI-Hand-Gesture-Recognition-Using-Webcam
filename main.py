import cv2

from config import CAMERA_INDEX, WINDOW_NAME
from hand_detector import HandDetector
from gesture_recognizer import GestureRecognizer


def main():

    print("--------------------------------------")
    print(" AI HAND GESTURE RECOGNITION")
    print("--------------------------------------")

    print("Supported gestures:")
    print("1. Open Hand")
    print("2. Fist")
    print("3. Thumbs Up")
    print("4. Victory / Peace")

    print("--------------------------------------")
    print("Press Q to exit.")
    print("--------------------------------------")

    
    camera = cv2.VideoCapture(CAMERA_INDEX)

    if not camera.isOpened():

        print("ERROR: Unable to access webcam.")
        return

    detector = HandDetector()
    recognizer = GestureRecognizer()

    while True:

        success, frame = camera.read()

        if not success:

            print("ERROR: Unable to read webcam.")
            break

        frame = cv2.flip(frame, 1)

        result = detector.detect(frame)

        gesture = "No Hand Detected"

        if result.hand_landmarks:

            detector.draw_landmarks(
                frame,
                result
            )

            landmarks = result.hand_landmarks[0]

            gesture = recognizer.recognize(
                landmarks
            )

        cv2.rectangle(
            frame,
            (10, 10),
            (500, 95),
            (0, 0, 0),
            -1
        )

        cv2.putText(
            frame,
            "Gesture:",
            (25, 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            gesture,
            (25, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2
        )

        
        cv2.putText(
            frame,
            "Press Q to Quit",
            (10, frame.shape[0] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

       
        cv2.imshow(
            WINDOW_NAME,
            frame
        )

       
        if cv2.waitKey(1) & 0xFF == ord("q"):

            break

  
    camera.release()
    cv2.destroyAllWindows()

    detector.close()

    print("Application closed.")


if __name__ == "__main__":
    main()