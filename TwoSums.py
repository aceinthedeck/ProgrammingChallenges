# given a list of numbers return whether any two sums to k. 
# Given [10,15,3,7] and k of 17 return true since 10+7 = 17

numbers=[10,15,3,7]
sum=134
sumFound=False
tempSum=0
for i in range(len(numbers)):
    j=i
    while (j+1) < len(numbers):
        tempSum=numbers[i]+numbers[j+1]
        if tempSum==sum:
            sumFound=True
            break
        else:
            tempSum=0
            j=j+1
if sumFound:
    print("True")
else:
    print("False")

