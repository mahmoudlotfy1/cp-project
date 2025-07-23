
def color_(color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
        }
    def decorator(func):
        def wrapper(*arges,**kwargs):
            result= func(*arges,**kwargs)
            return f"{colors.get(color, colors['reset'])}{result}{colors['reset']}"
        return wrapper
    return decorator




class Filetext:
    def __init__(self,name):
        self.name= name
    @property
    def filetxt(self):
       return self.name
    @filetxt.setter
    def filetxt(self, new_name):
        self.name= new_name
   
    def text (self):
        #understand
        with open(self.name,'r') as k:
            for i in k:
                yield i.strip()
                # strip
    @staticmethod
    
    def line_num(name):
        with open(name,'r') as k:
           return len(k.readlines())
    @classmethod
    def adding(cls,name,):
         #good understand
         with open('./m.txt','w') as k:
             k.write( name ) 
         return cls('./m.txt')
    def __str__(self):
        #week point 
        return f"Filetext object with file: {self.name}"
    def __add__(self, other):
        if not isinstance(other,Filetext):
            return NotImplemented
        f1= '\n'.join(self.text())
        f2= '\n'.join(other.text())
        f_1sumf_2= f1 + '\n'+ f2
        new_filename= "new.txt"
        with open(new_filename, "w") as f:
            f.write(f_1sumf_2)
        return Filetext(new_filename)
    @color_("blue")
    def colored_text(self):
        return '\n'.join(self.text())
    
    @staticmethod
    def more_than2(*files,new_one="3_or_more.txt"):
        with open(new_one,'w') as l:
            for line in files:
                with open(line,'r') as k:
                    l.write(k.read()+ '\n')
        return Filetext(new_one)
    @color_("blue")
    def colored_text(self):
        return '\n'.join(self.text())


    



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

class child(Filetext):
    def __init__(self, name,  author=None):
        super().__init__(name)
        self.author= author
    def __str__(self):
        base = super().__str__()
        if self.author:
            return f'{base}, Author: {self.author}'
        return base
    def word_count(self):
        with open(self.name,'r') as s:
            text= s.read()
            words= text.split()

            return len(words)
        








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