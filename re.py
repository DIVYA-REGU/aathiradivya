import re
def find_substring_indices(main_string, substring):
    pattern = re.compile(r'(?=(' + re.escape(substring) + '))')
    matches = pattern.finditer(main_string)
    indices = [(match.start(1), match.end(1) - 1) for match in matches]
    return indices if indices else [(-1, -1)]
main_string = input().strip()
substring = input().strip()
indices = find_substring_indices(main_string, substring)
for start, end in indices:
    print(f'({start}, {end})')
