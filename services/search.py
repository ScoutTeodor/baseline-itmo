from tavily import TavilyClient
from config import settings
import logging
from .rss_parser import parse_itmo_news

tavily = TavilyClient(api_key=settings.TAVILY_API_KEY)


def search(query: str, max_results=3) -> list:
    try:
        response = tavily.search(
            query=f"{query} site:itmo.ru",
            search_depth="advanced",
            max_results=max_results,
            include_answer=True
        )
        return response.get("results", [])[:max_results]
    except Exception as e:
        return []

# def search(query: str, max_results=3) -> list:
#     # Если запрос о новостях - используем RSS
#     if "новости" in query.lower():
#         return parse_itmo_news(max_results)

#     # Обычный поиск через Tavily
#     try:
#         response = tavily.search(
#             query=f"{query} site:itmo.ru",
#             search_depth="advanced",
#             max_results=max_results,
#             include_answer=True
#         )
#         return response.get("results", [])[:max_results]
#     except Exception as e:
#         logging.error(f"Search error: {str(e)}")
#         return []
