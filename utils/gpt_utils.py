import os
from openai import OpenAI
from dotenv import load_dotenv

# Загружаем .env
load_dotenv()

# Создаём клиент с API-ключом
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_homework(text: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Или "gpt-3.5-turbo" — если хочешь дешевле
            messages=[
                {"role": "system", "content": "Ты учитель. Проверь домашнюю работу и дай обратную связь."},
                {"role": "user", "content": text}
            ],
            temperature=0.3,
            max_tokens=700
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Ошибка GPT: {e}"
