from file_reader import Filetext
from child_class import child
import os
# line number , adding two po
def test_line_num():
    with open("testfile.txt", "w") as f:
        f.write("Line 1\nLine 2\n")
    assert Filetext.line_num("testfile.txt") == 2
    os.remove("testfile.txt")

def test_add_files():
    with open("file1.txt",'w') as f:
        f.write("i am the 1st")
    with open("file2.txt",'w') as f:
        f.write("i am the 2nd")
    f1= Filetext(str('file1.txt'))
    f2= Filetext(str('file2.txt'))
    add= f1 + f2
    expect= "i am the 1st\ni am the 2nd"
    real= '\n'.join(add.text())

    assert real== expect
    os.remove('file1.txt')
    os.remove('file2.txt')
    os.remove('new.txt')
   
    
def test_word_count():
    with open("sample.txt", "w") as f:
        f.write("One two three.")
    c = child("sample.txt")
    assert c.word_count() == 3
    os.remove("sample.txt")





