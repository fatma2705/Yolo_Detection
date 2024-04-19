import fitz  
from PyPDF2 import PdfReader
from ultralytics import YOLO
import os 
import shutil

def find_pages_with_keyword(pdf_path, keyword):
    """
    Finds pages containing the specified keyword within a PDF document.

    Args:
        pdf_path (str): The path to the PDF document.
        keyword (str): The keyword to search for.

    Returns:
        list: A list of page numbers containing the keyword.
    """
    found_pages = []

    with fitz.open(pdf_path) as pdf_document:
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            page_text = page.get_text()

            if keyword.lower() in page_text.lower():
                found_pages.append(page_number + 1)

    return found_pages

def extract_images_from_pdf(pdf_path, output_folder):
    """
    Extracts images from a PDF document and saves them to the specified folder.

    Args:
        pdf_path (str): The path to the PDF document.
        output_folder (str): The folder where extracted images will be saved.
    """
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        pdf_document = fitz.open(pdf_path)

        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            images = page.get_images(full=True)

            for img_index, img_info in enumerate(images):
                image_index = img_info[0]
                base_image = pdf_document.extract_image(image_index)
                image_bytes = base_image["image"]

                image_filename = f"page_{page_number + 1}_img_{img_index + 1}.jpg"
                full_path = os.path.join(output_folder, image_filename)
                with open(full_path, "wb") as image_file:
                    image_file.write(image_bytes)

        print("Image extraction completed.")

    except Exception as e:
        print(f"Error during image extraction: {str(e)}")

def detect_images(image_folder, keyword, class_id):
    """
    Detects images containing specified objects using YOLOv5.

    Args:
        image_folder (str): The folder containing images.
        keyword (str): The keyword to match images against.
        class_id (int): The class ID of the object to detect.
    """
    model = YOLO("yolov8m.pt")  
    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)
        results = model.predict(source=image_path, save=True, show=True)
        for result in results:
            boxes = result.boxes  
            if class_id in boxes.cls:
                print(f"Image of {keyword} found.")
            else:
                os.remove(image_path)
                print("Image removed.")

# Example usage
pdf_path = "./dog.pdf"
output_folder = "./extracted_images"

# Extract images from PDF
# extract_images_from_pdf(pdf_path, output_folder)

# Find pages containing the keyword 'dog'
# print(find_pages_with_keyword(pdf_path, "dog"))

# Detect images containing dogs
# detect_images(output_folder, "dog", 16)
