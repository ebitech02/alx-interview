"""
solved pascal triangle task
while efficiently handled error cases
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle up to level n.
    Handles cases where n is not a valid integer using try-except.
    """
    try:
        # Ensure n is non-negative
        if n <= 0:
            return []

        # Initializing Pascal's Triangle with the first row
        triangle = [[1]]

        # Generate each row from 1 to n-1
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)

        return triangle

    except TypeError:
        # Catch any unexpected errors and return an empty list
        print(f"Not a valid integer")
        return []
