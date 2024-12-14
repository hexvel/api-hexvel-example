# Image Processing API Client

This is a Python client for the image processing API hosted at `api.hexvel.ru`. The client provides functionality to perform various image processing operations using asynchronous HTTP requests.

## Features

- Pixelate images
- Edge detection
- Image cropping
- Generate quote images with avatars

## Requirements

- Python 3.7+
- aiohttp
- asyncio

## Installation

Create a virtual environment and install the required packages:

```bash
pip install aiohttp
```

## Usage

The client provides several example functions demonstrating different API endpoints:

### Pixelate Image
```python
await pixelate_image_example()
```
Applies a pixelation effect to the input image.

### Edge Detection
```python
await edge_image_example()
```
Detects and highlights edges in the input image.

### Image Cropping
```python
await cut_image_example()
```
Crops the input image.

### Quote Image Generation
```python
await quote_image_example()
```
Generates a quote image with customizable text, avatar, and optional background. Parameters include:
- `fullname`: Author's name
- `time`: Timestamp
- `text`: Quote text
- `avatar`: Author's avatar image

## File Structure

Place your images in the `assets` directory:
- `assets/bg.jpg` - for background images
- `assets/avatar.jpg` - for avatar images in quotes

## Output

Processed images are saved in the current directory with appropriate names:
- `pixelated_image.png`
- `edged_image.png`
- `cropped_image.png`
- `quote_image.png`

## API Endpoints

- `/image/pixelate` - Pixelate effect
- `/image/edge` - Edge detection
- `/image/cut` - Image cropping
- `/image/quote` - Quote image generation

## Error Handling

The client includes basic error handling and will print the status code and error message if the API request fails.


## Examples

All examples are available in the `main.py` file.
