#WAP TO PRINT AND CHECK ARMSTRONG NUMBER.
num = int(input("Enter a number: "))
sum = 0
order = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(f"{num} is an Armstrong number.")
elif(num != sum):
    print(f"{num} is not an Armstrong number.")
else:
    print(f"{num} is not a valid Input!")
