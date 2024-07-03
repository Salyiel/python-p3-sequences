def print_fibonacci(length):
    """
    Generate and print the Fibonacci sequence up to the specified length.

    Parameters:
    - length (int): Length of the Fibonacci sequence to generate.
    """
    if length <= 0:
        # Print an empty list with newline if length is 0 or negative
        print("[]")
        return
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # List to store the Fibonacci sequence
    fib_sequence = []
    
    # Generate Fibonacci sequence
    for _ in range(length):
        fib_sequence.append(a)
        a, b = b, a + b
    
    # Print the Fibonacci sequence
    print(fib_sequence)
