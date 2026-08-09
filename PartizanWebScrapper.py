import re
import requests
from bs4 import BeautifulSoup
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

url = "https://en.wikipedia.org/wiki/2021%E2%80%9322_KK_Partizan_season"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
aba_heading = soup.find(id="Adriatic_League")
if aba_heading is None:
    raise SystemExit("Could not find the Adriatic League section on the page.")

match_tables = []
for tag in aba_heading.find_all_next():
    if tag.name == "h2" and tag is not aba_heading:
        break
    if tag.name == "table" and "mw-collapsible" in (tag.get("class") or []):
        h3 = tag.find_previous("h3")
        heading = h3.get_text(" ", strip=True) if h3 else ""
        if heading in {"Matches", "Quarterfinals", "Semifinals", "Finals", "Playoffs"}:
            match_tables.append(tag)

if not match_tables:
    raise SystemExit("Could not find any Adriatic League match tables.")


def parse_score(value):
    match = re.search(r"(\d+)", value)
    return int(match.group(1)) if match else None


def parse_referees(text):
    match = re.search(r"Referees(?:\s*[:|])*\s*(.+)$", text)
    return match.group(1).strip() if match else ""


def parse_match(table):
    rows = [tr.get_text(" | ", strip=True) for tr in table.find_all("tr")]
    if len(rows) < 1:
        return None

    first = [part.strip() for part in rows[0].split("|") if part.strip()]
    if len(first) < 7:
        return None

    date = first[0]
    match_number = first[1]
    team_a = first[2]
    score_a = parse_score(first[3])
    score_b = parse_score(first[4])
    team_b = first[5]
    location = first[6]

    if score_a is None or score_b is None:
        return None

    if "Partizan" in team_a:
        partizan_score = score_a
        opponent_score = score_b
        opponent = team_b
        venue = "home"
    else:
        partizan_score = score_b
        opponent_score = score_a
        opponent = team_a
        venue = "away"

    if partizan_score > opponent_score:
        outcome = "W"
    elif partizan_score < opponent_score:
        outcome = "L"
    else:
        outcome = "D"

    referees = parse_referees(rows[-1])
    if not referees and len(rows) > 1:
        referees = parse_referees(" ".join(rows[1:]))

    return {
        "date": date,
        "match_number": match_number,
        "opponent": opponent,
        "venue": venue,
        "location": location,
        "score": f"{partizan_score}-{opponent_score}",
        "outcome": outcome,
        "referees": referees,
    }


matches = [parse_match(table) for table in match_tables]
matches = [m for m in matches if m and "Hordov" in m["referees"]]

for match in matches:
    print(
        f"{match['date']} | vs {match['opponent']} | {match['score']} | {match['outcome']} | Referees: {match['referees']}"
    )
