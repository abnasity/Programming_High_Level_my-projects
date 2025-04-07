
# try:
#     f = open("test_file.txt")
  
# except FileNotFoundError:
#     print("sorry this file does not exist")
# except Exception:
#     print("sorry something went wrong")
    
    
try:
    f = open("test_file.txt")
  
    if f.name == "currupt_file.txt":
        raise Exception
    
except Exception as e:
    print("Error!")