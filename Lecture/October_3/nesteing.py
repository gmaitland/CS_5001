"""
    Nested Functions
"""


PI = 3.1415 # Enclosing scope (Or Global Scope), (Module Scope)

def test():
    print("Hello World!")
    x =1

    # Within local scope, not at global scope
    
    def inner_test():
        print("Let's go to dinner, Inner!")
        print("Outer's x value is: ", x)

    inner_test() # Function call operator, inner_test is the call


def main():
    test()

if __name__ == "__main__":
    main()
