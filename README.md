# ReID-DeepSORT-ByteTrack

**An experimental framework for accurately identifying objects re-appearing in video frames within a certain time period.**

This project implements a person detection pipeline using YOLOv8, designed as a foundation for experimenting with re-identification techniques like DeepSORT and ByteTrack.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **YOLOv8 Integration**: State-of-the-art object detection for person tracking
- **Configuration-Driven**: Easy customization through YAML configuration files
- **Modular Architecture**: Clean separation of concerns for easy extension
- **Video Processing**: Automatic resolution adjustment and video encoding
- **Real-time Progress**: Progress bars and detailed logging
- **Extensible Design**: Ready for integration with DeepSORT/ByteTrack tracking algorithms

## 📁 Project Structure

```
ReID-DeepSORT-ByteTrack/
├── config/                 # Configuration files
│   └── config.yaml        # Main configuration file
├── data/                  # Input videos and datasets
├── docs/                  # Documentation
├── outputs/               # Processed videos and results
├── src/                   # Source code
│   ├── __init__.py
│   ├── config_utils.py   # Configuration management
│   ├── detector.py       # Person detection module
│   └── video_processor.py # Video processing pipeline
├── tests/                 # Unit tests
├── main.py               # Main entry point
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) CUDA-capable GPU for faster inference

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/viraj1995/ReID-DeepSORT-ByteTrack.git
   cd ReID-DeepSORT-ByteTrack
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download YOLO model** (optional - will auto-download on first run)
   ```bash
   # The model will be automatically downloaded when you run the script
   # Or manually download from: https://github.com/ultralytics/assets/releases
   ```

## ⚡ Quick Start

1. **Place your video** in the `data/` directory
   ```bash
   # Example: data/2-rotated.mp4
   ```

2. **Update configuration** (optional)
   Edit `config/config.yaml` to set your video path and preferences

3. **Run the detection**
   ```bash
   python main.py
   ```

4. **Check output**
   The processed video will be saved in `outputs/output_low_res.mp4`

## ⚙️ Configuration

The `config/config.yaml` file contains all customizable parameters:

### Model Settings
```yaml
model:
  name: "yolov8n.pt"          # Model variant (n, s, m, l, x)
  device: "cpu"               # Device: cpu, cuda, mps
  confidence_threshold: 0.5   # Detection confidence threshold
```

### Video Settings
```yaml
video:
  input_path: "data/2-rotated.mp4"
  output_path: "outputs/output_low_res.mp4"
  output_width: 640           # Output resolution
  codec: "mp4v"              # Video codec
```

### Detection Settings
```yaml
detection:
  target_classes: [0]         # COCO classes (0 = person)
  draw_boxes: true           # Draw bounding boxes
  box_color: [0, 255, 0]     # BGR color
  box_thickness: 2
```

## 💻 Usage

### Basic Usage

```bash
python main.py
```

### Custom Configuration

```bash
python main.py --config config/custom_config.yaml
```

### Using Different Models

Edit `config/config.yaml`:
```yaml
model:
  name: "yolov8s.pt"  # Options: yolov8n, yolov8s, yolov8m, yolov8l, yolov8x
```

### GPU Acceleration

Edit `config/config.yaml`:
```yaml
model:
  device: "cuda"  # Use GPU if available
```

## 🔮 Future Work

This project serves as a foundation for more advanced tracking experiments:

- [ ] **DeepSORT Integration**: Add re-identification features with appearance descriptors
- [ ] **ByteTrack Implementation**: Implement association algorithms for robust tracking
- [ ] **Multi-Object Tracking**: Track multiple persons across frames
- [ ] **Re-ID Metrics**: Evaluate re-identification accuracy
- [ ] **Real-time Processing**: Optimize for live video streams
- [ ] **Custom Training**: Fine-tune models on specific datasets

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for the detection framework
- [DeepSORT](https://github.com/nwojke/deep_sort) for tracking inspiration
- [ByteTrack](https://github.com/ifzhang/ByteTrack) for association techniques

## 📧 Contact

**Viraj** - [@viraj1995](https://github.com/viraj1995)

Project Link: [https://github.com/viraj1995/ReID-DeepSORT-ByteTrack](https://github.com/viraj1995/ReID-DeepSORT-ByteTrack)

---

⭐ If you find this project useful, please consider giving it a star!

