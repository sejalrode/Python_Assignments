#Accept a list of integers from user & use map() function to double each no.

Double = lambda No : No * 2

def main():
    Data = []

    size = int(input("Enter number of elements : "))

    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    MData = list(map(Double,Data))
    print("Doubled list : ",MData)

if __name__ == "__main__":
    main()

'''
Enter number of elements : 5
Enter the elements :
1
2
3
4
5
Doubled list :  [2, 4, 6, 8, 10]
'''