
# try:
#     f = open("test_file.txt")
  
# except FileNotFoundError:
#     print("sorry this file does not exist")
# except Exception:
#     print("sorry something went wrong")
    
    
# try:
#     f = open("test_file.txt")
  
#     if f.name == "currupt_file.txt":
#         raise Exception
    
# except Exception as e:
#     print("Error!")


# a = 5
# b = 0
# try:
#     print(a/b)
# except Exception:
#     print("Hey! you cannot divide a number by zero")
    
# try:
#   print(x)
# except:
#   print("An exception occurred")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") 