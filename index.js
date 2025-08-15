// 1.Task: Array Filtering and Mapping
// Create an array of objects, each representing a person with properties like name, age, and gender.Write a function to filter out all females and then map the remaining people to an array of names.Print the final result.

// Solution:

const people = [
  { name: 'Alice', age: 25, gender: 'female' },     
  { name: 'Bob', age: 30, gender: 'male' },
  { name: 'Charlie', age: 22, gender: 'female' },
  { name: 'David', age: 35, gender: 'male' },
  { name: 'Eva', age: 28, gender: 'female' },
];

// const filterAndMapNames = people.filter(person => person.gender === 'female').map(person => person.name);

// console.log(filterAndMapNames)

const filterAndMapNames = (arrayOfPeople) => { 
  return arrayOfPeople
    .filter(person => person.gender === 'female')
    .map(person => person.name);
}

console.log(filterAndMapNames(people));



// 2.Task: Object Manipulation
// Create an array of objects representing books with properties like title, author, and year. Write a function that takes the array and returns a new array with only the book titles. Print the result.

const books = [
  { title: '1984', author: 'George Orwell', year: 1949 },
  { title: 'To Kill a Mockingbird', author: 'Harper Lee', year: 1960 },
  { title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', year: 1925 },
  { title: 'Pride and Prejudice', author: 'Jane Austen', year: 1813 },
  { title: 'The Catcher in the Rye', author: 'J.D. Salinger', year: 1951 },
];

const getBookTitles = (arrayOfBooks) => {
  return arrayOfBooks.map(book => book.title);
}

console.log(getBookTitles(books));


// 3.Task: Function Composition
// Write three functions: one to square a number, one to double a number, and one to add 5 to a number. Compose these functions to create a new function that squares a number, doubles the result, and then adds 5.

const makeSquare = (num) => num * num;
const makeDouble = (num) => num * 2;  
const add5 = (num) => num + 5;

const composeFunctions = (num) => {
  return add5(makeDouble(makeSquare(num)));
}

console.log(composeFunctions(3));


// 4.Task: Sorting Objects
// Create an array of objects representing cars with properties like make, model, and year. Write a function to sort the array of cars by the year of manufacture in ascending order. Print the sorted array.

const cars = [
  { make: 'Toyota', model: 'Corolla', year: 2020 },   
  { make: 'Honda', model: 'Civic', year: 2018 },
  { make: 'Ford', model: 'Focus', year: 2019 },
  { make: 'Chevrolet', model: 'Malibu', year: 2021 },
  { make: 'Nissan', model: 'Sentra', year: 2017 },
];

const sortByYear = (arrayOfCars) => {
  return arrayOfCars.sort((a, b) => a.year - b.year);
}

console.log(sortByYear(cars));


// 5.Task: Find and Modify
// Write a function that searches an array of objects for a specific person by name. If found, modify their age property. Print the updated array.

const arrayOfPeople = [
  { name: 'Alice', age: 25 },
  { name: 'Bob', age: 30 },
  { name: 'Charlie', age: 22 },
  { name: 'David', age: 35 },
  { name: 'Eva', age: 28 },
];

const findAndModify = (name) => {
  const personToModify = arrayOfPeople.find(person => person.name === name);
  if (!personToModify) {
    return 'Person not found';
  }
  personToModify.age = 27;
  return arrayOfPeople;
}

console.log(findAndModify('Charlie'));