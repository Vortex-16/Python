# Box in a box pattern (like a photo frame)

def photo_frame(n):
    if n < 3:
        print("Size should be at least 3.")
        return
    for i in range(n):
        for j in range(n):
            # For n=3, just print a single box
            if n == 3:
                print('*', end=' ')
            # For n>3, print outer and inner borders
            elif i < 2 or i >= n-2 or j < 2 or j >= n-2:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# Example usage
photo_frame(3)
print()
photo_frame(7)