def foo(x):
    if x < 0:
        return "I didn't do anything"
    print("I did something here")
    return "Something happened"

def main():
    print(foo(-1))
    print(foo(0))

if __name__ == "__main__":
    main()
    
