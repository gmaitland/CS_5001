"""
    Garfield Maitland
    CS 5001
    10/02/2023
    Homework 4 - runlength_decoder.py
"""
import hw4data  # Assuming hw4data.py is in the same directory

def decode(encoded_data):
    """
    Function: decode()
        Takes a list of run-length encoding (RLE) values and returns a list
        containing the decoded values with the "runs" expanded.

    Parameters:
        encoded_data list: A list of RLE values [element, count].

    Returns:
        list: A list containing the decoded values.
    """
    decoded_data = []

    i = 0
    while i < len(encoded_data):
        element = encoded_data[i]
        count = encoded_data[i + 1]
        decoded_data.extend([element] * count)
        i += 2

    return decoded_data

def main():
    # Access DATA0, DATA1, DATA2, etc. from the hw4data module
    DATA0 = hw4data.DATA0
    DATA1 = hw4data.DATA1
    DATA2 = hw4data.DATA2
    DATA3 = hw4data.DATA3
    DATA4 = hw4data.DATA4
    DATA5 = hw4data.DATA5

    decoded_data_0 = decode(DATA0)
    decoded_data_1 = decode(DATA1)
    decoded_data_2 = decode(DATA2)
    decoded_data_3 = decode(DATA3)
    decoded_data_4 = decode(DATA4)
    decoded_data_5 = decode(DATA5)

    # Print the decoded data for each dataset
    print("Decoded Data 0:", decoded_data_0)
    print("Decoded Data 1:", decoded_data_1)
    print("Decoded Data 2:", decoded_data_2)
    print("Decoded Data 3:", decoded_data_3)
    print("Decoded Data 4:", decoded_data_4)
    print("Decoded Data 5:", decoded_data_5)

if __name__ == "__main__":
    main()