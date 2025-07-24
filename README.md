# Filetext and Child Classes

This Python project implements two classes:

- **Filetext**: A class to work with text files, including features like counting lines and adding contents of two files.
- **child**: A subclass of `Filetext` that adds author information and word count functionality.

## Features

- Count the number of lines in a file (`Filetext.line_num`).
- Concatenate contents of two `Filetext` objects using `+`.
- Count words in a file (`child.word_count`).
- Custom string representation including filename and author (`__str__` method).

## Installation

No external dependencies required. Requires Python 3.x.
