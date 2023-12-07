"""
    CS 5001
    12/03/2023
    Final Exam - final.py
    Garfield Maitland
"""


# 7
class Item:
    """
    Class: Item()
        Creates an item and assigns it a name, quantity, and expiration date.

    Parameters:
        name (type: string)
        quantity (type: int)
        expiration_date (type: string)

    Returns:
        name, quantity, expiration_date

    Defense:
        Raises ValueError if quantity < 0
    """
    def __init__(self, name, quantity, expiration_date):
        self._name = name
        self.quantity = quantity
        self._expiration_date = expiration_date

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("The quantity is not allowed to be less than 0")
        self._quantity = int(value)

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def get_name(self):
        return self._name

    def __str__(self):
        return f"{self._name}:{self._quantity}:{self._expiration_date}"
        # return f"Name: {self._name}, Number of items:
        # {self._quantity}, Expiration Date: {self._expiration_date}"

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self._name.lower() == other._name.lower()


# 8
def shift(msg, shift_value):
    """
    Function: shift()
        Is a function that looks at a message and identifies the shift value.
        The function then converts the message into a string of values,
        shifts and then converts it back.

    Parameters:
        msg (type: string)
        shift_value (type: int)

    Returns:
        string

    Defense:
        None
    """
    ASCII_A = 65
    ASCII_Z = 90
    ALPHABET_SIZE = 26

    msg = msg.upper()

    if shift_value < 0 or shift_value > 15:
        return msg

    shifted_msg = []
    for char in msg:
        ascii_value = ord(char)
        if ASCII_A <= ascii_value <= ASCII_Z:
            shifted_ascii = (ascii_value - ASCII_A + shift_value) % ALPHABET_SIZE + ASCII_A
            shifted_char = chr(shifted_ascii)
        else:
            shifted_char = char
        shifted_msg.append(shifted_char)

    return ''.join(shifted_msg)


def slide(msg, slide_value):
    if len(msg) == 0:
        return msg
    slide_value %= len(msg)
    return msg[-slide_value:] + msg[:-slide_value]


def encrypt(function, msg, slide_shift_value):
    return function(msg, slide_shift_value)


# 9
def file_away(filename):
    """
    Function: fileaway()
        Creates an empty dictionary, and reads each line of the file.
        The '|' delimiter is used to check the formatting and to identify
        the name from the quote.
    Parameters:
        filename (type: file)

    Returns:
        quotes_dict (type: dict)

    Defense:
        An exception is placed into an empty dictionary
    """
    try:
        quotes_dict = {}
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 2:
                    quotes_dict[parts[0]] = parts[1] + '\n'

        return quotes_dict

    except Exception:
        return {}


# 10
def raise_to_power(base_value, exponent_value):
    """
    Function: raise_to_power()
        A recursive function that has a base case of 0 and
        a recursive case that decreases by 1

    Parameters:
        base_value (type: int)
        exponent_value (type: int)

    Returns:
        1, raise_to_power

    Defense:
        None
    """
    if exponent_value == 0:
        return 1
    else:
        return base_value * raise_to_power(base_value, exponent_value - 1)


# 11
def is_missing(list):
    """
    Function: is_missing()
        Finds the missing number in an array of integers that are not
        sorted from 1 to n and the returns tha integer. The time
        complexity of this algorithm is 0(n) which is linear time.

    Parameters:
        list (type: list)

    Returns:
        int

    Defense:
        None
    """
    n = len(list) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(list)
    return expected_sum - actual_sum


# 12
def equal_stacks(stack1, stack2):
    """
    Function: equal_stacks()
        Checks the size of two stacks. Determines if they are equal.
        Iteratively checks the items in each stack by using conditional
        statements, while loops, and nested while loops.

    Parameters:
        stack1 (type: int)
        stack2 (type: int)

    Returns:
        stacks_are_equal

    Defense:
        None
    """
    if stack1.size() != stack2.size():
        return False

    temporary_stack1 = Stack()
    temporary_stack2 = Stack()
    stacks_are_equal = True

    while not stack1.is_empty() and not stack2.is_empty():
        element1 = stack1.pop()
        element2 = stack2.pop()

        temporary_stack1.push(element1)
        temporary_stack2.push(element2)

        if element1 != element2:
            stacks_are_equal = False
            break

    while not temporary_stack1.is_empty():
        stack1.push(temporary_stack1.pop())

    while not temporary_stack2.is_empty():
        stack2.push(temporary_stack2.pop())

    return stacks_are_equal


""""
def main():
    banana_item = Item("Banana", 7, "01/01/2025")
    print(banana_item)
    recursion_test = raise_to_power(3, 4)
    print(recursion_test)
    stacka = [1,2,3,4,5]
    stackb = [1,2,3,4,5]
    stackc = [5,4,3,2,1]
    print(is_missing([2, 3, 4]))
    print(is_missing([4, 1, 3]))
    print(equal_stacks(stacka, stackb))
    print(equal_stacks(stackb, stackc))


if __name__ == "__main__":
    main()

"""
