import json
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from config import settings

client = MistralClient(api_key=settings.MISTRAL_API_KEY)


async def detect_options_llm(query: str) -> bool:
    """
    Определяет наличие вариантов ответа в вопросе с помощью LLM
    Возвращает True/False с объяснением решения
    """
    try:
        prompt = f"""
        Проанализируй вопрос и определи, содержит ли он явные варианты ответов в формате нумерованного списка.
        Вопрос: {query}

        Ответь строго в JSON-формате:
        {{
            "has_options": true/false,
            "reason": "краткое объяснение решения"
        }}
        """

        response = client.chat(
            model="mistral-large-latest",
            messages=[ChatMessage(role="user", content=prompt)],
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return result.get("has_options", False)

    except Exception as e:
        print(f"Options detection error: {str(e)}")
        return False
