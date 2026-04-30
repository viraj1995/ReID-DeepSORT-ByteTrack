"""
YOLO-based person detector for video processing.
"""

from ultralytics import YOLO
from typing import List, Tuple
import numpy as np


class PersonDetector:
    """
    Person detection using YOLO model.
    """

    def __init__(self, model_path: str, device: str = "cpu", confidence_threshold: float = 0.5):
        """
        Initialize the person detector.

        Args:
            model_path: Path to YOLO model weights or model name
            device: Device to run inference on (cpu, cuda, mps)
            confidence_threshold: Minimum confidence for detections
        """
        self.model = YOLO(model_path)
        self.device = device
        self.confidence_threshold = confidence_threshold

    def detect_persons(self, frame: np.ndarray, target_classes: List[int] = [0]) -> List[Tuple]:
        """
        Detect persons in a frame.

        Args:
            frame: Input frame (numpy array)
            target_classes: List of COCO class IDs to detect (default: [0] for person)

        Returns:
            List of tuples containing (x1, y1, x2, y2, confidence, class_id)
        """
        results = self.model(frame, device=self.device, verbose=False)
        detections = []

        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                # Filter by class and confidence
                if class_id in target_classes and confidence >= self.confidence_threshold:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    detections.append((x1, y1, x2, y2, confidence, class_id))

        return detections

    def get_class_name(self, class_id: int) -> str:
        """
        Get the class name for a given COCO class ID.

        Args:
            class_id: COCO class ID

        Returns:
            Class name string
        """
        return self.model.names.get(class_id, f"Class {class_id}")

    def get_model_info(self) -> dict:
        """
        Get information about the loaded model.

        Returns:
            Dictionary with model information
        """
        return {
            "model_type": "YOLOv8",
            "device": self.device,
            "confidence_threshold": self.confidence_threshold
        }
