p = (4, 5)
x, y = p
print (x)
print (y)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print (name)
print (date)
#Unpacking actually works with any object that happens to be iterable, not just tuples or
# lists. This includes strings, files, iterators, and generators. For example:
print ("Unpacking actually works with any object that happens to be iterable, not just tuples or lists. This includes strings, files, iterators, and generators. For example:")
s='Hello'
a, b, c, d, e = s
print (d)
# Unpacking Elements from Iterables of Arbitrary Length
print ("Unpacking Elements from Iterables of Arbitrary Length")
# suppose you run a course and decide at the end of the semester that you’re going to drop the first
# and last homework grades, and only average the rest of them. If there are only four
# assignments, maybe you simply unpack all four, but what if there are 24? A star expression
# makes it easy:
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

sales_record = (10, 8, 7, 1, 9, 5, 10, 3)
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_avg)
print (current_qtr)


records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


