import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing packages: {e}")
        return False
    return True

def check_camera():
    """Check if camera is accessible"""
    print("Checking camera access...")
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print("✓ Camera is accessible!")
                cap.release()
                return True
            else:
                print("✗ Could not read from camera")
        else:
            print("✗ Could not open camera")
        cap.release()
    except Exception as e:
        print(f"✗ Camera check failed: {e}")
    return False

def test_detection():
    """Test object detection with a sample image"""
    print("Testing object detection...")
    try:
        from object_detector import ObjectDetector
        import numpy as np
        
        # Create a dummy image for testing
        dummy_image = np.zeros((480, 640, 3), dtype=np.uint8)
        
        detector = ObjectDetector()
        detections = detector.detect_objects(dummy_image)
        
        print("✓ Object detection system is working!")
        return True
    except Exception as e:
        print(f"✗ Object detection test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("=" * 50)
    print("Object Detection System Setup")
    print("=" * 50)
    
    # Install requirements
    if not install_requirements():
        print("Please install packages manually and try again.")
        return
    
    # Check camera
    if not check_camera():
        print("Please check your camera connection and try again.")
    
    # Test detection
    test_detection()
    
    print("\n" + "=" * 50)
    print("Setup Complete!")
    print("=" * 50)
    print("\nTo use the system:")
    print("1. Command line: python object_detector.py")
    print("2. Web interface: python web_app.py")
    print("\nVisit http://localhost:5000 for the web interface")

if __name__ == "__main__":
    main()
