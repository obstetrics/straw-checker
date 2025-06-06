# Straw.Page Username Availability Checker

---

## Features

- Generates random lowercase usernames of fixed length (default 3 characters).
- Checks username availability via the API `https://straw.page/power/exists?site={username}`.
- Displays results in color:
  - Green for available usernames.
  - Red for unavailable usernames.
  - Yellow for errors or unknown responses.
- Saves valid (available) usernames to `valid.txt`.
- Runs continuously until stopped.

---

## Requirements

- Python 3.6+
- `cloudscraper`
- `colorama`

Install dependencies with:

```bash
pip install cloudscraper colorama

# Every Last Straw.Page 2 character username
  `https://files.catbox.moe/4145p8.txt`
