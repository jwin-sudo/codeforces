from sys import stdin, stdout 
 
def main():
    a = int(stdin.readline().strip())
    print(6*a*(a-1) + 1)
if __name__ == "__main__":
    main()