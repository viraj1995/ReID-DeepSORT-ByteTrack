"""
Video processing utilities for object detection and annotation.
"""

import cv2
from pathlib import Path
from typing import List, Tuple, Optional
from tqdm import tqdm
import numpy as np

from .detector import PersonDetector


class VideoProcessor:
    """
    Process videos with object detection and annotation.
    """
    
    def __init__(self, detector: PersonDetector, config: dict):
        """
        Initialize the video processor.
        
        Args:
            detector: PersonDetector instance
            config: Configuration dictionary
        """
        self.detector = detector
        self.config = config
        self.video_config = config['video']
        self.detection_config = config['detection']
        
    def process_video(self):
        """
        Process the input video and save annotated output.
        """
        # Open video
        input_path = self.video_config['input_path']
        output_path = self.video_config['output_path']
        
        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video file: {input_path}")
        
        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Calculate new dimensions
        new_width, new_height = self._calculate_output_dimensions(
            original_width, original_height
        )
        
        # Create output directory if it doesn't exist
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*self.video_config['codec'])
        out = cv2.VideoWriter(output_path, fourcc, fps, (new_width, new_height))
        
        print(f"Processing video: {input_path}")
        print(f"Output resolution: {new_width}x{new_height}")
        print(f"Total frames: {total_frames}")
        
        # Process frames
        frame_count = 0
        detection_count = 0
        
        with tqdm(total=total_frames, desc="Processing frames") as pbar:
            while cap.isOpened():
                success, frame = cap.read()
                
                if not success:
                    break
                
                # Resize frame
                frame = cv2.resize(frame, (new_width, new_height))
                
                # Detect persons
                detections = self.detector.detect_persons(
                    frame,
                    target_classes=self.detection_config['target_classes']
                )
                
                detection_count += len(detections)
                
                # Annotate frame
                annotated_frame = self._annotate_frame(frame, detections)
                
                # Write frame
                out.write(annotated_frame)
                
                frame_count += 1
                pbar.update(1)
        
        # Cleanup
        cap.release()
        out.release()
        
        print(f"\nProcessing complete!")
        print(f"Frames processed: {frame_count}")
        print(f"Total detections: {detection_count}")
        print(f"Average detections per frame: {detection_count/frame_count:.2f}")
        print(f"Output saved to: {output_path}")
    
    def _calculate_output_dimensions(self, width: int, height: int) -> Tuple[int, int]:
        """
        Calculate output dimensions maintaining aspect ratio.
        
        Args:
            width: Original width
            height: Original height
            
        Returns:
            Tuple of (new_width, new_height)
        """
        target_width = self.video_config['output_width']
        aspect_ratio = width / height
        target_height = int(target_width / aspect_ratio)
        
        return target_width, target_height
    
    def _annotate_frame(self, frame: np.ndarray, detections: List[Tuple]) -> np.ndarray:
        """
        Draw bounding boxes and labels on frame.
        
        Args:
            frame: Input frame
            detections: List of detections (x1, y1, x2, y2, confidence, class_id)
            
        Returns:
            Annotated frame
        """
        annotated_frame = frame.copy()
        
        for detection in detections:
            x1, y1, x2, y2, confidence, class_id = detection
            
            # Draw bounding box
            if self.detection_config['draw_boxes']:
                color = tuple(self.detection_config['box_color'])
                thickness = self.detection_config['box_thickness']
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, thickness)
            
            # Draw label
            if self.detection_config['draw_labels']:
                label = f"Person: {confidence:.2f}"
                font_scale = self.detection_config['label_font_scale']
                label_thickness = self.detection_config['label_thickness']
                
                cv2.putText(
                    annotated_frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    font_scale,
                    color,
                    label_thickness
                )
        
        return annotated_frame
