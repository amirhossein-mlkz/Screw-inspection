# Bolt Inspection System

A Python-based bolt inspection software that extracts various bolt dimensions and detects defects using **OpenCV** and **Qt**.

## Features
- **Dimension Measurement:** Extracts bolt diameter, length, and thread count.
- **Defect Detection:** Identifies cracks, missing threads, and deformations.
- **Thread Analysis:** Counts and measures thread length accurately.
- **Graphical User Interface:** Built with **Qt** for ease of use.
- **Real-time Processing:** Supports live inspection from camera input.

## Technologies Used
- **Python**
- **OpenCV** (Computer Vision & Image Processing)
- **Qt** (GUI Development)
- **NumPy & SciPy** (Mathematical Computations)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bolt-inspection.git
   cd bolt-inspection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main_UI.py
   ```

## Sample Screenshots


## Usage
1. Load an image or connect to a live camera.
2. Adjust parameters if needed.
3. Click **"Inspect"** to analyze the bolt.
4. View the extracted measurements and detected defects.

## Future Improvements
- Implement computer vision defect detection.
- Add support for different bolt types.

