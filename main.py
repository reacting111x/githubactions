# main.py

def write_apple():
    with open('test.txt', 'w') as f:
        f.write('apple')

if __name__ == "__main__":
    write_apple()
    print("Updated test.txt with 'apple'")
