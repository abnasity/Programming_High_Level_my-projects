#For loop
#for loop is used for iterating over a sequence that is either a list, a tuple, a dictionary, a set, or a string.
# USE CASES:


#***apple and banana will be printed because the loop will break when it gets to cherry
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break


# ***only apple will be printed because the loop will break when it gets to banana
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)
  
  
#RANGE FUNCTION
# For loop with range function
# for x in range(6):
#      print(x)

# for x in range(2, 6):
#   print(x)
  
#Increment the sequence with 3 (default is 1):
# for x in range(2, 30, 3):
#   print(x)


  
# x = ["fanta", "orage", "cocacola"]
# for x in x:

#   print (x)

#Create a program that looks like a car game

command = ""
while command != "quit":
    command = input("> ")
    if command == "start":
      if "started":
          print("car already started")
    else:
        if "started" == True:
         print("start the car.....")
    
        
         
        
        elif command == "stop":
            if  "stop":
               print("car already stopped")
            if "stop" == True:
               print("stop the car.....")
        
         
        
            
        elif command == "help":
              print("""
              start - start the car
              stop - stop the car
              quit - quits
              """)
    # elif command == "quit":
    #     break
    # else:
    #     # print("park the car")
#