#  1.Task: Array Filtering and Mapping
#  Create an array of objects, each representing a person with properties like name, age, and gender.Write a function to filter out all females and then map the remaining people to an array of names.Print the final result.

#  Solution:

people = [
    {"name": "Alice", "age": 25, "gender": "female"},
    {"name": "Bob", "age": 30, "gender": "male"},
    {"name": "Charlie", "age": 22, "gender": "female"},
    {"name": "David", "age": 35, "gender": "male"},
    {"name": "Eva", "age": 28, "gender": "female"},
    {"name": "Harry", "age": 21, "gender": "male"},
    {"name": "Hermione", "age": 21, "gender": "female"},
]

def filter_and_map_names(people):
    return [person["name"] for person in people if person["gender"] == "female"]


print(filter_and_map_names(people))

# 2.Task: Object Manipulation
# Create an array of objects representing books with properties like title, author, and year. Write a function that takes the array and returns a new array with only the book titles. Print the result.

books = [
    {"title": "1984", "author": "George Orwell", "year": 1948},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
]

def get_book_titles(books):
    return [book["title"] for book in books]

print(get_book_titles(books))



# 3.Task: Function Composition
# Write three functions: one to square a number, one to double a number, and one to add 5 to a number. Compose these functions to create a new function that squares a number, doubles the result, and then adds 5.

def square(x):
    return x ** 2

def double(x):
    return x * 2

def add_five(x):
    return x + 5

def compose(f, g, h):
    return lambda x: h(g(f(x)))

square_then_double_then_add_five = compose(square, double, add_five)

print(square_then_double_then_add_five(3))



# 4.Task: Sorting Objects
# Create an array of objects representing cars with properties like make, model, and year. Write a function to sort the array of cars by the year of manufacture in ascending order. Print the sorted array.

cars = [
    {"make": "Toyota", "model": "Camry", "year": 2018},
    {"make": "Honda", "model": "Civic", "year": 2020},
    {"make": "Ford", "model": "Mustang", "year": 2015},
    {"make": "Chevrolet", "model": "Malibu", "year": 2019}, 
]

def sort_cars_by_year(cars):
    return sorted(cars, key=lambda car: car["year"])

print(sort_cars_by_year(cars))


# 5.Task: Find and Modify
# Write a function that searches an array of objects for a specific person by name. If found, modify their age property. Print the updated array.

array_of_people = [
    {"name": "Alice", "age": 25, "gender": "female"},
    {"name": "Bob", "age": 30, "gender": "male"},
    {"name": "Charlie", "age": 22, "gender": "female"},
    {"name": "David", "age": 35, "gender": "male"},
]

def find_and_modify_person(array_of_people, name, new_age):
    for person in array_of_people:
        if person["name"] == name:
            person["age"] = new_age
            break
    return array_of_people

print(find_and_modify_person(array_of_people, "Alice", 26))