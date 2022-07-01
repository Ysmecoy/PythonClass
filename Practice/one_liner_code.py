# to convert input or string(num) or data separated by space in a list
'''
li = list(map(int, input().split()))
'''
# function that return the square of a number
'''    
def sqr(x):
    return x*x 
'''
# list comprehension. to list of even numbers till 20

# normal way
evenNumbers = []
for x in range(20):
    if x % 2 == 0:
        evenNumbers.append(x)

print(evenNumbers)

# The pythonic way

evenNumbers = [x for x in range(20) if x % 2 == 0]
print(evenNumbers)
      


        
        
