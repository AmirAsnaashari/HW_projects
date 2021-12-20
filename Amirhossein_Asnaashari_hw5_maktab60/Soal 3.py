def print_list_element(thelist, index):
    print(thelist[index])

    try:
        thelist[index]

    except IndexError:
        if index > len(thelist):
            print("IndexError")


thelist = []
n = input("Enter your list:").split()
index = n
thelist.append(n)
