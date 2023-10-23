"""
    Garfield Maitland
    CS 5001
    10/17/2023
    Lecture - file_examples.py
"""

# Supports keyword arguments
# Ensure that your code is portable

def write_msg(file_name, additional_msg = " "):
    """ writes a message to a text file """
    with open(file_name, mode = "w") as outfile:
        outfile.write("Keith is Fantastic!\n")
        outfile.write("At least HE thinks so!\n")
        outfile.write("LOL!\n")
        outfile.write(additional_msg)

def read_msg(file_name):
    with open(file_name, mode = "r") as infile:
        for each in infile:
            print(each.strip("\n")) # What happened??!!??

def main():
    # write_msg("Tuesday.txt")
    # write_msg("Northeastern.txt)
    write_msg("Sunday.txt")
    write_msg("Monday.txt", "Ba-da-ba-ba-baa! I'm lovin' it!")
    write_msg(additional_msg = "Ba-da-ba-ba-baa! I'm lovin' it!", file_name = "Thursday.txt") 
    # read_msg("Northeastern.txt")
    print("Done")

if __name__ == "__main__":
    main()

