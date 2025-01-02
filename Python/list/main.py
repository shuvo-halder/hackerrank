def list_operation(listCommand):
    my_list = []

    for command in listCommand:
        parts = command.split()
        cmd = parts[0]

        if cmd == "insert":
            my_list.insert(int(parts[1]), int(parts[2]))
        elif cmd == "print":
            print(my_list)
        elif cmd == "remove":
            my_list.remove(int(parts[1]))
        elif cmd == "append":
            my_list.append(int(parts[1]))
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()

listCommand = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort", "print", "pop", "reverse", "print"]
list_operation(listCommand)