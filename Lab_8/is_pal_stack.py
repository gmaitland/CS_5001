'''
    Stack Palindrome
    Taking the next step with Stacks!
    Reusing the pre_process function from our other versions of palindrome.
    Renaming it here because...well, we're actually allowing phrases not
    words, so it seemed like a better function name.
'''

from Stack import Stack

def pre_process_phrase(phrase):
    ''' function pre_process_phrase
        Input: a string (any phrase, word, letter)
        Returns: reformatted string lowercased and with blanks removed
        Does: Removes blanks and lowercases phrase so that palindrome
              test can be case-insensitive
    '''
    phrase = phrase.lower()
    phrase = phrase.replace(' ', '')
    return phrase

def is_pal_stack(phrase):
    if len(phrase) == 0 or len(phrase) == 1: # trivial case, true
        return True

    phrase = pre_process_phrase(phrase) # homogenize data
    
    stack = Stack()
    for each in phrase:
        stack.push(each)

    rev_phrase = ""
    while not stack.is_empty():
        rev_phrase += stack.pop() # pop every element; gives us reversed phrase

    if phrase == rev_phrase:
        return True
    return False


def main():
    words = ['tacocat','radar','borroworrob','madamimadam', 'aa', 'a', '']
    for each in words:
        if is_pal_stack(each):
            print(f"{each} IS a palindrome")
        else:
            print(f"{each} is NOT a palindrome")

    print()
    
    words = ['bigbear','Cat in the Hat','CS 5001','5005']
    for each in words:
        if is_pal_stack(each):
            print(f"{each} is a palindrome")
        else:
            print(f"{each} is NOT a palindrome")        

if __name__ == "__main__":
    main()
        
