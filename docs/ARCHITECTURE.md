# Architecture Overview

## System Design

The ReID-DeepSORT-ByteTrack project follows a modular architecture with clear separation of concerns:

```
┌─────────────────┐
│   main.py       │  Entry point & CLI
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ config_utils.py │  Configuration loading & validation
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  detector.py    │  YOLOv8 person detection
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│video_processor  │  Video I/O & frame annotation
└─────────────────┘
```

## Component Descriptions

### 1. Configuration Management (`config_utils.py`)

Handles loading and validation of YAML configuration files.

**Key Functions:**
- `load_config()`: Loads YAML configuration
- `validate_config()`: Validates required configuration structure

### 2. Person Detector (`detector.py`)

Wraps YOLOv8 model for person detection with configurable parameters.

**Key Features:**
- Confidence thresholding
- Class filtering
- Device management (CPU/GPU)

**Methods:**
- `detect_persons()`: Run detection on a frame
- `get_class_name()`: Resolve COCO class ID to label
- `get_model_info()`: Retrieve model metadata

### 3. Video Processor (`video_processor.py`)

Manages video I/O, frame processing, and annotation.

**Key Features:**
- Detection on original resolution for accuracy
- Automatic output resolution adjustment
- Progress tracking
- Frame annotation (boxes, labels)
- Statistics reporting
- Guaranteed resource cleanup on error or interrupt

**Methods:**
- `process_video()`: Main processing loop
- `_calculate_output_dimensions()`: Maintain aspect ratio
- `_annotate_frame()`: Draw detections on frame

### 4. Main Entry Point (`main.py`)

Orchestrates the entire pipeline with CLI support.

**Features:**
- Command-line argument parsing
- Error handling
- Pipeline initialization
- Runtime filesystem checks (video file existence)

## Data Flow

```
Input Video
    ↓
Load Original Frame
    ↓
YOLO Detection (on original resolution)
    ↓
Filter by Class & Confidence
    ↓
Scale Detections to Output Resolution
    ↓
Resize Frame
    ↓
Annotate Frame
    ↓
Write to Output Video
    ↓
Statistics & Reports
```

## Future Architecture Extensions

### Phase 1: Tracking Integration
```
Detection → Feature Extraction → Association → Tracking
```

### Phase 2: Re-ID Pipeline
```
Detection → ReID Features → Gallery Matching → Identity Assignment
```

### Phase 3: Multi-Camera
```
Camera 1 ─┐
Camera 2 ─┼→ Global Tracker → Cross-Camera ReID
Camera N ─┘
```

## Design Patterns Used

1. **Dependency Injection**: Components receive dependencies via constructor
2. **Configuration Object**: Centralized configuration management
3. **Single Responsibility**: Each module has one clear purpose
4. **Factory Pattern**: Model instantiation abstracted in detector

## Performance Considerations

- **Detection Accuracy**: Inference runs on original resolution; only annotations are scaled
- **Memory Management**: Frames processed sequentially to limit memory
- **GPU Utilization**: Supports CUDA for accelerated inference
- **I/O Optimization**: Using OpenCV VideoWriter for efficient encoding
- **Resource Safety**: Video capture and writer are always released via `try...finally`
