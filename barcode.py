from pyzbar.pyzbar import decode
from PIL import Image

def extract_barcode_data(image: Image.Image) -> str:
    decoded_objects = decode(image)
    for obj in decoded_objects:
        return obj.data.decode("utf-8")
    return ""
