# ReID-DeepSORT-ByteTrack

An experimental framework for accurately identifying objects re-appearing in video frames within a certain time period.

This project implements a person detection pipeline using YOLOv8, designed as a foundation for experimenting with re-identification techniques like DeepSORT and ByteTrack.

## Features

- **YOLOv8 Integration**: State-of-the-art object detection for person tracking
- **Configuration-Driven**: Easy customization through YAML configuration files
- **Modular Architecture**: Clean separation of concerns for easy extension
- **Video Processing**: Automatic resolution adjustment and video encoding

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

1. Place your video in the `data/` directory
2. Update `config/config.yaml` if needed
3. Run:

```bash
python main.py
```

The processed video will be saved in `outputs/output_low_res.mp4`.

## Configuration

Edit `config/config.yaml`:

```yaml
model:
  name: "yolov8n.pt"          # Model variant (n, s, m, l, x)
  device: "cpu"               # cpu, cuda, mps
  confidence_threshold: 0.5

video:
  input_path: "data/2-rotated.mp4"
  output_path: "outputs/output_low_res.mp4"
  output_width: 640
  codec: "mp4v"

detection:
  target_classes: [0]         # COCO classes (0 = person)
  draw_boxes: true
  draw_labels: true
  box_color: [0, 255, 0]
  box_thickness: 2
  label_font_scale: 0.5
  label_thickness: 2
```

## Usage

```bash
python main.py                  # Default config
python main.py --config config/custom_config.yaml
```

## License

MIT
