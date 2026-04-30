# Configuration Guide

This guide explains all configuration options available in `config/config.yaml`.

## Configuration File Structure

### Model Configuration

```yaml
model:
  name: "yolov8n.pt"
  device: "cpu"
  confidence_threshold: 0.5
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | string | `yolov8n.pt` | Model name or path. Options: `yolov8n.pt`, `yolov8s.pt`, `yolov8m.pt`, `yolov8l.pt`, `yolov8x.pt` |
| `device` | string | `cpu` | Computation device. Options: `cpu`, `cuda`, `mps` (Mac) |
| `confidence_threshold` | float | `0.5` | Minimum confidence for detections (0.0-1.0) |

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

## Example Configurations

### High Accuracy Configuration

```yaml
model:
  name: "yolov8x.pt"
  device: "cuda"
  confidence_threshold: 0.7

video:
  output_width: 1280
```

### Fast Processing Configuration

```yaml
model:
  name: "yolov8n.pt"
  device: "cuda"
  confidence_threshold: 0.3

video:
  output_width: 416
```

### Multi-Class Detection

```yaml
detection:
  target_classes: [0, 1, 2, 3]
  box_color: [255, 0, 0]
```

## Using Custom Configurations

```bash
python main.py --config config/my_config.yaml
```

## Configuration Validation

The system validates that required configuration sections are present. Input video existence is checked at runtime, not during configuration validation.

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
**Solution**: Try different codec:
```yaml
video:
  codec: "mp4v"
```
