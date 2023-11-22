def do_something(n):
    if n > 0:
        do_something(n - 1)
        # print(n, end="")
        print(n)
        do_something(n - 1)

def main():
    do_something(3)

if __name__ == "__main__":
    main()
