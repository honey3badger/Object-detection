"""
Configuration file for Object Detection System
"""

# Detection Settings
CONFIDENCE_THRESHOLD = 0.5  # Minimum confidence for object detection (0.0 - 1.0)
NMS_THRESHOLD = 0.4  # Non-maximum suppression threshold

# Camera Settings
CAMERA_INDEX = 0  # Default camera (0 for built-in, 1 for external)
CAMERA_WIDTH = 640  # Camera resolution width
CAMERA_HEIGHT = 480  # Camera resolution height
CAMERA_FPS = 30  # Target FPS

# Display Settings
SHOW_CONFIDENCE = True  # Show confidence scores on bounding boxes
SHOW_LABELS = True  # Show class labels on bounding boxes
FONT_SCALE = 0.6  # Font size for labels
BOX_THICKNESS = 2  # Thickness of bounding boxes

# Web Interface Settings
WEB_PORT = 5000  # Port for web interface
WEB_HOST = '0.0.0.0'  # Host for web interface
WEB_DEBUG = False  # Debug mode for web interface

# Model Settings
MODEL_NAME = 'fasterrcnn_resnet50_fpn'  # Pre-trained model to use
USE_GPU = True  # Use GPU if available

# Performance Settings
MAX_DETECTIONS = 100  # Maximum number of detections per frame
SKIP_FRAMES = 0  # Skip frames for performance (0 = no skipping)

# Colors (BGR format)
COLORS = {
    'box': (0, 255, 0),  # Green for bounding boxes
    'text': (0, 0, 0),   # Black for text
    'background': (0, 255, 0),  # Green for label background
}

# Logging Settings
LOG_LEVEL = 'INFO'  # Logging level (DEBUG, INFO, WARNING, ERROR)
LOG_FILE = 'detection.log'  # Log file name
