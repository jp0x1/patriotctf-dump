import re

def extract_binary_values(vcd_file):
    # Regex patterns to match the signal value changes for dout and din
    binary_pattern = re.compile(r'b([01]+) ["#]')

    # Initialize lists to store the binary values
    dout_values = []
    din_values = []

    # Read the VCD file line by line
    with open(vcd_file, 'r') as file:
        for line in file:
            # Match binary values for dout or din
            match = binary_pattern.search(line)
            if match:
                binary_value = match.group(1)
                # Check which signal (dout or din) the value belongs to
                if '"' in line:
                    dout_values.append(binary_value)
                elif '#' in line:
                    din_values.append(binary_value)

    return dout_values, din_values

def binary_to_ascii(binary_values):
    # Convert each binary value to its ASCII representation
    ascii_string = ''.join([chr(int(b, 2)) for b in binary_values])
    return ascii_string

def main():
    # Path to the VCD file
    vcd_file = 'flag.vcd'
    
    # Extract binary values from the VCD file
    dout_values, din_values = extract_binary_values(vcd_file)
    
    # Convert the binary values to ASCII
    dout_ascii = binary_to_ascii(dout_values)
    din_ascii = binary_to_ascii(din_values)
    
    # Print the results
    print("Dout ASCII:", dout_ascii)
    print("Din ASCII:", din_ascii)

if __name__ == '__main__':
    main()
