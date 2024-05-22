# Image2PDF Converter

This project provides a way to convert WebP images contained within ZIP files into a single PDF for each ZIP file. The conversion process includes extracting ZIP files, converting the WebP images to a PDF, and then cleaning up the extracted files.

## Project Structure

- `lib/`: Contains the Python scripts for handling ZIP extraction and WebP to PDF conversion.
  - `zip.py`: Contains the `open_and_deletezip` function for extracting and deleting ZIP files.
  - `converter.py`: Contains the `convert_webp2pdf` function for converting WebP images to PDF.
- `converter/`: Contains the ZIP files to be processed.
- `pdf/`: The output directory where the generated PDF files will be saved.
- `main.py`: The main script to execute the conversion process.
- `README.md`: This file.

## Setup and Usage

rm -rf venv

### Step 1: Navigate to the Project Directory

Open your terminal and navigate to the project directory:

```sh
cd /path/to/image2pdf

### Step 2: (Optional) Create a Virtual Environment

```sh
python3 -m venv venv


### Step 3: Activate the Virtual Environment

```sh
source venv/bin/activate

### Step 4: Install Required Packages

```sh
pip install pillow

### Step 5: Place ZIP Files in the converter Directory
Ensure that the ZIP files containing the WebP images are placed in the converter directory. Each ZIP file should contain the WebP images you want to convert to PDF.

### Step 6: Run the Script

```sh
python main.py

### Disactivate virtual envirionment
source deactivate
