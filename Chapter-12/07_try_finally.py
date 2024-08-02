"""
The finally block is always executed, even if a return, break, continue, or exception is encountered in the try block. 
This ensures that any necessary cleanup code in the finally block will run regardless of what happens in the try or except blocks.
"""


def main():
    try:
        a = int(input("Enter a number: "))
        print(a)

    except Exception as e:
        print(e)

    finally:  # This else block will execute if the code inside try block runs successfully
        print("Heyy I am in finally block")


main()
