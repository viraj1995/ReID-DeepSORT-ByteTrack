# Configuration Guide

This guide explains all configuration options available in `config/config.yaml`.

## Configuration File Structure

### Model Configuration

```yaml
model:
  name: "yolov8n.pt"
  path: "models/"
  device: "cpu"
  confidence_threshold: 0.5
  iou_threshold: 0.45
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | string | `yolov8n.pt` | Model filename. Options: `yolov8n.pt`, `yolov8s.pt`, `yolov8m.pt`, `yolov8l.pt`, `yolov8x.pt` |
| `path` | string | `models/` | Directory containing model weights |
| `device` | string | `cpu` | Computation device. Options: `cpu`, `cuda`, `mps` (Mac) |
| `confidence_threshold` | float | `0.5` | Minimum confidence for detections (0.0-1.0) |
| `iou_threshold` | float | `0.45` | IoU threshold for NMS (0.0-1.0) |

**Model Variants:**
- `yolov8n.pt`: Nano (fastest, least accurate)
- `yolov8s.pt`: Small
- `yolov8m.pt`: Medium
- `yolov8l.pt`: Large
- `yolov8x.pt`: Extra Large (slowest, most accurate)

### Video Configuration

```yaml
video:
  input_path: "data/2-rotated.mp4"
  output_path: "outputs/output_low_res.mp4"
  output_width: 640
  codec: "mp4v"
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_path` | string | Required | Path to input video file |
| `output_path` | string | Required | Path for output video |
| `output_width` | int | `640` | Width of output video (height auto-calculated) |
| `codec` | string | `mp4v` | Video codec. Options: `mp4v`, `avc1`, `XVID` |

**Codec Options:**
- `mp4v`: MPEG-4 (widely compatible)
- `avc1`: H.264 (better compression, may require additional codecs)
- `XVID`: Xvid codec (good compatibility)

### Detection Configuration

```yaml
detection:
  target_classes: [0]
  draw_boxes: true
  draw_labels: true
  box_color: [0, 255, 0]
  box_thickness: 2
  label_font_scale: 0.5
  label_thickness: 2
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `target_classes` | list | `[0]` | COCO class IDs to detect |
| `draw_boxes` | bool | `true` | Whether to draw bounding boxes |
| `draw_labels` | bool | `true` | Whether to draw text labels |
| `box_color` | list | `[0, 255, 0]` | Box color in BGR format |
| `box_thickness` | int | `2` | Box line thickness in pixels |
| `label_font_scale` | float | `0.5` | Font size multiplier |
| `label_thickness` | int | `2` | Label text thickness |

**Common COCO Classes:**
- `0`: Person
- `1`: Bicycle
- `2`: Car
- `16`: Dog
- `17`: Cat
- (See [COCO dataset](https://cocodataset.org/#home) for full list)

### Performance Configuration

```yaml
performance:
  batch_size: 1
  verbose: false
  show_progress: true
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `batch_size` | int | `1` | Number of frames to process at once |
| `verbose` | bool | `false` | Show detailed inference logs |
| `show_progress` | bool | `true` | Display progress bar |

## Example Configurations

### High Accuracy Configuration

```yaml
model:
  name: "yolov8x.pt"  # Largest model
  device: "cuda"      # Use GPU
  confidence_threshold: 0.7  # Higher threshold
  
video:
  output_width: 1280  # Higher resolution
```

### Fast Processing Configuration

```yaml
model:
  name: "yolov8n.pt"  # Smallest model
  device: "cuda"      # Use GPU
  confidence_threshold: 0.3  # Lower threshold
  
video:
  output_width: 416   # Lower resolution
```

### Multi-Class Detection

```yaml
detection:
  target_classes: [0, 1, 2, 3]  # person, bicycle, car, motorcycle
  box_color: [255, 0, 0]  # Blue boxes
```

## Creating Custom Configurations

1. Copy the default configuration:
   ```bash
   cp config/config.yaml config/my_config.yaml
   ```

2. Edit your custom configuration:
   ```bash
   # Use your preferred text editor
   notepad config/my_config.yaml
   ```

3. Run with custom configuration:
   ```bash
   python main.py --config config/my_config.yaml
   ```

## Configuration Validation

The system automatically validates:
- Required fields are present
- Input video file exists
- Numeric values are in valid ranges
- Color values are valid BGR tuples

If validation fails, a descriptive error message will be displayed.

## Environment Variables

You can override configuration with environment variables (future feature):

```bash
export REID_MODEL_DEVICE="cuda"
export REID_VIDEO_INPUT="data/my_video.mp4"
python main.py
```

## Troubleshooting

### Video file not found
```
Error: Input video not found: data/2-rotated.mp4
```
**Solution**: Ensure the video file exists at the specified path.

### CUDA out of memory
```
RuntimeError: CUDA out of memory
```
**Solution**: 
- Reduce `output_width` in config
- Use a smaller model (`yolov8n.pt`)
- Switch to CPU: `device: "cpu"`

### Codec not available
```
Warning: codec not available, using fallback
```
**Solution**: Try different codec:
```yaml
video:
  codec: "mp4v"  # or "avc1" or "XVID"
```
