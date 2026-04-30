"""
Configuration management utilities for ReID-DeepSORT-ByteTrack.
"""

import yaml
from pathlib import Path
from typing import Dict, Any


def load_config(config_path: str = "config/config.yaml") -> Dict[str, Any]:
    """
    Load configuration from YAML file.
    """
    config_file = Path(config_path)

    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    return config


def validate_config(config: Dict[str, Any]) -> bool:
    """
    Validate configuration structure.
    """
    required_keys = ['model', 'video', 'detection']

    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required configuration section: {key}")

    return True
