# Library of Numpy 
import numpy as np 
import sys
import ast
#Variables
# Enter the points as arrays, Example is [[n1,n2],[n3,n4]]
print("Enter the points as arrays, example is [[n1,n2],[n3,n4]]...")
print("The program only accepts a Polynomial until 10th degree")
#Display user input 
array = input("Enter arrays: ") 
#Convert the string inputed as list
arraylist = ast.literal_eval(array)
#Convert the list into an array
a = np.asarray(arraylist) 
# Length of n inputs 
arraylength = len(a) 
# Locates values of x
x = a[0:arraylength,0] 
# Locates the values of y
y = a[0:arraylength,1]
#Set another variable where to append the values 
poly1 = []
poly2 = []
error=[]
leastnorm=[]
def Polynomial():
    for n in range(1,arraylength):
        if n <= 10:
            # Returns the coefficients for a polynomial p(x) of degree n that is a best fit 
            p1 = np.polyfit(x,y,n)
            poly1.append(p1)
            # Evaluates the polynomial at values of x.
            p2 = np.polyval(p1,x) 
            poly2.append(p2)
            #Poly 1D returns the coeeficients as polynomials
            coefficients = np.poly1d(p2)
            #Find the norm using the command
            norm = np.linalg.norm(y-p2)
            error.append(norm)
            #Find the least norm error 
            lne = np.min(norm) 
            leastnorm.append(lne)
        #Condition that the degree exceeded 
        elif n > 10:
            sys.exit("Notice: nth degree exceeded, the program only accepts 1st to 10th degree")
    print("Polynomial Coefficients are:",p2)
    print("Equation form is:",coefficients)
    print("The least-norm error vector(e(x)) is:",lne,)
Polynomial()

