import math
import numpy as np
import cv2

class ShapeDetector:
    def __init__(self):
        self.scale = 1
        self.cap = cv2.VideoCapture(0)

    def detect_shape(self, contour):
        approx = cv2.approxPolyDP(contour, cv2.arcLength(contour, True) * 0.02, True)

        if abs(cv2.contourArea(contour)) < 100 or not cv2.isContourConvex(approx):
            return None

        if len(approx) == 3:
            return "Triangle"
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h
            if 0.95 <= aspect_ratio <= 1.05:
                return "Square"
            else:
                return "Rectangle"
        else:
            area = cv2.contourArea(contour)
            x, y, w, h = cv2.boundingRect(contour)
            radius = w / 2
            if abs(1 - (float(w) / h)) <= 0.2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2:
                return "Circle"
        return None

    def process_video(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                
                resized_frame = cv2.resize(frame, (320, 240))

                gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
                canny = cv2.Canny(gray, 100, 200)  

                contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                for contour in contours:
                    shape = self.detect_shape(contour)
                    if shape:
                        x, y, _, _ = cv2.boundingRect(contour)
                        cv2.putText(frame, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, self.scale, (0, 255, 0), 2, cv2.LINE_AA)

                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    shape_detector = ShapeDetector()
    shape_detector.process_video()
