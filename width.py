thickness = int(input())

# Top cone
for i in range(thickness):
    print((' ' * (thickness - i - 1) + 'H' * (2 * i + 1)).rstrip())

# Top pillars
for i in range(thickness + 1):
    print(('H' * thickness).rjust(thickness + i) + ('H' * thickness).ljust(thickness * 5 - i))

# Middle part
for i in range((thickness + 1) // 2):
    print(('H' * thickness * 5).center(thickness * 6))

# Bottom pillars
for i in range(thickness + 1):
    print(('H' * thickness).rjust(thickness + i) + ('H' * thickness).ljust(thickness * 5 - i))

# Bottom cone
for i in range(thickness):
    print((' ' * i + 'H' * (2 * (thickness - i - 1) + 1)).rstrip())
