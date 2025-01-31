import json
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from config import settings

client = MistralClient(api_key=settings.MISTRAL_API_KEY)


async def generate_answer(query: str, context: str) -> dict:
    try:
        prompt = f"""
        Ты эксперт по Университету ИТМО. Выбери правильный вариант ответа (только цифру) на основе контекста.
        Контекст: {context}
        Вопрос: {query}

        Ответь в формате JSON:
        {{
            "answer": "номер правильного варианта (только цифра)",
            "reasoning": "подробное объяснение на русском языке с источниками"
        }}
        """

        response = client.chat(
            # model="mistral-large-latest",
            model="mistral-small-latest",
            messages=[ChatMessage(role="user", content=prompt)],
            response_format={"type": "json_object"},
            temperature=0.3
        )

        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"answer": None, "reasoning": f"LLM Error: {str(e)}"}
