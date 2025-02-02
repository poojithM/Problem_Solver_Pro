```python
def print_formatted(number):
    width = len(bin(number)) - 2  # Calculate width based on the binary representation of the number
    formatted_output = []
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        formatted_output.append(f'{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}')
    return '\n'.join(formatted_output)

# Testing the function with defined test cases
test_cases = [17, 1, 8, 16]
results = {n: print_formatted(n) for n in test_cases}

# Print the results for each test case
for n, result in results.items():
    print(f"Test case for number {n}:\n{result}\n")
```