if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.