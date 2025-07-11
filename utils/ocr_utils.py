from google.cloud import vision
from dotenv import load_dotenv
import io
import os

# Загружаем переменные окружения из .env (в т.ч. путь к JSON-ключу)
load_dotenv()

def extract_text_from_image(image_path: str) -> str:
    """
    Распознаёт текст с изображения с помощью Google Vision OCR.
    Возвращает текст или сообщение об ошибке.
    """
    try:
        # Создаём клиент для Google Cloud Vision
        client = vision.ImageAnnotatorClient()

        # Читаем изображение как байты
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.text_detection(image=image)

        # Проверка на ошибку от API
        if response.error.message:
            return f"❌ API Error: {response.error.message}"

        # Если текст найден
        texts = response.text_annotations
        if texts:
            return texts[0].description.strip()

        return "❌ Ничего не распознано"

    except Exception as e:
        return f"❌ Ошибка Google OCR: {e}"
