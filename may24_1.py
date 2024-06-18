from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text")
print(Back.YELLOW + "This text has a yellow background")
print(Style.BRIGHT + "This is bright text")
