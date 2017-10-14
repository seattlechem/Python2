class MathDojo(object):

    def __init__(self):
        self.total = 0

    def add(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for i in arg:
                    self.total += i
            else:
                self.total += arg
        return self                

    def subtract(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for i in arg:
                    self.total -= i
            else:
                self.total -= arg
        return self
    
    def result(self):
        print self.total
        return self

md = MathDojo()

md.add(2).add(2,5).subtract(3,2).result()

md.add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result()

