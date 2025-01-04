def add(a, b):
    result = a + b
    with open('result.txt', 'w') as f:
        f.write(f"resultoutput={result}")
    return result

if __name__ == "__main__":
    print(add(2, 44444))
