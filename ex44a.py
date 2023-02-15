class parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(parent):
    pass

dad = parent()
son = Child()

dad.implicit()
son.implicit()
