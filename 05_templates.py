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

