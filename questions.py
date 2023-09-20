questions = [
    (
        "Declare a Python variable 'name' and assign it the value 'John'.",
        "name = 'John'\n",
        "python",
    ),
    (
        "Write a Python function called 'add' that takes two parameters 'a' and 'b' and returns their sum.",
        "def add(a, b):\n    return a + b\n",
        "python",
    ),
    (
        "Create a Python list named 'colors' containing the strings 'red', 'green', and 'blue'.",
        "colors = ['red', 'green', 'blue']\n",
        "python",
    ),
    (
        "Write a 'for' loop in Python that iterates from 1 to 5 and prints each number.",
        "for i in range(1, 6):\n    print(i)\n",
        "python",
    ),
    (
        "Define a Python dictionary 'person' with keys 'name' (string) and 'age' (integer).",
        "person = {'name': 'John', 'age': 30}\n",
        "python",
    ),
    (
        "Write a Python function 'is_even' that takes an integer 'num' as an argument and returns True if it's even, False otherwise.",
        "def is_even(num):\n    return num % 2 == 0\n",
        "python",
    ),
    (
        "Create a Python class 'Car' with an '__init__' method that initializes 'make' and 'model' attributes.",
        "class Car:\n    def __init__(self, make, model):\n        self.make = make\n        self.model = model\n",
        "python",
    ),
    (
        "How can you remove an element at a specific index from a Python list?",
        "You can use 'del' statement or 'pop()' method, e.g., 'del mylist[index]' or 'mylist.pop(index)'\n",
        "python",
    ),
    (
        "Write Python code to check if a given string 'text' contains the word 'apple'.",
        "text = 'This is an apple.'\nif 'apple' in text:\n    print('Contains apple.')\nelse:\n    print('Does not contain apple.')\n",
        "python",
    ),
    (
        "Create a Python function 'greet' that takes a name as an argument and prints 'Hello, <name>!'",
        "def greet(name):\n    print(f'Hello, {name}!')\n",
        "python",
    ),
    (
        "Define a Python class 'Rectangle' with 'width' and 'height' attributes and a method 'area' that calculates the area.",
        "class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    def area(self):\n        return self.width * self.height\n",
        "python",
    ),
    (
        "Write Python code to read the contents of a file named 'example.txt' and store it in a variable 'content'.",
        "with open('example.txt', 'r') as file:\n    content = file.read()\n",
        "python",
    ),
    (
        "Create a Python list 'numbers' containing integers from 1 to 10 using a list comprehension.",
        "numbers = [i for i in range(1, 11)]\n",
        "python",
    ),
    (
        "Write Python code to reverse a string 'text' and store the result in a variable 'reversed_text'.",
        "text = 'Hello'\nreversed_text = text[::-1]\n",
        "python",
    ),
    (
        "Define a Python function 'cube' that takes a number 'x' as an argument and returns the cube of 'x'.",
        "def cube(x):\n    return x**3\n",
        "python",
    ),
    (
        "Declare a JavaScript variable 'name' and assign it the value 'John'.",
        "var name = 'John';\n",
        "javascript",
    ),
    (
        "Write a JavaScript function called 'add' that takes two parameters 'a' and 'b' and returns their sum.",
        "function add(a, b) {\n  return a + b;\n}\n",
        "javascript",
    ),
    (
        "Create a JavaScript array named 'colors' containing the strings 'red', 'green', and 'blue'.",
        "var colors = ['red', 'green', 'blue'];\n",
        "javascript",
    ),
    (
        "Write a 'for' loop in JavaScript that iterates from 1 to 5 and logs each number to the console.",
        "for (let i = 1; i <= 5; i++) {\n  console.log(i);\n}\n",
        "javascript",
    ),
    (
        "Define a JavaScript object 'person' with properties 'name' (string) and 'age' (number).",
        "var person = {\n  name: 'John',\n  age: 30\n};\n",
        "javascript",
    ),
    (
        "Write a JavaScript function 'isEven' that takes an integer 'num' as an argument and returns true if it's even, false otherwise.",
        "function isEven(num) {\n  return num % 2 === 0;\n}\n",
        "javascript",
    ),
    (
        "Create an HTML button with the text 'Click Me' using JavaScript and append it to the DOM.",
        "var button = document.createElement('button');\nbutton.textContent = 'Click Me';\ndocument.body.appendChild(button);\n",
        "javascript",
    ),
    (
        "Create an anonymous function in JavaScript that alerts the message 'Hello, World!' when invoked.",
        "(function() {\n  alert('Hello, World!');\n})();\n",
        "javascript",
    ),
    (
        "Define a JavaScript function 'multiply' that takes two parameters 'x' and 'y' and returns their product.",
        "function multiply(x, y) {\n  return x * y;\n}\n",
        "javascript",
    ),
    (
        "Write JavaScript code to change the background color of an HTML element with the id 'myElement' to 'blue'.",
        "document.getElementById('myElement').style.backgroundColor = 'blue';\n",
        "javascript",
    ),
    (
        "Create an array 'numbers' containing integers from 1 to 10 using a JavaScript loop.",
        "var numbers = [];\nfor (let i = 1; i <= 10; i++) {\n  numbers.push(i);\n}\n",
        "javascript",
    ),
    (
        "Write JavaScript code to reverse a string 'str' and store the result in a variable 'reversedStr'.",
        "var str = 'Hello';\nvar reversedStr = str.split('').reverse().join('');\n",
        "javascript",
    ),
    (
        "Define a JavaScript function 'square' that takes a number 'x' and returns the square of 'x'.",
        "function square(x) {\n  return x * x;\n}\n",
        "javascript",
    ),
]
