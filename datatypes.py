#Setting the Data Type

#string
a = "hello world"
print(a)
print(type(a))

#integer
b = 42
print(b)
print(type(b))

#float
c = 3.14
print(c)
print(type(c))

#boolean
d = True
print(d)
print(type(d))

#complex
e = 1j
print(e)
print(type(e))

#list
f = [1, 2, 3, "four", "five"]
print(f)
print(type(f))

#tuple
g = (1, 2, 3, "four", "five")
print(g)
print(type(g))

#dictionary
h = {"name": "Alice", "age": 30, "city": "New York"}
print(h)
print(type(h))

#set
i = {1, 2, 3, "four", "five"}
print(i)
print(type(i))

#range
j = range(1, 10)
print(j)
print(type(j))
print(list(j))  # Convert range to list for display

#bytes
k = b"hello"
print(k)
print(type(k))

#bytearray
l = bytearray(b"hello")
print(l)
print(type(l))

#memoryview
m = memoryview(b"hello")
print(m)
print(type(m))

#NoneType
n = None
print(n)
print(type(n))

#Setting the Specific Data Type

#string
a = str("hello world")
print(a)
print(type(a))

#integer
b = int(42)
print(b)
print(type(b))

#float
c = float(3.14)
print(c)
print(type(c))

#boolean
d = bool(True)
print(d)
print(type(d))

#complex
e = complex(1, 2)
print(e)
print(type(e))

#list
f = list([1, 2, 3, "four", "five"])
print(f)
print(type(f))

#tuple
g = tuple((1, 2, 3, "four", "five"))
print(g)
print(type(g))

#dictionary
h = dict(name="Alice", age=30, city="New York")
print(h)
print(type(h))

#set
i = set([1, 2, 3, "four", "five"])
print(i)
print(type(i))

#range
j = range(1, 10)
print(j)
print(type(j))
print(list(j))  # Convert range to list for display

#bytes
k = bytes("hello", "utf-8")
print(k)
print(type(k))

#bytearray
l = bytearray("hello", "utf-8")
print(l)
print(type(l))

#memoryview
m = memoryview(bytes("hello", "utf-8"))
print(m)
print(type(m))

#NoneType
n = None
print(n)
print(type(n))