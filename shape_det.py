import cv2
import numpy as np

def detect_color(image, contour):
    mask = np.zeros_like(image)
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
    mean_val = cv2.mean(image, mask=mask[:,:,0])

    hsv = cv2.cvtColor(np.uint8([[mean_val[:3]]]), cv2.COLOR_BGR2HSV)[0][0]

    if 35 < hsv[0] < 85:  
        return "green"
    elif 0 <= hsv[0] <= 10 or hsv[0] >= 160: 
        return "red"
    elif 100 < hsv[0] <= 130:  
        return "blue"
    elif 20 <= hsv[0] <= 30:  
        return "yellow"
    else:
        return "undefined"

def detect_shape(contour):
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.03 * peri, True)
    
    if len(approx) == 3:
        return "Triangle"
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        if 0.9 <= aspect_ratio <= 1.15:
            return "Square"
        else:
            return "Rectangle"
    else:
        return "Circle"

image = cv2.imread('test.jpg')
image = cv2.resize(image, (1000,500))
cv2.imshow("Original image",image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 50, 100)
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    if cv2.contourArea(contour) > 100:  
        shape = detect_shape(contour)
        color = detect_color(image, contour)
        
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
        
        cv2.drawContours(image, [contour], -1, (0, 0, 0), 2)
        cv2.putText(image, shape, (cX-60, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.putText(image, color, (cX -5 , cY + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

cv2.imshow("Detected Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
