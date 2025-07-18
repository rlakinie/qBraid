# Basic concepts of classical computation: algorithms, bits and logic gates



#Representing Information using bits

# we import matplotlib which helps in showing the pictures. The "as plt" part means that we will call it plt when we invoke it later.
import matplotlib.pyplot as plt
# we import numpy to manipulate matrices
import numpy as np
# import the module copy to copy variables.
import copy
# assign the matrix of numbers that represent the image to a variable. 
import scipy.datasets
f = scipy.datasets.face()

# The following line shows the image in the notebook.
plt.imshow(f)
f_shape = np.shape(f)
#The following line shows the matrix of numbers that represents the picture.
#Note the numbers are between 0 and 255. These represent different colors
print(f)

# creating a copy of the variable, so we can play with it
f1 = copy.deepcopy(f)
# make a bunch of entries in the matrix zero.
f1[:,1:300,:]=np.zeros([f_shape[0],299,f_shape[2]])
plt.imshow(f1)

# As we discussed above, the numbers represent the colors of pixels. So, let's just play
# with these numbers and add 50 to each number in the matrix
x_filter = 50*np.ones(np.shape(f),dtype='uint8')
# type(x_filter)
f1 = f+x_filter
#plt.show()
plt.imshow(f1)

# Now we subtract 50 from each number in the matrix and see what happens.
f2 = f-x_filter
plt.show()
plt.imshow(f2)




# Logic gate problems
# Problem 1. Write Python code that implements the logic gates AND, and OR, following the template below.


inputs = [(0,0), (0,1), (1,0), (1,1)]

#x = 1
#y = 1

## YOUR CODE HERE ##
#AND 
print("AND GATE")
for x, y in inputs:
  if x == 1 and y == 1:
    z = 1
  else: 
    z = 0
  
  print(f"x = {x}, y = {y} -> z = {z}")
###

#OR
print("\nOR GATE")
for x, y in inputs:
  if x == 1 or y == 1:
    z = 1
  else:
    z = 0
  
  print(f"x = {x}, y = {y} -> z = {z}")
#print(z)



# Problem 2. Write/draw a circuit, consisting of only AND and NOT gates, which implements the OR gate.
# I realized I have completely forgotten about De Morgan's Law
print("OR using only AND and NOT")
for x, y in inputs:
    z = not (not x and not y)
    print(f"x = {x}, y = {y} -> z = {int(z)}")  # int(z) to print 0 or 1
