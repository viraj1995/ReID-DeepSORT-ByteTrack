"""
Main entry point for ReID-DeepSORT-ByteTrack experiment.
"""

import argparse
from pathlib import Path
import sys

from src.config_utils import load_config, validate_config, get_model_path
from src.detector import PersonDetector
from src.video_processor import VideoProcessor


def main():
    """
    Main function to run the person detection pipeline.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Person Detection using YOLOv8",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py
  python main.py --config config/config.yaml
  python main.py --config config/custom_config.yaml
        """
    )
    parser.add_argument(
        '--config',
        type=str,
        default='config/config.yaml',
        help='Path to configuration file (default: config/config.yaml)'
    )
    
    args = parser.parse_args()
    
    try:
        # Load and validate configuration
        print("Loading configuration...")
        config = load_config(args.config)
        
        print("Validating configuration...")
        validate_config(config)
        
        # Initialize detector
        print("Initializing person detector...")
        model_path = get_model_path(config)
        
        # If model doesn't exist, use model name directly (ultralytics will download it)
        if not model_path.exists():
            print(f"Model not found at {model_path}, using model name: {config['model']['name']}")
            model_path = config['model']['name']
        
        detector = PersonDetector(
            model_path=str(model_path),
            device=config['model']['device'],
            confidence_threshold=config['model']['confidence_threshold']
        )
        
        # Initialize video processor
        print("Initializing video processor...")
        processor = VideoProcessor(detector, config)
        
        # Process video
        processor.process_video()
        
        print("\n✓ Successfully completed!")
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Configuration Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
