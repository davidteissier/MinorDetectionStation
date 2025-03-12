import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sun_calculator import SunCalculator
from datetime import datetime
import time
import cv2
import configparser

class CameraCapture:
    def __init__(self, config_path='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        
        # Camera settings from config
        self.camera_device = int(self.config['Capture']['camera_device'].replace('/dev/video', ''))
        self.resolution_width = int(self.config['Capture']['resolution_width'])
        self.resolution_height = int(self.config['Capture']['resolution_height'])
        self.exposure_time = float(self.config['Capture']['exposure_time'].replace('s', ''))
        
        # Setup storage paths
        self.data_dir = self.config['Storage']['data_dir']
        self.captured_dir = os.path.join(self.data_dir, self.config['Storage']['captured_dir'])
        os.makedirs(self.captured_dir, exist_ok=True)

    def capture_image(self):
        """Capture a single image from the camera"""
        try:
            cap = cv2.VideoCapture(self.camera_device)
            if not cap.isOpened():
                print("Error: Could not open camera")
                return None
                
            # Set camera properties
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution_width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution_height)
            cap.set(cv2.CAP_PROP_EXPOSURE, self.exposure_time)
            
            ret, frame = cap.read()
            cap.release()
            
            if ret:
                # Generate filename with timestamp
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f'capture_{timestamp}.fits'
                filepath = os.path.join(self.captured_dir, filename)
                
                # Save image
                cv2.imwrite(filepath, frame)
                print(f"Image captured: {filepath}")
                return filepath
            else:
                print("Failed to capture image")
                return None
                
        except Exception as e:
            print(f"Error during capture: {str(e)}")
            return None

def main():
    try:
        sun_calc = SunCalculator(config_path='../config.ini')  # Updated config path
        camera = CameraCapture(config_path='../config.ini')    # Updated config path
        
        print("Starting capture system...")
        print(f"Camera initialized: Device {camera.camera_device}")
        print(f"Resolution: {camera.resolution_width}x{camera.resolution_height}")
        
        while True:
            if sun_calc.is_dark():
                print("Dark enough for capture")
                camera.capture_image()
                time.sleep(int(camera.config['Capture']['capture_interval']))
            else:
                next_event = sun_calc.time_until_next_event()
                print(f"Waiting for {next_event['event']} in {next_event['time_until']}")
                time.sleep(300)  # Check every 5 minutes
                
    except KeyboardInterrupt:
        print("\nCapture system stopped by user")
    except Exception as e:
        print(f"Error in main loop: {str(e)}")

if __name__ == "__main__":
    main()