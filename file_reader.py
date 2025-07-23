from color import color_
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
    def more_than2(*files,new_one="3e.txt"):
         with open(new_one,'w') as l:
            for line in files:
                with open(line,'r') as k:
                    l.write(k.read()+ '\n')
         return Filetext(new_one)
   
