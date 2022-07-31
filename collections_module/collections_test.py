import collections

print('\nNAMEDTUPLE\n')
# named tuple
# you can create tuple with named elements
Fruit = collections.namedtuple('Fruits', ['name', 'color', 'eatable'])
banana_tuple = Fruit('banana', 'yellow', 'yes')
print(banana_tuple)
print(banana_tuple.name)
print(banana_tuple.color)
print(banana_tuple.eatable)

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
marks_count = {}
for mark in student_marks:
    if mark in marks_count:
        marks_count[mark] += 1
    else:
        marks_count[mark] = 1

print(marks_count)

# Counter - counts number of same elements
marks_count = collections.Counter(student_marks)
print(marks_count)
# show most common elements
print(marks_count.most_common(1))
# two most common elements
print(marks_count.most_common(2))

print('\nCOUNTER\n')
# Counter can subtract one list from another list
l1 = collections.Counter(a=4, b=2, c=0, d=-1)
l2 = collections.Counter(a=2, b=1, c=3, d=3)
l1.subtract(l2)
print(l1)

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}
for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)
print(grouped_words)

# You can group of words by first character with defaultdict
grouped_words = collections.defaultdict(list)
for word in words:
    char = word[0]
    grouped_words[char].append(word)
print(grouped_words)

print('\nDEQUE\n')
# deque - faster than classic list in python
d = collections.deque()
d.append('Last')
d.appendleft('First')
d.insert(1, 'Middle')
print(d)

print(d.pop())  # last
print(d.popleft())  # first
print(d)

# you can adjust maximum length of list by changing "maxlen" parameter
d = collections.deque(maxlen=5)
for i in range(10):
    d.append(i)
print(d)  # 5, 6, 7, 8, 9
