# Thread-Detection-using-openCV
This project detects and counts the number of threads in an image using **OpenCV** and **Python**. The script processes the image, applies adaptive thresholding, detects contours, and draws bounding boxes around detected threads while displaying the total count.
## ⚡ Features
- **Automatic thread detection** using contour analysis
- **Adaptive Thresholding** for better accuracy
- **Noise Removal** using Morphological Operations
- **Bounding Box Visualization** for detected threads
- **Thread Count Display** on the image

## 📂 Prerequisites
Ensure you have the following installed before running the script:
- Python 3.x
- OpenCV
- NumPy

## 🛠 Installation
Clone this repository and install the required dependencies:
```bash
# Clone the repository
git clone https://github.com/yourusername/thread-detection.git
cd thread-detection

# Install dependencies
pip install opencv-python numpy
```
```
## 🚀 Usage
1. **Place your image** (e.g., `bolt.jpg`) in the project folder.
2. **Run the script** using:
   ```bash
   python thread_detection.py
```
```
### The script will:
- Read the input image.
- Convert it to grayscale.
- Apply thresholding & noise removal.
- Detect contours and draw bounding boxes.
- Display the processed image with the detected thread count.
```
```
### Output Images:
- **processed_threads.jpg** → Image with detected threads and count.
- **thread_extracted.jpg** → Binary image showing extracted threads.
```
