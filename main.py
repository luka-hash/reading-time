# Copyright © 2023 Luka Ivanović
# This code is licensed under the 2-clause BSD licence (see LICENCE for details)

import unicodedata
import nltk
import argparse
import sys
import math

WPM = 200


def isPunct(word: str) -> bool:
    return all(
        # P is for punctiation
        unicodedata.category(char).startswith('P') for char in word
    )


def countWords(text: str) -> int:
    wc = 0
    for word in nltk.word_tokenize(text):
        if not isPunct(word):
            wc += 1
    return wc


def readingTime(text: str, wpm: int) -> float:
    wc = countWords(text)
    return wc/wpm


def main(args: list[str]):
    text = None
    if args.input == "stdin":
        text = sys.stdin.read()
    else:
        with open(args.input) as f:
            text = f.read()
    filename = "given file" if args.input == "stdin" else f"'{args.input}'"
    rt = math.ceil(readingTime(text, int(args.wpm)))
    print(f"Readig {filename} will take aproximately {rt} minutes.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate the time required to read the text based \
                on the average WPM."
    )
    parser.add_argument(
        "--wpm",
        default=WPM,
        help="choose non-default WPM (default=200)"
    )
    parser.add_argument(
        "--input",
        default="stdin",
        help="choose the file to calculate reading time for (default=stdin)"
    )
    args = parser.parse_args()
    main(args)
