from file_reader import Filetext
from child_class import child








#file itself   

file=Filetext('./ll.text')

file.filetxt= './m.txt'
#@classmethod
filew= Filetext.adding("i love my dad\nhappy")
print(file.__str__())
#text reading
for txt in file.text():
    print(txt)
#stat....
print(file.line_num('./m.txt'))









for t in filew.text():
    print(t)

# add

file1= Filetext('./ll.text')
file2= Filetext('./m.txt')
combined =file1+file2
print(combined.filetxt)
for line in combined.text():
    print(line)
#color
print(file2.colored_text())
print(file1.colored_text())

#more than 1 file

files=Filetext.more_than2("ll.text","m.txt","new.txt")
print(files.colored_text())

#child class

childclass = child('ll.text', author="chad")
print(childclass)
print(childclass.word_count())
print(childclass.colored_text())