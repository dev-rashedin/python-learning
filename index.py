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


#  people = [
#   { name: 'Alice', age: 25, gender: 'female' },     
#   { name: 'Bob', age: 30, gender: 'male' },
#   { name: 'Charlie', age: 22, gender: 'female' },
#   { name: 'David', age: 35, gender: 'male' },
#   { name: 'Eva', age: 28, gender: 'female' },
#   { name: 'Harry', age: 21, gender: 'male' },
#   { name: 'Hermione', age: 21, gender: 'female' },
# ];

# // const filterAndMapNames = people.filter(person => person.gender === 'female').map(person => person.name);

# // console.log(filterAndMapNames)

# const filterAndMapNames = (arrayOfPeople) => { 
#   return arrayOfPeople
#     .filter(person => person.gender === 'female')
#     .map(person => person.name);
# }

# console.log(filterAndMapNames(people));


