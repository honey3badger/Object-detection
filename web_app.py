from flask import Flask, render_template, Response, jsonify
import cv2
import threading
from object_detector import ObjectDetector

app = Flask(__name__)

# Global variables
camera = None
detector = ObjectDetector(confidence_threshold=0.5)
detection_results = []

def get_camera():
    """Initialize camera"""
    global camera
    if camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0)
    return camera

def generate_frames():
    """Generate frames for video streaming"""
    global detection_results
    camera = get_camera()
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        
        # Detect objects
        detections = detector.detect_objects(frame)
        detection_results = detections
        
        # Draw detections
        frame = detector.draw_detections(frame, detections)
        
        # Encode frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route"""
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detections')
def get_detections():
    """Get current detections"""
    return jsonify(detection_results)

@app.route('/stop_camera')
def stop_camera():
    """Stop camera"""
    global camera
    if camera and camera.isOpened():
        camera.release()
        camera = None
    return jsonify({'status': 'Camera stopped'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
