import matplotlib.pyplot as plt
plt.title("Bresenham Algorithm", size='14')
plt.xlabel("X Axis", size='12')
plt.ylabel("Y Axis", size='12')
plt.grid(color='#0d0d0d')


def bresenham(x1,y1,x2,y2):
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    print(f"x = {x}, y = {y}")
    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        print(f"x = {x}, y = {y}")
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates, color='#a020f0', marker='o', 
             linestyle='solid', linewidth='2', markersize='12')
    plt.show()


def main():
    x1 = int(input("Enter the Starting point of x: "))
    y1 = int(input("Enter the Starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    bresenham(x1, y1, x2, y2)

if __name__ == "__main__":
    main()