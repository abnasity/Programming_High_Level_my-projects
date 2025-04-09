
#***Characterestics of Sequence Objects/Data Types
#1. Ordered - This means that the elements have a defined order and you can access them using an index
#2. Indexed - This means that you can access the elements using an index
#3. Mutable - This means that you can change the elements of the sequence
#4. Allow Duplicates - This means that you can have multiple elements with the same value
#5. Iterable - This means that you can repeat a process or a set of steps foreach element in the sequence
#6. Can Be Nested - This means that you can have a sequence inside a sequence
#7. Can be sliced - This means that you can access a rane of elements in the sequence
#8. Can be concatenated - This means that you can join two or more sequences together
#9. Can be reapeted - This means that you can repeat the elements in the sequence
#10.Can be converted to other data types - This ,eans that you can convert the sequence to other data types i.e set, Dictionaries etc


#***The following items can be ordered*****
#1. LIsts
#2. Tuples
#3. Strings



#****The following items can be indexed *****

#1. Lists
#2. Tuples
#3. Strings



#******THe following items can be muted/changed****
#1. Lists
#2. Dictionaries
#3. Sets


#****The following items can be nested*****
#1. Dictionaries - Dictionaries with lists
#2. Lists - Lists with dictionaries




#******The following items can be sliced*****

str	✅ Yes	"Python"[0:3] → 'Pyt'
list	✅ Yes	[1, 2, 3, 4][1:3] → [2, 3]
tuple	✅ Yes	(10, 20, 30)[0:2] → (10, 20)
range	✅ Yes	list(range(10))[2:7] → [2, 3, 4, 5, 6]



#****The following items can be concatenated*****
str	✅ Yes	"Hello" + "World" → "HelloWorld"
list	✅ Yes	[1, 2] + [3, 4] → [1, 2, 3, 4]
tuple	✅ Yes	(1, 2) + (3, 4) → (1, 2, 3, 4)



#****The following items can be repeated*****
str	✅ Yes	"ab" * 3 → "ababab"
list	✅ Yes	[1] * 4 → [1, 1, 1, 1]
tuple	✅ Yes	(2, 3) * 2 → (2, 3, 2, 3)


#****The following data types can be converted to other data types/Type casting*****

rom → To	✅ Can Convert?	Example
int → float	✅ Yes	float(5) → 5.0
float → int	✅ Yes	int(3.9) → 3
int → str	✅ Yes	str(100) → "100"
str → int	✅ Yes (if numeric)	int("42") → 42
list ↔ tuple	✅ Yes	tuple([1,2]) → (1,2)
list ↔ set	✅ Yes	set([1,1,2]) → {1,2}
str → list	✅ Yes	list("abc") → ['a', 'b', 'c']
dict → list	✅ (keys only)	list({"a":1, "b":2}) → ['a', 'b']
list → dict	✅ If list of pairs	dict([("a",1), ("b",2)]) → {'a':1, 'b':2}rom → To	✅ Can Convert?	Example
int → float	✅ Yes	float(5) → 5.0
float → int	✅ Yes	int(3.9) → 3
int → str	✅ Yes	str(100) → "100"
str → int	✅ Yes (if numeric)	int("42") → 42
list ↔ tuple	✅ Yes	tuple([1,2]) → (1,2)
list ↔ set	✅ Yes	set([1,1,2]) → {1,2}
str → list	✅ Yes	list("abc") → ['a', 'b', 'c']
dict → list	✅ (keys only)	list({"a":1, "b":2}) → ['a', 'b']
list → dict	✅ If list of pairs	dict([("a",1), ("b",2)]) → {'a':1, 'b':2}