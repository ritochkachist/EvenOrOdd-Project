# Margarita Chistiakova  
# 2/13/2023 
# Even and odd program  

#Function definition here:
def evenOdd(number):
  if number % 2 == 0: 
    print("The number you entered is even.")
  elif number % 2 != 0:
    print("The number you entered is odd.")
    return number
  
#Main program code here:
print("Hello! Please enter a number so I can detect if it is even or odd ")
number = int(input())

#I am calling my function here
#result = 
evenOdd(number)
#print(result)


