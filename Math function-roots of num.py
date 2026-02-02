#WAP TO FIND SQUAREROOT OR CUBE ROOT OF ANY NUMBER BY USER INPUT.
num= float(input("Enter a number: "))


print("\n 1. Squareroot of a number : \n 2. Cube ROOT of a number.")
ch = int(input("Enter your choice: "))

if ch == 1:
  sq = num**(1/2)
  print(f"{sq} is the square root of {num}")
elif ch == 2:
  cb = num**(1/3)
  print(f"{cb} is the cube root of {num}")
else:
  print("Invalid choice!")
