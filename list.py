def generate_coordinates(x, y, z, n):
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    return coordinates
def main():
    x = int(input("Enter the dimension along x-axis: "))
    y = int(input("Enter the dimension along y-axis: "))
    z = int(input("Enter the dimension along z-axis: "))
    n = int(input("Enter the value of n: "))
    coordinates = generate_coordinates(x, y, z, n)
    print("Coordinates with sum not equal to", n, ":")
    for coordinate in coordinates:
        print(coordinate)
if __name__ == "__main__":
    main()
