import feedparser
from datetime import datetime, timedelta


def parse_itmo_news(max_entries=100):
    """
    Парсит RSS-ленту новостей ИТМО
    Возвращает последние новости за последние 7 дней
    """
    try:
        feed = feedparser.parse("https://news.itmo.ru/ru/rss/")
        week_ago = datetime.now() - timedelta(days=7)

        return [
            {
                "title": entry.title,
                "link": entry.link,
                "date": datetime(*entry.published_parsed[:6]),
                "summary": entry.summary
            }
            for entry in feed.entries
            if datetime(*entry.published_parsed[:6]) > week_ago
        ][:max_entries]

    except Exception as e:
        print(f"RSS parsing error: {str(e)}")
        return []
