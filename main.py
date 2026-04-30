"""
Main entry point for ReID-DeepSORT-ByteTrack experiment.
"""

import argparse
from pathlib import Path
import sys

from src.config_utils import load_config, validate_config
from src.detector import PersonDetector
from src.video_processor import VideoProcessor


def main():
    """
    Main function to run the person detection pipeline.
    """
    parser = argparse.ArgumentParser(
        description="Person Detection using YOLOv8"
    )
    parser.add_argument(
        '--config',
        type=str,
        default='config/config.yaml',
        help='Path to configuration file (default: config/config.yaml)'
    )

    args = parser.parse_args()

    try:
        print("Loading configuration...")
        config = load_config(args.config)

        print("Validating configuration...")
        validate_config(config)

        # Check video file exists at runtime
        video_path = Path(config['video']['input_path'])
        if not video_path.exists():
            raise FileNotFoundError(f"Input video not found: {video_path}")

        # Initialize detector
        print("Initializing person detector...")
        model_name = config['model']['name']
        detector = PersonDetector(
            model_path=model_name,
            device=config['model']['device'],
            confidence_threshold=config['model']['confidence_threshold']
        )

        # Initialize video processor
        print("Initializing video processor...")
        processor = VideoProcessor(detector, config)

        # Process video
        processor.process_video()

        print("\nSuccessfully completed!")

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
