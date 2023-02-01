from copy import deepcopy

class Polynomial:

    __slots__ = ['__coef']

    def __init__(self, *args):

        if args is None or len(args) == 0:      #just in case 
            self.__coef = [1] 

        elif len(args) == 1:

            if isinstance(args[0], list):         #suport for Polynomial([1,2,3,4])
                self.__coef = args[0]

            elif isinstance(args[0], Polynomial):   #suport for Polynomial(Polynomial)
                pass

        elif len(args) > 1:
            self.__coef = []
            for i in args: self.__coef.append(args)

    def __str__(self):
        print(self.__coef)

    def __call__(self):
        pass

    def __iadd__(self, other):
        pass

    def __add__(poly_1, poly_2):
        pass

    def __isub__(self, other):
        pass

    def __sub__(poly_1, poly_2):
        pass

    def __imul__(self, other):
        pass

    def __mul__(poly_1, poly_2):
        pass



    
