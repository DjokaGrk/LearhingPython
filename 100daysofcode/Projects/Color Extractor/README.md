# Color Extractor

This project is a simple Python script that extracts the dominant colors from an image.

## About The Project

This script uses the `colorgram.py` library to analyze an image and identify the most prominent colors. It then outputs these colors as a list of RGB tuples.

## Features

*   Extracts a specified number of dominant colors from a JPG image.
*   Converts the extracted colors into RGB format.
*   Prints the list of RGB color tuples to the console.

## How to Run

1.  **Install the required library:**

    ```bash
    pip install colorgram.py
    ```

2.  **Place an image file** named `image.jpg` in the same directory as the script.

3.  **Run the script** from your terminal:

    ```bash
    python main.py
    ```

The script will print a list of RGB tuples representing the dominant colors in the image.

## Project Structure

*   `main.py`: The main Python script that performs the color extraction.
*   `image.jpg`: The input image file from which colors are extracted.
