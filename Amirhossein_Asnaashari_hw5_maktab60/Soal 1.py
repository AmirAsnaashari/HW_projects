import os
f = open(os.getcwd()+"/myfile.csv")
lines = f.read()
f.close()


def reverse_array(b):
    for item in lines.split("\n"):
        a = []
        for i in item.split("   "):
            a.append(int(i))
        b.append(a)
    return [[b[j][i] for j in range(len(b))] for i in range(len(b[0]))]

def rv_2(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

bz = []
arr = reverse_array(bz)
temp = arr[0]
arr[0] = arr[1]
arr[1] = temp
arrT = map(lambda x, y, z: x + y + z, arr[0], arr[1], arr[2])
arr.append(list(arrT))
my_arr = ""
ba = rv_2(arr)

for item in ba:
    print(item)
    for i in item:
        my_arr+=str(i)+"   "
    my_arr+="\n"

print(my_arr)
f = open(os.getcwd()+"/myfile.csv", mode="w")
f.write(my_arr)
f.close()