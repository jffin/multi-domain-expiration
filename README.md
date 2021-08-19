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

*install with poetry*

```
poetry install
```

*install with pip*

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

## Output
Domain info:
is existing, is expired, if it will expire soon
expiration date, creation date, updated date, country
written to a file in the JSON formats


## Whois Installation
Also, you need to have installed whois on your computer.<br>
In most Linux operating systems, whois is already available.<br>
If not, install it. For example:

For Apple macOS:
```
$ brew install whois
```

For Debian based:
```
$ sudo apt update && sudo apt upgrade
$ sudo apt install whois
```

For RHEL 6.x/RHEL 7.x/CentOS 6.x/CentOS 7.x:
```
$ sudo yum install jwhois
```

For RHEL 8.x/CentOS 8.x/Fedora 22 and higher:
```
$ sudo dnf install jwhois
```

For Arch/Manjaro:
```
$ sudo pacman -S whois
```
