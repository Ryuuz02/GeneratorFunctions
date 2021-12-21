"""
A generator function is a function that yields multiple values
yielding is basically returning, but it effectively freezes the function at that point, when the function is next needed
it will continue from there
def next_num_gen():
    yield 1
    yield 2
    yield 3


When you assign any variable equal to a generator function, that variable is a generator object
num_gen = next_num_gen()

generator objects have the attribute __next__(), which yields the next value in their generator function
print(num_gen.__next__())
^ returns 1
print(num_gen.__next__())
^ returns 2
print(num_gen.__next__())
^ returns 3
"""

"""
You can use a while statement to infintely generate numbers
def long_num_gen():
    i = 1
    while True:
        yield i
        i += 1


gen = long_num_gen()

Will print off 1-10
for i in range(0, 10):
    print(gen.__next__())
"""


"""
Can use it with equations to get as many values following a pattern as you would need
def square_gen():
    i = 1
    while True:
        yield i ** 2
        i += 1


gen = square_gen()

Prints out the first 10 square numbers
for i in range(0, 10):
    print(gen.__next__())
"""
