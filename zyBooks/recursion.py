
"""
Let me also try on the recursion.py file

def count_up(count):
    if count == 100:
        print('Excellent')
    else:
        print(f'{count}, ok')
        count_up(count + 1)

count_up(80)
"""

def count_up(count):
    while count != 100:
        print(f'{count}, ok')
        count_up(count + 1)
    else:
        print('Excellent')

count_up(80)
