d = {1: "one", 2: "two"}
d.clear()
print('d =', d)


original = {1:'one', 2:'two'}
new = original.copy()

print('Orignal: ', original)
print('New: ', new)


# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.values())


d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)
person = {'name': 'Pearl', 'age': 20}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.items())
person = {'name': 'Pearl', 'age': 20, 'salary': 3500.0}
print(person.keys())

empty_dict = {}
print(empty_dict.keys())


# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)
person = {'name': 'Pearl', 'age': 20, 'salary': 3500.0}

# ('salary', 3500.0) is inserted at the last, so it is removed.
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)

# inserting a new element pair
person['profession'] = 'Ethical Hacker'

# now ('profession', 'Ethical Hacker') is the latest element
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)

person = {'name': 'Pearl', 'age': 20, 'salary': 3500.0}

# ('salary', 3500.0) is inserted at the last, so it is removed.
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)

# inserting a new element pair
person['profession'] = 'Ethical Hacker'

# now ('profession', 'Ethical Hacker') is the latest element
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)
