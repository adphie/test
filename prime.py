while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
      break
    if 0 < n < 2 or n < 0:
        print("Please enter a number greater than or equal to 2.")
        continue
    y = 0
    for i in range(1,n+1,1):
      if n % i == 0:
        y+=1
    if y == 2:
      print(n, "is a prime number")
    else:
     print(n, "is not a prime number")
print("END OF PROGRAM")