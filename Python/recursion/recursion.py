
#A recursion is a defined function that can call itself
def fact(n):
    if n==0:
     return 1

    return n * fact(n-1)
result = fact(10)
print(result)

 #General factorial rule 
 
 #n! = nx(n-1)!
 #5!=5*4*3*2*1
 #5! can be written as 5=5*4!
 
 # Temperature 🌡
# Codédex

# temp_f = 56
# temp_c = (temp_f - 32) / 1.8

# print(temp_c)