# reading-time

Calculate the time required for reading texts (plain texts).

## Requirements and installation

- python3
- venv
- network connection

1. create and activate virtual environment
    - `python -m venv env`
    - `source env/bin/activate.fish` depending on your shell (bash, zsh, etc.)
2. install requirements
    - `pip install -r requirements.txt`
3. install nltk data
    - `python setup.py`

## Usage

```
usage: main.py [-h] [--wpm WPM] [--input INPUT]

Calculate the time required to read the text based on the average WPM.

options:
  -h, --help     show this help message and exit
  --wpm WPM      choose non-default WPM
  --input INPUT  choose the file to calculate reading time for
```

## Licence

This code is licensed under the 2-clause BSD licence (see LICENCE for details).

