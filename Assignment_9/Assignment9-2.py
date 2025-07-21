#Program using multiprocessing.Process to square a list of numbers using multiple processes.

import multiprocessing

def Square(value):
    square = 1
    List = []
    for i in value:
        square = i * i
        List.append(square)
    print("Squares : ",List)

def main():
    Data = []
    size = int(input("Enter number of elements : "))
    
    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    P1 = multiprocessing.Process(target = Square, args = (Data,))
    P2 = multiprocessing.Process(target = Square, args = (Data,))

    P1.start()
    P2.start()

if __name__ == "__main__":
    main()

'''
Enter number of elements : 4
Enter the elements :
2
3
4
5
Squares :  [4, 9, 16, 25]
Squares :  [4, 9, 16, 25]
'''