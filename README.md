# Task_13.2
### Simple Shape and Color Detection Using Classical Methods

### Techniques for Shape Detection

1. **Edge Detection**:  
   Canny edge detection is used to find the edges of shapes in the image. This highlights the boundaries of shapes, which can be used to find contours.
   
   ```python
   edges = cv2.Canny(gray_image, 50, 150)
   ```

2. **Contour Detection**:  
   Contours are the outlines of shapes, detected using the `cv2.findContours()` function. Contours are the boundaries of the detected shapes.
   
   ```python
   contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   ```

3. **Polygon Approximation**:  
   Each contour is approximated to a polygon using `cv2.approxPolyDP()`. The number of vertices of this polygon helps classify the shape:
   - 3 vertices: **Triangle**
   - 4 vertices: **Square/Rectangle** (Square if width ≈ height)
   - More than 4 vertices: **Circle**
   
   ```python
   approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
   ```

4. **Shape Classification**:  
   Shapes are classified based on the number of vertices in the approximated contour:
   - **Triangle**: 3 vertices
   - **Square/Rectangle**: 4 vertices (Square if width ≈ height)
   - **Circle**: More than 4 vertices
   - 
### Techniques for Color Detection

**Color Detection Function**:

A mask is created from the contour, and the mean color value inside the shape is extracted. This value is then converted to HSV to classify the color:
```python
    mask = np.zeros_like(image)
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
    mean_val = cv2.mean(image, mask=mask[:,:,0])
    hsv = cv2.cvtColor(np.uint8([[mean_val[:3]]]), cv2.COLOR_BGR2HSV)[0][0]
```
Then color is decided based  on the mean color value:

Red: 0° ≤ hue ≤ 10° or hue ≥ 160°
Green: 35° < hue < 85°
Blue: 100° < hue ≤ 130°
Yellow: 20° ≤ hue ≤ 30°

---

### Resources

1. **YouTube Channel**: For more tutorials and hands-on coding sessions, check out [CreepyD246](https://www.youtube.com/@CreepyD246) and the **MIA Sessions**.
   
2. **ChatGPT**: some tips to write the code , error fixing , helped me to form this README file And fix some spelling errors
---
