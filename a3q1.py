# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442

while True:
    u_Input = input("Enter the type of container you want to make: ")
    if u_Input == "s":
        import Stack

        container = Stack.Stack()
        while True:
            print("Please enter a Symbol :")
            Symbol = input()
            if Symbol == "add":
                print("Please enter a value to add :")
                n = input()
                container.push(n)
            elif Symbol == "peak":
                print(container.peek())
            elif Symbol == "remove":
                container.pop()
            elif Symbol == "help":
                print("“add” Will need to prompt the user to for a value as well.\n"
                      "“peak” Will give the first element of the container.\n"
                      "“remove” Will remove the first element of the container.\n"
                      "“help” Will print what actions are possible.\n"
                      "“quit” End program.")
            elif Symbol == "quit":
                print("Goodbye.")
                break
            else:
                print("Invalid Symbol")

    elif u_Input == "q":
        import Queue

        container = Queue.Queue()
        while True:
            print("Please enter a Symbol :")
            Symbol = input()
            if Symbol == "add":
                print("Please enter a value to add :")
                n = input()
                container.enqueue(n)
            elif Symbol == "peak":
                print(container.peek())
            elif Symbol == "remove":
                container.dequeue()
            elif Symbol == "help":
                print("“add” Will need to prompt the user to for a value as well.\n"
                      " “peak” Will give the first element of the container.\n"
                      " “remove” Will remove the first element of the container.\n"
                      " “help” Will print what actions are possible.\n"
                      " “quit” End program.")
            elif Symbol == "quit":
                print("Goodbye.")
                break
            else:
                print("Invalid Symbol")

    else:
        print("Inappropriate input \nPlease enter s for stack container or q for queue container")
        continue
    break
