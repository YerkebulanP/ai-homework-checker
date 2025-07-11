import os
from utils.ocr_utils import extract_text_from_image
from utils.gpt_utils import analyze_homework

if __name__ == "__main__":
    image_path = os.path.join("data", "asd.jpg")

    print("🔍 Распознаём текст...")
    text = extract_text_from_image(image_path)
    print("=== Текст с фото ===")
    print(text)

    print("\n🧠 Отправляем в GPT для проверки...")
    result = analyze_homework(text)
    print("=== Результат GPT ===")
    print(result)
