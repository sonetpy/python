
records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *sonu in records:
    if tag == 'foo':
        do_foo(*sonu)
    elif tag == 'bar':
        do_bar(*sonu)

"""
Here's how the code processes the records list:

For the first record ('foo', 1, 2):

tag is 'foo'
sonu is [1, 2]
The do_foo(1, 2) function is called, printing 'foo 1 2'.
For the second record ('bar', 'hello'):

tag is 'bar'
sonu is ['hello']
The do_bar('hello') function is called, printing 'bar hello'.
For the third record ('foo', 3, 4):

tag is 'foo'
sonu is [3, 4]
The do_foo(3, 4) function is called, printing 'foo 3 4'.
"""