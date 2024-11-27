def fast_factorize_product(product):
    """Efficiently factorize a product into byte values (0-255) using prime factorization."""
    factors = []
    
    # Check small prime numbers and their multiples (only up to 255)
    for i in range(2, 256):
        while product % i == 0:
            factors.append(i)
            product //= i
        if product == 1:
            break  # Early exit if we have fully factored the product

    # If product is still greater than 1 and less than 256, it should be a valid byte
    if 1 < product < 256:
        factors.append(product)
    
    return factors

def convert_to_base256(numbers):
    """Convert a list of numbers (byte values) to base 256 representation (hexadecimal)."""
    base256_representation = [format(num, 'x') for num in numbers]
    return ' '.join(base256_representation)

def map_number_to_char(n):
    """Convert a number (0-255) back to a corresponding character."""
    if 0 <= n <= 255:
        return chr(n)
    return ''

def main():
    # Step 1: Ask the user to enter the product of bytes
    product = int(input("Enter the product of byte values: "))#597
    
    # Step 2: Factorize the product into possible byte values (0-255)
    factors = fast_factorize_product(product)
    
    # Print Line 1: Input Product
    print(f"Input Product: {product}")
    
    # Print Line 2: Factors (decoded byte values)
    print(f"Factors (decoded byte values): {factors}")
    
    # Step 3: Calculate the product of the factors to confirm
    calculated_product = 1
    for byte in factors:
        calculated_product *= byte
    
    # Print Line 3: Product of Byte Values
    print(f"Product of Byte Values: {calculated_product}")
    
    # Step 4: Decode the byte values into a message (if possible)
    decoded_message = ''.join(map(map_number_to_char, factors))
    
    # Print Line 4: Decoded Message (characters)
    print(f"Decoded Message (from byte values): {decoded_message}")
    
    # Step 5: Convert the decoded byte values to base 256 (hexadecimal)
    base256_message = convert_to_base256(factors)
    
    # Print Line 5: Decoded Message in Base 256 (hexadecimal)
    print(f"Decoded Message in Base 256: {base256_message}")#3 c7
    
    # Final message display
    print("The decoded message based on the byte values is displayed above.")

if __name__ == "__main__":
    main()