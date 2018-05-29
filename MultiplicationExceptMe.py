#Problem 2
# Given an array of integers return a new array such taht each element at index i of the new array is the product of all the numbers in the original array except the one at i
# Ex - if the input is [1,2,3,4,5] the expect output would be [120,60,40,30,24]
# follow up do it without division.

def multiplication(list):
    product=1
    newList=[]
    for num in list:
        product=product*num
    for num in list:
        newList.append(product/num)
    return newList

list=[1,2,3,4,5]
print(multiplication(list))
