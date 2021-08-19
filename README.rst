# Multi-domain checker

This script allows checking multiple domain names for existence, expiration date and other helpful information.
The script is written in python 3.

Under the hood, it uses the python-whois library, which is just a wrapper around os native whois app.

## Installation
**Clone repository**

```
git clone https://github.com/jffin/cookie_leaked_credentials.git
```

**Install dependencies**

```
python -m pip install -r requirements.txt
```

## Usage
```
usage: entrypoint.py [-h] -i INPUT -o OUTPUT

Domains Expiration

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        File to read targets from
  -o OUTPUT, --output OUTPUT
                        File to save result in
```
