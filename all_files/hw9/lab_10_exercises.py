from functools import reduce

####
Take a list of numbers, square each element

my_nums = [1, 2, 3, 4, 5]

### Imperatively

squared_nums = []
for num in my_nums:
    squared_nums.append(num * num)

### Functionally

squared_nums = map(lambda x: x * x, range(1, 6))

### Functionally convert this list to a list of strings, not ints

squared_strings = map(str, squared_nums)

### Functionally flip the digits on all of the strings

squared_strings_reversed = map(reversed, squared_strings)

### Take your list of squared numbers and make a list of only the even ones

### Imperatively
even_squared_nums = []
for squared_num in squared_nums:
    if squared_num % 2 == 0:
        even_squared_nums.append(squared_num)

### Functionally
even_squared_nums = filter(lambda x: x % 2 == 0, squared_nums)

### Combine the answers from the first two to create a list of even squares in one line

even_squared_nums = filter(lambda x: x % 2 == 0,
                            map(lambda x: x * x, range(1, 10)))

### Sum the list of even squares

### Imperatively

sum = 0
for esn in even_squared_nums:
    sum += esn

### Functionally

sum = reduce(lambda a, x: a + x, even_squared_nums)

### Functionally find the length of the list of even squares

count = reduce(lambda a, x: a + 1, even_squared_nums)

### Consider the following list of dictionaries (looks like JSON)
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

### What is the total height of those with heights provided


### Imperatively
total_height = 0
for person in people:
    if 'height' in person:
        total_height += person['height']

### Functionally

total_height = reduce(lambda a, x: a + x,
                      map(lambda x: x.get('height', 0), people))

# With a comprehension
total_height = sum([x.get('height', 0) for x in people])

### How would we do this if this were a list of tuples instead?

people_tuples = [('Mary', 160), ('Isla', 80), ('Sam',)]

total_height = reduce(lambda a, x: a + x,
                      map(lambda x: x[1] if len(x) > 1 else 0, people_tuples))