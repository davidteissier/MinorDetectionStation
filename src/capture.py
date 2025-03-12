from .sun_calculator import SunCalculator
from datetime import datetime
import time
import cv2
import os
import configparser

class CameraCapture:
    def __init__(self, config_path='../config.ini'):
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
        cap = cv2.VideoCapture(self.camera_device)
        
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

def main():
    sun_calc = SunCalculator()
    camera = CameraCapture()
    
    while True:
        if sun_calc.is_dark():
            # It's dark enough to capture
            camera.capture_image()
            # Wait for the specified interval
            time.sleep(int(camera.config['Capture']['capture_interval']))
        else:
            # Wait for next sunset
            next_event = sun_calc.time_until_next_event()
            print(f"Waiting for {next_event['event']} in {next_event['time_until']}")
            # Sleep for a while before checking again
            time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    main()