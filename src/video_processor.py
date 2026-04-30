"""
Video processing utilities for object detection and annotation.
"""

import cv2
from pathlib import Path
from typing import List, Tuple
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
        input_path = self.video_config['input_path']
        output_path = self.video_config['output_path']

        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video file: {input_path}")

        fps = cap.get(cv2.CAP_PROP_FPS)
        original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        new_width, new_height = self._calculate_output_dimensions(
            original_width, original_height
        )

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        fourcc = cv2.VideoWriter_fourcc(*self.video_config['codec'])
        out = cv2.VideoWriter(output_path, fourcc, fps, (new_width, new_height))

        print(f"Processing video: {input_path}")
        print(f"Output resolution: {new_width}x{new_height}")
        print(f"Total frames: {total_frames}")

        frame_count = 0
        detection_count = 0

        scale_x = new_width / original_width
        scale_y = new_height / original_height

        try:
            with tqdm(total=total_frames, desc="Processing frames") as pbar:
                while cap.isOpened():
                    success, frame = cap.read()
                    if not success:
                        break

                    # Detect on original resolution
                    detections = self.detector.detect_persons(
                        frame,
                        target_classes=self.detection_config['target_classes']
                    )
                    detection_count += len(detections)

                    # Scale detections to output resolution
                    scaled_detections = []
                    for det in detections:
                        x1, y1, x2, y2, confidence, class_id = det
                        sx1 = int(x1 * scale_x)
                        sy1 = int(y1 * scale_y)
                        sx2 = int(x2 * scale_x)
                        sy2 = int(y2 * scale_y)
                        scaled_detections.append((sx1, sy1, sx2, sy2, confidence, class_id))

                    # Resize frame for output
                    output_frame = cv2.resize(frame, (new_width, new_height))

                    # Annotate output frame
                    annotated_frame = self._annotate_frame(output_frame, scaled_detections)
                    out.write(annotated_frame)

                    frame_count += 1
                    pbar.update(1)
        finally:
            cap.release()
            out.release()

        print(f"\nProcessing complete!")
        print(f"Frames processed: {frame_count}")
        print(f"Total detections: {detection_count}")
        avg = detection_count / frame_count if frame_count > 0 else 0.0
        print(f"Average detections per frame: {avg:.2f}")
        print(f"Output saved to: {output_path}")

    def _calculate_output_dimensions(self, width: int, height: int) -> Tuple[int, int]:
        """
        Calculate output dimensions maintaining aspect ratio.
        """
        target_width = self.video_config['output_width']
        aspect_ratio = width / height
        target_height = int(target_width / aspect_ratio)

        return target_width, target_height

    def _annotate_frame(self, frame: np.ndarray, detections: List[Tuple]) -> np.ndarray:
        """
        Draw bounding boxes and labels on frame.
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
                label = f"{self.detector.get_class_name(class_id)}: {confidence:.2f}"
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
