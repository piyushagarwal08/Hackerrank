if __name__ == '__main__':
    N = int(input())
    answer = []
    for i in range(N):
        command = input().split()
        if command[0] == 'insert':
            answer.insert(int(command[1]),int(command[2]))
        elif command[0] == 'remove':
            answer.remove(int(command[1]))
        elif command[0] == 'sort':
            answer = sorted(answer)
        elif command[0] == 'reverse':
            answer.reverse()
        elif command[0] == 'append':
            answer.append(int(command[1]))
        elif command[0] == 'pop':
            answer.pop()
        else:
            print(answer)