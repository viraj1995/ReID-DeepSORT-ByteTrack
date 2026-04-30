"""
Unit tests for detector module.
"""

import pytest
import numpy as np
from pathlib import Path

from src.detector import PersonDetector


class TestPersonDetector:
    """Test cases for PersonDetector class."""

    def test_get_class_name_unknown(self):
        """Test that unknown class IDs return a fallback string."""
        detector = PersonDetector("yolov8n.pt")
        assert detector.get_class_name(999) == "Class 999"


if __name__ == "__main__":
    pytest.main([__file__])
