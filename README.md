Yolo_Detection

Description:
This project utilizes YOLO v8 for keyword-based search within PDF documents and retrieval of associated images. The README provides a tutorial for installation and execution.

Installation:
Clone the repository:
git clone https://github.com/fatma2705/Yolo_Detection.git

Install dependencies:

pip install PyMuPDF pyyaml PyPDF2 ultralytics

Download the YOLOv8 model weights (e.g., yolov8m.pt) and place them in the project directory.

Execution:
Set up input files:
Place the PDF file to search in the project directory.
Run the script:

python main.py

Check the output:
Extracted images will be saved in the extracted_images directory.
Console output will indicate images found or removed based on the keyword search.
Understanding word IDs:
The script uses a file named coconames.csv included in the project repository.
This file contains word-ID pairs. When searching for a keyword, the script looks up the corresponding ID from coconames.csv and uses it for image detection.

Notes:

Ensure Python and necessary libraries are installed.
YOLOv8 model weights are required for image detection.
Modify the script according to specific project requirements.

Feel free to contribute, report issues, or suggest improvements!
