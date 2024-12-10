import cv2
import imutils
import numpy as np

# Seçim noktalarını saklamak için bir liste
points = []
font = cv2.FONT_HERSHEY_SIMPLEX

video_path = "kampus.mp4"
cap = cv2.VideoCapture(video_path)

window_name = "ROI"
cv2.namedWindow(window_name)

def mouse_callback(event, x, y, flags, param):
    global frame
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print("x:{} y:{}".format(x, y))
        
        # Noktaları ve çizimleri güncellemek için görüntüyü yeniden çiz
        frame_copy = frame.copy()
        for point in points:
            cv2.circle(frame_copy, point, 5, (0, 0, 255), -1)
            cv2.putText(frame_copy, str(point), point, font, 0.5, (0, 0, 255), 2)
        if len(points) > 1:
            cv2.polylines(frame_copy, [np.array(points)], False, (0, 255, 0), 2)
        cv2.imshow(window_name, frame_copy)

cv2.setMouseCallback(window_name, mouse_callback)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = imutils.resize(frame, width=1280)
    frame_copy = frame.copy()
    
    # Mevcut noktaları her karede çiz
    for point in points:
        cv2.circle(frame_copy, point, 5, (0, 0, 255), -1)
        cv2.putText(frame_copy, str(point), point, font, 0.5, (0, 0, 255), 2)
    if len(points) > 1:
        cv2.polylines(frame_copy, [np.array(points)], False, (0, 255, 0), 2)
    
    cv2.imshow(window_name, frame_copy)
    
    key = cv2.waitKey(1)
    if key == 27:  # ESC tuşuna basıldığında çık
        cv2.imwrite("roi.png", frame_copy)
        break

cap.release()
cv2.destroyAllWindows()
