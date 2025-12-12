import os
import asyncio
from fastapi import FastAPI, Header, HTTPException
from app.utils.wiktionary_wotd import get_word_of_the_day
from app.utils.email_utils import send_email, RECIPIENTS
from app.utils.email_template import build_wotd_newsletter_body

app = FastAPI()

@app.get("/api/cron/send-daily")
async def send_daily_email(authorization: str | None = Header(default=None)):
    secret = os.getenv("CRON_SECRET")
    if secret and authorization != f"Bearer {secret}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    word = get_word_of_the_day()
    body = build_wotd_newsletter_body(word=word.word, uri=word.uri)

    await asyncio.to_thread(
        send_email,
        to=RECIPIENTS,
        subject="Lexicron - Word of the day",
        body=body,
        html=True,
    )
    return {"ok": True, "sent": True}


@app.get("/")
async def test():
    return "OK"
