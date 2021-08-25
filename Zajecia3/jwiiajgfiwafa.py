# resultLambda1 = lambda x, y: x + y
# print('Wynik wywołania funkcji lambda:',resultLambda1(3,5))
#
# name ='Ala'
# resultLambda2 = lambda oneWord: oneWord.upper()
# print(resultLambda2(name))
#
# def power(number):
#     result = number**2
#     return(result)
#
# listNumber = [2, 10, 15, 100, -5] # równoważne: [double(n) for n in listNumber]
# resultMap = map(power, listNumber)
# print(list(resultMap)) # map(functionName, lista)

# listWord = ['dnA','RnA']
# print(listWord)
# upperLetter = lambda oneWord: oneWord.upper()
# resultLambdaZip = map(upperLetter, listWord)
# powyższa linia równoważna: map(lambda oneWord: # oneWord.upper(), listWord)
# print('Wynik wywołania funkcji map:',list(resultLambdaZip))

# list1 = [1,3,5]
# list2 = [2,4,6]
# resultZip = zip(list1, list2)
# print(list(resultZip))

# import functools, operator
#
#
# resultLambda1 = lambda x, y: x + y
# list1 = [1,2,3,4]
# resultReduce1 = functools.reduce(resultLambda1, list1,0)
# print(resultReduce1)

# import functools, operator
# list2 = [1,2,3,4]
# resultReduce2 = functools.reduce(operator.mul, list2, 1)
# print(resultReduce2)

# list1 = [1,2,3,4]
# def even(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False
#
# resultFilter = filter(even, list1)
# print(list(resultFilter))

from trans import trans


seq='ATCGAATGGCGCAAAACGCG'
print(seq)
print('Ilość par zasad w łańcuchu:',len(seq))
print('pierwsza zasada',seq[0])
print('ostatnia zasada',seq[len(seq)-1])
print('srodkowa zasada')
print('liczebność A:',seq.count('A'))
print('liczebność T:',seq.count('T'))
print('liczebność C:',seq.count('C'))
print('liczebność G:',seq.count('G'))
print('zawartość % alaniny:',seq.count('A')/len(seq)*100)
print('zawartość % cytozyny:',seq.count('C')/len(seq)*100)
listadna=list(seq)
listadna.remove('G')
print('dna bez guaniny',listadna)
listadna.reverse()
print('odwrócona lista',listadna)
rna=trans(seq)
listarna=list(rna)
listarna.reverse()
print('odwrócone rna:',listarna)

