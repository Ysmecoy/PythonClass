list_3 = [1, 3, 5, 7, 9]
list_4 = []
for value in reversed(list_3): list_4.append(value)
print(list_4)

list = []
list_5 = [1, 2, 3, 4, 5]
'''
for value1 in list_5:
    value1 *= 2
    list.append(value1)
    
print(list)
'''

i = 0

while i < len(list_5):
    list_5[i] *= 2
    i+=1
print(list_5)


list_9 = [-2, 3, 3, 5, 8, 11]
for (index, value) in enumerate(list_9):
    
    print(' %d, %d.' % (index, value))
    
s_6 = '(15 + 2) * 3 - (18 + 6)'
''' Change 18 to 108. '''
tokens = s_6.split()
tokens[6] = '(108'
s_6 = ' '.join(tokens)
print(s_6)
 
    

