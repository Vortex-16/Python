# Box in a box pattern

def box_in_box(n):
    for i in range(n):
        for j in range(n):
            # Print '*' for border of outer or inner box
            if i == 0 or i == n-1 or j == 0 or j == n-1 or \
               (i == 1 or i == n-2 or j == 1 or j == n-2):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# Example usage
box_in_box(7)