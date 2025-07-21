class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print("Book name : "+self.Name)
        print("Author Name : "+self.Author)
        print("No of books : ",BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Linux System Programming","Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()

'''
Book name : Linux System Programming
Author Name : Robert Love
No of books :  1

Book name : C Programming
Author Name : Dennis Ritchie
No of books :  2
'''