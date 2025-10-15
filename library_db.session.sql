-- Creating tables

CREATE TABLE IF NOT EXISTS authors (
    authorId SERIAL PRIMARY KEY,
    authorName VARCHAR(150),
    countryOfOrigin VARCHAR(150),
    numberOfBooksWritten INT
);

CREATE TABLE IF NOT EXISTS books (
    bookId SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    authorId INT,
    genre VARCHAR(150) NOT NULL,
    dateOfPublication DATE,
    publisher VARCHAR(150) NOT NULL,
    isbn VARCHAR(150) NOT NULL,
    language VARCHAR(150),
    availableCopies INT NOT NULL,
    ageRating VARCHAR(150),
    FOREIGN KEY (authorId) REFERENCES authors(authorId)
);

CREATE TYPE fulfilment as ENUM ('Pending', 'Fulfilled', 'Processing');

CREATE TABLE IF NOT EXISTS BookOrders (
    orderId SERIAL PRIMARY KEY,
    orderDate DATE,
    bookId INT,
    cost DECIMAL(10, 2),
    quantity INT NOT NULL,
    supplyDate DATE,
    fulfillmentStatus fulfilment,
    supplierName VARCHAR(105) NOT NULL
);

CREATE TABLE IF NOT EXISTS borrowHistory (
    borrowedId SERIAL PRIMARY KEY,
    bookId INT,
    memberId INT,
    borrowDate DATE,
    returnDate DATE,
    FOREIGN KEY (bookId) REFERENCES books(bookId),
    FOREIGN KEY (memberId) REFERENCES members(memberId)
);

CREATE TABLE departments (
    departmentId SERIAL PRIMARY KEY,
    departmentName VARCHAR(150),
    managerName VARCHAR(150)
);

CREATE TABLE libraryStaff (
    staffID SERIAL PRIMARY KEY,
    name VARCHAR(155),
    jobTitle VARCHAR(155),
    departmentId INT,
    gender gender,
    address VARCHAR(155),
    phoneNumber VARCHAR(30),
    hireDate DATE,
    managerId INT,
    FOREIGN KEY (departmentId) REFERENCES departments(departmentId)
);


DROP TABLE librarystaff;
SELECT * FROM librarystaff;
SELECT * FROM departments;

SELECT authorId, pg_typeof(authorid) FROM authors LIMIT 5;