import cv2

image = cv2.imread("C:\\Users\\josam\\Downloads\\test.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

def classify_shape(contour):
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    
    if len(approx) == 3:
        return "Triangle"
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        if abs(w - h) <= 5:  # Check if width and height are nearly equal
            return "Square"
        else:
            return "Rectangle"
    elif len(approx) > 4:
        return "Circle"
    else:
        return "Unknown"

for contour in contours:
    shape = classify_shape(contour)
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    
    # Get the contour center to place the label
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        cv2.putText(image, shape, (cx - 30, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

cv2.imshow("Shape Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
