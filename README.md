# **Description 🚀:**<br>
The code showcases real-time shape detection in video streams using OpenCV. It defines a `ShapeDetector` class with methods for contour analysis, filtering, and shape identification. The implementation is user-friendly, allowing termination with the 'q' key. Overall, it demonstrates effective utilization of computer vision techniques for dynamic shape recognition in videos.

# **Steps Involved 🛠️:**
1. 📚 Import necessary libraries: `math`, `numpy`, and `cv2`.
2. 🎨 Define a `ShapeDetector` class.
3. ⚙️ Initialize class attributes: `scale`, `cap` (video capture), and `out` (video writer).
4. 🔍 Define a `detect_shape` method within the class.
5. 🔄 Approximate the polygonal curve of a contour using `cv2.approxPolyDP`.
6. 🚧 Filter out small and non-convex contours.
7. 📏 Identify shapes based on the number of vertices in the approximated contour:
   - For triangles, return "Triangle."
   - For quadrilaterals, further distinguish between rectangles and squares based on aspect ratio.
   - For other cases, identify circles based on aspect ratio and area.
8. ⚙️ Define a `process_video` method within the class.
9. 🔄 Enter a loop to process video frames while the capture is open.
10. 📷 Read a frame from the video capture.
11. 🖼️ Resize the frame, convert it to grayscale, and apply Canny edge detection.
12. 🔍 Find contours in the processed frame.
13. 🔄 Iterate through contours and detect shapes using the `detect_shape` method.
14. 🎨 If a shape is detected, draw the shape name on the original frame.
15. 📺 Display the frame with shape names.
16. ⏹️ Break the loop if the 'q' key is pressed.
17. 🗑️ Release the video capture object and close all OpenCV windows.
18. 🎯 Define the entry point of the script.
19. 🚀 Create an instance of `ShapeDetector` and process the video.







# Output

![image](https://github.com/Prateekshayuvaraj/shapededuction/assets/123887021/effd07c1-c1fe-4ba7-9aea-8f86066c91ac)
