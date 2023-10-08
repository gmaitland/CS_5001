'''
   2023_Fall_CS5003_Lab_2
   09/21/2023_(09/22/2023)
   Garfield Maitland
   menu.py
'''

'''
Test case #1:
Input: a, b, c, d
Output: A, B, C, D
Test case #2:
Input: 1, 2, 3, 4
Output: A, B, C, D
Test case #3:
Input: qwerty
Output: Invalid response
'''

def menu(prompt):
    valid_answer = False
    while valid_answer == False:
        response = input(prompt)
        response = response[0]
        if response in ("abcdABCD"):
            valid_answer = True
        elif response == '1':
            response = 'A'
            valid_answer = True
        elif response == '2':
            response = 'B'
            valid_answer = True
        elif response == '3':
            response = 'C'
            valid_answer = True
        elif response == '4':
            response = 'D'
            valid_answer = True
        else:
            print("Invalid response")
    response = response.upper()
    print(response)
            
def main():
    question1 = ('How do you like to keep active?\n'
                'A: Running\nB: Birdwatching\nC: Swimming\n'
                'D: Does laying on a couch count?\n Your answer: ')

    question2 = ('What is your favorite food?\n'
                'A: Salad\nB: Cakes and Pies\nC: Sandwiches\n'
                'D: Yes\n Your answer: ')

    question3 = ('What grade do you want to get in CS 5001?\n'
                'A: A\nB: A\nC: A\n'
                'D: Is this a real question?\n Your answer: ')
  
    menu(question1)
    menu(question2)
    menu(question3)

if __name__ == "__main__":
    main()


