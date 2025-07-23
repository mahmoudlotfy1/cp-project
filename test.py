from file_reader import Filetext
from child_class import child
import os

def test_line_num():
    with open("testfile.txt", "w") as f:
        f.write("Line 1\nLine 2\n")
    assert Filetext.line_num("testfile.txt") == 2
    os.remove("testfile.txt")

def test_add_files():
    with open("a.txt", "w") as f:
        f.write("Hello")
    with open("b.txt", "w") as f:
        f.write("World")

    file1 = Filetext("a.txt")
    file2 = Filetext("b.txt")
    combined = file1 + file2
    assert isinstance(combined, Filetext)
    os.remove("a.txt")
    os.remove("b.txt")
    os.remove("new.txt")

def test_word_count():
    with open("sample.txt", "w") as f:
        f.write("One two three.")
    c = child("sample.txt")
    assert c.word_count() == 3
    os.remove("sample.txt")
