from manager import run

def main():
    # Enter file text here
    filename = '.\inputs\process5.txt'
    run(filename)
    test()

def test():
    items = [4, 3, 1, 8, 12, 6]
    items2 = items
    list.sort(items)
    items.pop(0)
    print(items2)

if __name__ == "__main__":
    main()
