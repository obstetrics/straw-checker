# Straw\.Page Username Availability Checker

## Features

* Generates random lowercase usernames of fixed length (default 3 characters).
* Checks username availability via the API endpoint:

  ```
  https://straw.page/power/exists?site={username}
  ```
* Displays results in color:

  * Green for available usernames.
  * Red for unavailable usernames.
  * Yellow for errors or unknown responses.
* Saves valid (available) usernames to `valid.txt`.
* Runs continuously until stopped.

## Requirements

* Python 3.6+
* `cloudscraper`
* `colorama`

Install dependencies with:

```bash
pip install cloudscraper colorama
```

## Useful Links

* Every last Straw\.Page 2-character username list:
  [https://files.catbox.moe/4145p8.txt](https://files.catbox.moe/4145p8.txt)

* Every last Straw\.Page 3-character username list (22k+ entries):
  [https://files.catbox.moe/hu1prl.txt](https://files.catbox.moe/hu1prl.txt)
