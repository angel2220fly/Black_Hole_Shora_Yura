def decode_binary_to_bytes(binary_input):
    """Decode a binary string (without spaces) into byte values (0-255)."""
    if len(binary_input) % 8 != 0:
        raise ValueError("Binary input must be a multiple of 8 bits.")
    
    # Split binary input into chunks of 8 bits
    byte_values = [int(binary_input[i:i+8], 2) for i in range(0, len(binary_input), 8)]
    return byte_values

def convert_to_base256(numbers):
    """Convert a list of byte values to hexadecimal (base-256) representation."""
    return ''.join(format(num, '02x') for num in numbers)

def convert_bytes_to_binary(numbers):
    """Convert byte values back to binary (8 bits each, without spaces)."""
    return ''.join(format(num, '08b') for num in numbers)

def calculate_product_binary(byte_values):
    """Calculate the binary representation of the product of byte values."""
    product = 1
    for byte in byte_values:
        product *= byte
    # Convert the product to binary
    return format(product, 'b')  # Binary without spaces

def main():
    try:
        # Step 1: Ask the user to enter a binary string without spaces
        binary_input = input("Enter the binary string (8 bits each, no spaces): ").strip()
        
        # Step 2: Decode the binary input into byte values
        byte_values = decode_binary_to_bytes(binary_input)
        
        # Step 3: Convert the byte values into base 256 (hexadecimal)
        base256_message = convert_to_base256(byte_values)
        
        # Step 4: Calculate the product of the byte values
        product = 1
        for byte in byte_values:
            product *= byte
        
        # Step 5: Calculate the binary representation of the product
        product_binary = product_binary=format(product,'01b')
        
        # Step 6: Convert byte values back to binary representation (8 bits each, no spaces)
        binary_message = convert_bytes_to_binary(byte_values)
        
        #Step 8 Conver to binary
        
        # Step 7: Display the results
        print(f"Input Binary: {binary_input}")
        print(f"Byte Values (decoded from binary): {byte_values}")
        print(f"Product of Byte Values: {product}")
        print(f"Product of Binary: {product_binary}")
        print(f"Decoded Message in Base 256: {base256_message}")
        print(f"Decoded Message binary each 8 bits without spaces: {binary_message}")
        print("The decoded message based on the byte values is displayed above.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()