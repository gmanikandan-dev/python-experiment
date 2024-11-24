# Background Removal Tool

This Python tool removes backgrounds from images using the `rembg` library.

## Features
- Remove background from single images
- Process multiple images in a directory
- Supports various image formats (PNG, JPG, JPEG)
- Preserves transparency in output images

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Single Image Processing
```bash
python remove_bg.py --input path/to/image.jpg --output output.png
```

### Directory Processing
```bash
python remove_bg.py --input path/to/input/directory --output path/to/output/directory
```

## Arguments
- `--input`: Path to input image or directory
- `--output`: Path to output image or directory
- `--batch`: (Optional) Process all images in the input directory
