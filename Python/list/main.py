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



if __name__ == '__main__':
    listCommand = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort", "print", "pop", "reverse", "print"]
    list_operation(listCommand)



 ar = []
    for _ in range(N):
        command_args = input().strip().split(" ")
        cmd = command_args[0]
        if cmd == "print":
            print(ar)
        elif cmd == "sort":
            ar.sort()
        elif cmd == "reverse":
            ar.reverse()
        elif cmd == "pop":
            ar.pop()
        elif cmd == "remove":
            val = int(command_args[1])
            ar.remove(val)
        elif cmd == "append":
            val = int(command_args[1])
            ar.append(val)
        elif cmd == "insert":
            pos = int(command_args[1])
            val = int(command_args[2])
            ar.insert(pos, val)