from file_reader import Filetext

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
        