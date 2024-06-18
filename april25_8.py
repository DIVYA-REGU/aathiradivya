import re

def is_valid_float(s):
    try:
        float_num = float(s)
        return True
    except ValueError:
        return False

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        test_case = input().strip()
        if re.match(r'^[+-]?\d*\.\d+$', test_case):
            print(is_valid_float(test_case))
        else:
            print(False)

if __name__ == "__main__":
    main()
