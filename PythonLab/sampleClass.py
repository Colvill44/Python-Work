#Define a sample class, which have a class parameter and have a same instance parameter. 
class Sample(str):
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return self.arg
    def __repr__(self):
        return self.arg