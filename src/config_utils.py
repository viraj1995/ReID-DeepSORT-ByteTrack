"""
Configuration management utilities for ReID-DeepSORT-ByteTrack.
"""

import yaml
from pathlib import Path
from typing import Dict, Any


def load_config(config_path: str = "config/config.yaml") -> Dict[str, Any]:
    """
    Load configuration from YAML file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Dictionary containing configuration parameters
    """
    config_file = Path(config_path)
    
    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    return config


def validate_config(config: Dict[str, Any]) -> bool:
    """
    Validate configuration parameters.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        True if configuration is valid
        
    Raises:
        ValueError: If configuration is invalid
    """
    required_keys = ['model', 'video', 'detection']
    
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required configuration section: {key}")
    
    # Validate video input path
    video_path = Path(config['video']['input_path'])
    if not video_path.exists():
        raise FileNotFoundError(f"Input video not found: {video_path}")
    
    return True


def get_model_path(config: Dict[str, Any]) -> Path:
    """
    Get the full path to the model weights.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        Path object pointing to model weights
    """
    model_name = config['model']['name']
    model_dir = Path(config['model']['path'])
    
    # If model_path is relative, make it absolute
    if not model_dir.is_absolute():
        model_dir = Path.cwd() / model_dir
    
    return model_dir / model_name
