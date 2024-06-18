def mutate_string(string, i, c):
    string_list = list(string)
    string_list[i] = c
    mutated_string = ''.join(string_list)
    return mutated_string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
