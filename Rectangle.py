#Roquia Ibrahim
#CIS261
#Rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
def calculate_perimeter(self):
    return 2 * (self.height + self width)

def calculate_area(self):
    return self.height * self.width

def print_rectangle(self):
    print(f"Height: {self.height}")
    print(f"Width: {self.width}")
    print(f"Perimeter: {self.calculate_perimeter()}")
    print(f"Area: {self.calculate_area()}")
    
    for i in range(self.height):
        if i == 0 or i == self.height - 1:
            print('*' * self.width)
        else:
            print('*' + ' ' * (self.width - 2) + '*')
            
def main():
    while True:
        print("\nRectangle Calculator")
        
        height = int(input("Enter height: "))
        width = int(input("Enter width: "))
        
        rect = Rectangle(height, width)
        
        rect.print_rectangle()
        
        cont = input("Continue? (y/n): ").strip().lower()
        if cont != 'y':
            break
        
if __name__ == "__main__":
    main()
