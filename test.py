from polynomial import Polynomial

w = Polynomial(0,-2,0, -3,4,-5,0)
print(w.coefficients)
print(w)
print(w(2))

w3 = Polynomial(0,0,0,0,0,0,1,2,3)
print(w3.coefficients)
print(w3)
print(w3.deg)



w1 = Polynomial(1,2,3,4,5,6)
w2 = Polynomial(-5, -6)
print(w1)
w1 += w2
print(w1)

w2 = Polynomial(1,2,3,4,5,6)
w1 = Polynomial(-5, -6)
print(w1)
w1 += w2
print(w1)

a = [1,2,3,4]
print(a)
b = [x * -1 for x in a]
print(b)


w2 = Polynomial(2,2,2,2)
w1 = Polynomial(1,1,1,1)
w3 = w1 * w2 
print(w3)

w2 = Polynomial(2,2,2,2)
w1 = Polynomial(1,1,1,1)

w1 *= w2 
print(w1)

a=2
print(w1*a)
print(a)

w1 = Polynomial([1, 2, 3, 5])      # 1*x^3 + 2*x^2 + 3*x + 5
w2 = Polynomial(5, 2, 1)           #         5*x^2 + 2*x + 1
w3 = Polynomial(w1)
print("**************")
print(w1)
print(w1.coefficients)
a = [1,2,3,4]
print(a)
print(a.reverse())


