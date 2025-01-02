if __name__ == '__main__':
    N = int(input())

    ar = []
    for _ in range(N):
        command_arg = input().strip().split(" ")
        cmd = command_arg[0]

        if cmd == "print":
            print(ar)
        elif cmd == "short":
            ar.sort()
        elif cmd == "reverse":
            ar.reverse()
        elif cmd == "pop":
            ar.pop()
        elif cmd == "remove":
            val = int(command_arg[1])
            ar.remove(val)
        elif cmd == "append":
            val = int(command_arg[1])
            ar.append(val)
        elif cmd == "insert":
            val = int(command_arg[2])
            pos = int(command_arg[1])
            ar.insert(pos, val)
