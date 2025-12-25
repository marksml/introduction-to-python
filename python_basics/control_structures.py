#iterating over a set of names and printing a greeting for each name
print("---> iterating over a set of names and printing a greeting for each name")
names = {"Alice", "Bob", "Charlie", "Diana"}
#this will print each name in the set with a greeting but the order of the processed names is random as a set is not sorted
for name in names:
    print("Hello " + name + ".")

#iterating and using a conditional printing
print("---> iterating over names and printing by using a condition")
names = ["Alice", "Bob", "Charlie", "Diana", "Ellen"]
#this will print a special greeting for Alice and a different message for others
for name in names:
    print(f"Welcome back, {name}!")    

# building a list from the names list from only the names that start with a vowel
print("---> building a list from the names list from only the names that start with a vowel")
names = ["Alice", "Bob", "Charlie", "Diana", "Ellen", "Oscar", "Uma"]
vowel_names = []
for name in names:
    if name[0].lower() in 'aeiou':
        vowel_names.append(name)    
    
print("Names that start with a vowel: " + ", ".join(vowel_names))

# sum up floats in a list
print("---> summing up floats in a list")
float_numbers = [1.5, 2.3, 3.7, 4.0, 5.2]
total_sum = 0.0
for number in float_numbers:
    total_sum = total_sum + number

print(f"The total sum of the float numbers is: {total_sum}")

#now use the python function sum to do the same
print("---> summing up floats in a list using the built-in sum function")
sum_using_function = sum(float_numbers)
print(f"The total sum of the float numbers using sum(list) is: {sum_using_function}")


