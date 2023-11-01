"""
    Garfield Maitland
    CS 5001
    10/31/2023
    Lecture - stock_dictionary.py
"""

# What ticker symbol do you want?
# Bring back stock price to the user

def test_stocks():
    stocks = {"IBM": "$140",
              "AAPL": "$224.40",
              "NKE": "$92.85"
              }
    while True:
        stock = input("Enter a stock: ")
        stock = stock.upper()
        if stock == ":Q:":
            break
        if stock in stocks:
            print(f"The stock and the stock price is {stocks[stock]}")
        else:
            print(f"This stock and value for {stock} does not exist")


def main():
    """
    english = ["hello", "goodbye", "thank you"]
    french = ["bonjour", "au revoir", "merci"]
    spanish = ["hola", "adios", "gracias"]

    translator = [english, french, spanish]

    word = input("Enter a word in English: ")
    word = word.lower()

    if word in translator[0]:
        index = translator[0].index(word)
        print(f"Translated word is {translator[1][index]} in French")
        print(f"Translated word is {translator[2][index]} in Spanish")
    else:
        print(f"Cannot translate {word}")

    print("Done")
    """
    test_stocks()
    print("Done")
if __name__ == "__main__":
    main()
