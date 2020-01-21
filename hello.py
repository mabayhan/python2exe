#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Murat"
__version__ = "0.0.1"
__license__ = "GPL"


def main():
    vize = input("Vize (%20)\t: ")
    sozlu = input("Sozlu (%20)\t: ")
    final = input("Final (%60)\t: ")
    print(int(vize) * 0.2 + int(sozlu) * 0.2 + int(final) * 0.4)


if __name__ == "__main__":
    main()