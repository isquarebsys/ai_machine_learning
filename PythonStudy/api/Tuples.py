# Tuples are similar to lists, but they are immutable – which means they cannot be changed after creation

my_tuple = ("Michael", "Herman", 31, "Software Developer")

print(my_tuple[1])

# Adding tuples
first_tuple = (1, 2)
second_tuple = (3, 4)
third_tuple = first_tuple + second_tuple
print(third_tuple)

# Convert tuple to a list=>using list()
print(list(first_tuple))
