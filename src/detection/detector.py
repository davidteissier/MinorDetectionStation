import numpy as np
from astropy.io import fits
from scipy.ndimage import gaussian_filter

class MovingObjectDetector:
    def __init__(self, threshold=3.0, min_area=5):
        self.threshold = threshold
        self.min_area = min_area
    
    def detect_objects(self, image_series):
        """
        Detect moving objects in a series of images
        Args:
            image_series: List of numpy arrays containing consecutive images
        Returns:
            List of detected object coordinates
        """
        if len(image_series) < 3:
            raise ValueError("At least 3 images are required for detection")
        
        # Create difference images
        diff_images = []
        for i in range(len(image_series) - 1):
            diff = image_series[i + 1] - image_series[i]
            diff_images.append(diff)
        
        # Apply noise reduction
        smoothed_diffs = [gaussian_filter(diff, sigma=1) for diff in diff_images]
        
        # Detect significant changes
        detections = self._find_significant_changes(smoothed_diffs)
        
        return detections
    
    def _find_significant_changes(self, diff_images):
        """Find significant changes in difference images"""
        # TODO: Implement detection algorithm
        return []