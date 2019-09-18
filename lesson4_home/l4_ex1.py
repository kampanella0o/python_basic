numbers = [1, -2, 16, -13, 20, 0, 3, 77]
print("Original list:", numbers)
numbers_two = []
for num in numbers:
    if num < 0:
        numbers_two.append(-1)
    elif num > 0:
        numbers_two.append(1)
    else:
        numbers_two.append(num)
print("Changed list", numbers_two)

numbers_positive = []
numbers_negative = []

for num in numbers:
    if num < 0:
        numbers_negative.append(num)
    elif num > 0:
        numbers_positive.append(num)
print("List of positives:", numbers_positive)
print("List of negatives:",numbers_negative)

print("Minimal of positives:", min(numbers_positive))
print("Maximal of positives:", max(numbers_positive))
print("Minimal of negatives:", min(numbers_negative))
print("Maximal of negatives:", max(numbers_negative))

for i in range(0, len(numbers)):
    if numbers[i] < 0:
        numbers[i] = -1
    elif numbers[i] > 0:
        numbers[i] = 1
    else:
        numbers[i] = 0
print("Changed original list:", numbers)