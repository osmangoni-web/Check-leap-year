# using a function to identified the year
 
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("This year is a leap Year");  
  # Else it is not a leap year  
  else:  
    print ("This year is not a leap Year")  
# input year from user  
Year = int(input("Enter the number: "))  
# Printing result  
CheckLeap(Year)