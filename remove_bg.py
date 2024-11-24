import os
import argparse
from pathlib import Path
from rembg import remove
from PIL import Image

def process_image(input_path, output_path):
    """
    Remove background from a single image
    
    Args:
        input_path (str): Path to input image
        output_path (str): Path to save output image
    """
    try:
        # Read input image
        input_image = Image.open(input_path)
        
        # Remove background
        output_image = remove(input_image)
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save the output image
        output_image.save(output_path)
        print(f"Successfully processed: {input_path}")
        
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")

def process_directory(input_dir, output_dir):
    """
    Process all images in a directory
    
    Args:
        input_dir (str): Input directory path
        output_dir (str): Output directory path
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Supported image formats
    supported_formats = {'.png', '.jpg', '.jpeg'}
    
    # Process each image in the directory
    for file in os.listdir(input_dir):
        if Path(file).suffix.lower() in supported_formats:
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, f"nobg_{file}")
            process_image(input_path, output_path)

def main():
    parser = argparse.ArgumentParser(description='Remove background from images')
    parser.add_argument('--input', required=True, help='Input image path or directory')
    parser.add_argument('--output', required=True, help='Output image path or directory')
    parser.add_argument('--batch', action='store_true', help='Process all images in the input directory')
    
    args = parser.parse_args()
    
    if args.batch:
        process_directory(args.input, args.output)
    else:
        process_image(args.input, args.output)

if __name__ == "__main__":
    main()
