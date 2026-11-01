class Book:
    def __init__(self, title, author,  pages ):
        self.title = title 
        self.author = author
        self.pages = pages
    def info(self):
        print(f"нзвание {self.title} написал книгу {self.author} всего страниц {self.pages}")

q1 = Book("Война и мир", "Роналдо", 1488)
q1.info




# class Rectangle:
#     def __init__(self, width , height):
#         self.widht = width
#         self.height = height
#     def area(self):
#         print(self.width * self.heigth)
#     def perimeter(self):
#         print(sum * 2(self))
#     def info(self):
#         print(f"Периметр {self.perimeter()}")
#         print(f"размер {self.width} , {self.height}")
#         print(f"Площядь {self.area()}")
# a = Rectangle(4,5)
# a.info()

class TodoList:
    def __init__(self, tasks):
        self.tasks = tasks
    def add(self, task):
        self.tasks.append (task)
        print(f"Добавлено... {self.tasks}")
    def show(self):
        for i in self.tasks:
            print(i)

a = TodoList(['q,w,e'])
a.add("kdhgkrt8iojh")
print(a.tasks)