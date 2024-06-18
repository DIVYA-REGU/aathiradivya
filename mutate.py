def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    mutated_string = ''.join(string_list)
    return mutated_string
s = input().strip()
position, character = input().strip().split()
position = int(position)
result = mutate_string(s, position, character)
print(result)
