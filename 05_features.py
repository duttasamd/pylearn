# GENERATORS
# Generators are more efficient than lists.

#list comprehension

# this is a list object
squares_list = [x * x for x in range(10)]
print(squares_list)

#this is a generator
squares_gen = (x*x for x in range(10))
print(squares_gen)

for square in squares_gen:
    print(square)

# Performance enhancement demo
import m















print("=====================================================================")
# TEMPLATES

from string import Template

t = Template('x is $x')

x = 1

print(t.substitute({'x' : 1}))

print("=====================================================================")

results = []

results.append({'name': 'Ram', 'marks': 40})
results.append({'name': 'Shyam', 'marks': 90})
results.append({'name': 'Jadu', 'marks': 50})
results.append({'name': 'Modu', 'marks': 56})
results.append({'name': 'Vikram', 'marks': 63})

t = Template('$name got $marks')

for result in results :
    print(t.substitute(result))

# this is cleaner compared to :
#
# for result in results:
#     print("{} got {}".format(result['name'], result['marks']))

