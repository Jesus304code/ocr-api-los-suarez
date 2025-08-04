from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from utils.ocr import extract_text
from utils.barcode import extract_barcode_data
from PIL import Image
import io

app = FastAPI()

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    text = extract_text(image)
    barcode_data = extract_barcode_data(image)

    product_name = next((line for line in text.splitlines() if line.isupper() and len(line) > 3), "DESCONOCIDO")

    weight = "0.00"
    if barcode_data:
        last_digits = barcode_data[-4:]
        try:
            weight = f"{int(last_digits)/100:.2f}"
        except:
            pass

    return JSONResponse(content={
        "producto": product_name,
        "peso_kg": weight,
        "codigo_barras": barcode_data
    })
