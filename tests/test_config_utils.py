"""
Unit tests for configuration utilities.
"""

import pytest
from pathlib import Path
import yaml

from src.config_utils import load_config, validate_config


class TestConfigUtils:
    """Test cases for configuration utilities."""

    def test_load_config_file_not_found(self):
        """Test that FileNotFoundError is raised for missing config."""
        with pytest.raises(FileNotFoundError):
            load_config("nonexistent.yaml")

    def test_validate_config_missing_keys(self):
        """Test that validation fails for incomplete config."""
        incomplete_config = {"model": {}}
        with pytest.raises(ValueError):
            validate_config(incomplete_config)


if __name__ == "__main__":
    pytest.main([__file__])
