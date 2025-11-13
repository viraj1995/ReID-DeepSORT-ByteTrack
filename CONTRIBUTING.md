# Contributing to ReID-DeepSORT-ByteTrack

Thank you for considering contributing to this project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear title and description
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)
- Relevant logs or screenshots

### Suggesting Features

Feature suggestions are welcome! Please open an issue with:
- A clear description of the feature
- Use cases and benefits
- Any implementation ideas you have

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/viraj1995/ReID-DeepSORT-ByteTrack.git
   cd ReID-DeepSORT-ByteTrack
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clean, documented code
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Test your changes**
   ```bash
   pytest tests/
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of changes"
   ```
   
   Use conventional commits:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for modifications
   - `Remove:` for deletions
   - `Docs:` for documentation

6. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then open a Pull Request on GitHub.

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and modular
- Use meaningful variable names

### Example

```python
def detect_persons(
    self, 
    frame: np.ndarray, 
    target_classes: List[int] = [0]
) -> List[Tuple]:
    """
    Detect persons in a frame.
    
    Args:
        frame: Input frame (numpy array)
        target_classes: List of COCO class IDs to detect
        
    Returns:
        List of tuples containing (x1, y1, x2, y2, confidence, class_id)
    """
    # Implementation here
```

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for high test coverage
- Use pytest for testing

## Documentation

- Update README.md if needed
- Add docstrings to new functions/classes
- Update ARCHITECTURE.md for structural changes
- Update CONFIGURATION.md for new config options

## Questions?

Feel free to open an issue for any questions about contributing!
