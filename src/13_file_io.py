"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""


with open('./foo.txt', 'r') as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed


# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file


with open('./foo.txt', 'r') as e:
    read_data = e.read()
    print(read_data)
e.closed
# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
with open('./bar.txt', 'w') as t:
    write_data = t.write(' hello \n I am \n Brandon')
t.closed

with open('./bar.txt', 'r') as u:
    read_data = u.read()
    print(read_data)
u.closed
# YOUR CODE HERE
