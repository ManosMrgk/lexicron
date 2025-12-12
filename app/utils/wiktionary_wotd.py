from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


WOTD_PAGE_URL = (
    "https://el.wiktionary.org/wiki/"
    "%CE%92%CE%B9%CE%BA%CE%B9%CE%BB%CE%B5%CE%BE%CE%B9%CE%BA%CF%8C:"
    "%CE%9B%CE%AD%CE%BE%CE%B7_%CF%84%CE%B7%CF%82_%CE%97%CE%BC%CE%AD%CF%81%CE%B1%CF%82"
)

BASE_URL = "https://el.wiktionary.org"


@dataclass(frozen=True)
class WordOfTheDay:
    word: str
    uri: str
    date_text: Optional[str] = None


def _abs_url(href: str) -> str:
    href = href.strip()
    if href.startswith("//"):
        return "https:" + href
    return urljoin(BASE_URL, href)


def get_word_of_the_day(session: Optional[requests.Session] = None) -> WordOfTheDay:
    s = session or requests.Session()
    resp = s.get(
        WOTD_PAGE_URL,
        headers={
            "User-Agent": "Lexicron/1.0",
            "Accept-Language": "el,en;q=0.8",
        },
        timeout=20,
    )
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    # Find the heading by id, then the containing <section>
    h2 = soup.find(id="Λέξη_της_Ημέρας")
    if not h2:
        raise RuntimeError("Could not locate the 'Λέξη της Ημέρας' heading.")

    section = h2.find_parent("section")
    if not section:
        raise RuntimeError("Could not locate the <section> containing the word-of-the-day.")

    # Capture a readable "Σήμερα ..." line if present
    date_text = None
    center = section.find("center")
    if center:
        center_text = center.get_text(" ", strip=True)
        if center_text.startswith("Σήμερα"):
            date_text = center_text

    # In that section there are multiple links; we want the entry link (e.g. πυργάκι),
    # not the selflink "το λήμμα της ημέρας" (which points to Βικιλεξικό:...).
    candidates = section.find_all("a", href=True)

    word_a = None
    for a in candidates:
        label = a.get_text(strip=True)
        href = a["href"]

        if not label:
            continue
        if label == "το λήμμα της ημέρας":
            continue
        if "Βικιλεξικό:" in href:
            continue

        # Word link in your HTML looks like //el.wiktionary.org/wiki/<word>
        if "/wiki/" in href:
            word_a = a
            break

    if not word_a:
        raise RuntimeError("Could not extract the word-of-the-day link from the page.")

    word = word_a.get_text(strip=True).strip("«»")
    uri = _abs_url(word_a["href"])

    return WordOfTheDay(word=word, uri=uri, date_text=date_text)


if __name__ == "__main__":
    w = get_word_of_the_day()
    print("WORD:", w.word)
    print("URI :", w.uri)
    if w.date_text:
        print("DATE:", w.date_text)
