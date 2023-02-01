from copy import deepcopy

class Polynomial:

    __slots__ = ['__coef']

    def __init__(self, *arg):
        args = deepcopy(arg)
        if args is None or len(args) == 0:      #just in case 
            self.__coef = [1] 

        elif len(args) == 1:
            if isinstance(args[0], list):         #suport for Polynomial([1,2,3,4])
                self.__coef = args[0]
            elif isinstance(args[0], Polynomial):   #suport for Polynomial(Polynomial)
                self.__coef = args[0].get_coefficients() 
            if isinstance(args[0], int) or isinstance(args[0], float):  #suport for Polynomial(1)
                if args[0] != 0:
                    self.__coef = [args[0]]
                else: #suport for Polynomial(0) (that cannot be done!)
                    print("Can't create polynomial(0)! Polynomial(1) was created instead")
                    self.__coef = [1]

        elif len(args) > 1:
            self.__coef = []
            for i in args: self.__coef.append(i)

        while (self.__coef[0] == 0):   #we want deal with list like [1,2,3], and not [0,0,0,0,1,2,3]
            del self.__coef[0]

    def __str__(self):
        """Convention is like that:
            - 4*x^2 + 3*x - 10
            1*x + 1        etc"""

        a = ""

        #first n-2 terms:
        if self.deg >= 2: #leave two last elements because they ight have been 'problematic'
            for i in range(self.len - 2): 
                if self.__coef[i] != 0:
                    if self.__coef[i] < 0:
                        a += "- "
                    elif self.__coef[i] > 0:
                        a += "+ "
                    a += str(abs(self.__coef[i])) + "*x^" + str(self.deg-i) + " "

        #n-1 th term:
        if self.deg > 0: #printng single x term 
            j = self.deg-1
            if self.__coef[j] != 0:
                if self.__coef[j] < 0:
                        a += "- "
                elif self.__coef[j] > 0:
                    a += "+ "
                a += str(abs(self.__coef[j])) + "*x "

        #last term:
        if self.__coef[self.deg] != 0:
            if self.__coef[self.deg] < 0:
                        a += "- "
            elif self.__coef[self.deg] > 0:
                a += "+ "
            a += str(abs(self.__coef[self.deg]))

        #checking if fist term was positive. It's better to to it that way in my opinion (we would't have to mess up with indices and checking if coef[0] >0 all the time)
        if a[0] == "+":
            return a[2:]   #because to that stage string can begin with '+ ' and that is not elegant
        else:
            return a

    def __call__(self, value):
        eval = 0
        for i in range(self.len):
            eval += self.__coef[i] * (value**(self.deg-1))
        return eval

    def __iadd__(self, other):

        if other.len > self.len:
            temp = deepcopy(other.__coef)
            for i in range(self.len):
                temp[other.deg + i - self.deg] += self.__coef[i]
            self.__coef = temp

        else:
            for i in range(other.len):
                self.__coef[self.deg + i - other.deg] += other.__coef[i]
        return self

    def __add__(poly_1, poly_2):
        dummy = deepcopy(poly_1)
        dummy += poly_2
        return dummy

    def __isub__(self, other):
        b = [x * -1 for x in other.__coef]
        dummy = Polynomial(b)
        self += dummy
        return self

    def __sub__(poly_1, poly_2):
        dummy = deepcopy(poly_1)
        dummy -= poly_2
        return dummy

    def __imul__(self, other):
        dummy = self * other
        self = Polynomial(dummy)
        return self

    def __mul__(poly_1, poly_2):

        if isinstance(poly_1, float) or isinstance(poly_1, int):
            poly_1 = Polynomial(poly_1)
        if isinstance(poly_2, float) or isinstance(poly_2, int):
            poly_2 = Polynomial(poly_2)
        result = [0]*(poly_1.len+poly_2.len-1)

        for poly_1_power, poly_1_coef in enumerate(poly_1.__coef):
            for poly_2_power, poly_2_coef in enumerate(poly_2.__coef):
                result[poly_1_power+poly_2_power] += poly_1_coef * poly_2_coef
        return Polynomial(result)

    def get_coefficients(self):
        return deepcopy(self.__coef)

    @property 
    def coefficients(self):
        cf = deepcopy(self.__coef)
        cf.reverse()
        return cf

    @property 
    def len(self):
        return len(self.__coef)

    @property 
    def deg(self):
        return self.len - 1






    
