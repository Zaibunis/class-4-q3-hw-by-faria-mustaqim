#What is Exception Handling?
#Exception handling is a way to manage errors in your code without crashing your program. When an error occurs, the program can handle it gracefully and continue running.

#Key Concepts:
#try block: This is where you put the code that might cause an error. If an error occurs, the program stops executing the try block and jumps to the except block.
#except block: This is where you handle the error. You can tell Python what to do if an error happens (like printing a message or fixing the issue).
#else block: This part runs if no error occurs in the try block. It's used to run code that should only happen if everything goes well.
#finally block: This part always runs, no matter what happens (whether there’s an error or not). It’s usually used for cleaning up resources, like closing files.

try:
    alphabet = input("Enter an alphabet: ")
    
    # Check if the input is a single alphabet letter
    if alphabet.isalpha() and len(alphabet) == 1:
        print(f"You entered: {alphabet}")
    else:
        raise ValueError("Oops! That's not a valid alphabet.")  # Raise error if not a single alphabet

except ValueError as a:
    print(a)
finally:
    print("Thank you for using the program.")
