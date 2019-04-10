def find_uniq(arr):

        arr.sort()
        if arr[0] != arr[1]:
            return arr[0]
        elif arr[len(arr) - 1] != arr[len(arr) - 2]:
            return arr[len(arr) - 1]

def sqrnumbers( x):
    numbers = []
    for i in range(0, x):
        y = eval(input("Enter number here:"))
        numbers.append(y)
    for j in range(0, len(numbers)):
        numbers[j] = (numbers[j]) ** 2
        print(numbers[j])


def letter_position( word):
    alphabets = ["a", "b", "c", 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', "z"]
    talk = list(word)
    f = ""
    for i in range(0, (len(talk))):
        if talk[i] in alphabets:
            alphabet_position = alphabets.index(talk[i]) + 1
            f += str(alphabet_position) + " "
            str(f)

    print(f)


def narcissistic(value):
    sum = 0
    value = str(value)
    for i in value:
        sum += int(i) ** len(value)
    value = int(value)
    if sum == value:

        return True
    else:
        return False


def __init__(self):
    print("this is my first class")

fob=open('c:/doc/mind your business.txt','w',)
fob.close()




def euclid(x,y):
    if x < y:
        print("The first number should be greater than the last")
    else:
        while y!=0:
            (x,y)=(y, x % y)
    print("The gcd is : ", x)
    return x


def fibbonaci(n):
    first=1
    second=1
    my_list=[first,second]
    result=first+second
    if n==1:
        print(first)
    else:
        for i in range (1,n-1):
            next_num=first + second
            result+=next_num
            my_list.append(next_num)
            first=second
            second=next_num

    return my_list,result

num=int(input("Enter the number of terms you want to view: "))
print("The first ", num, " terms of the fibbonaci series and their sum is ", fibbonaci(num))


