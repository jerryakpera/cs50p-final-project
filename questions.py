questions = [
    (
        "How do you split a variable called 'text' by a comma and save the parts into a list?",
        "parts = text.split(',')",
        "python",
    ),
    (
        "What Python function is used to check the length of a list named 'my_list'?",
        "len(my_list)",
        "python",
    ),
    (
        "How do you add a new item 'item' to the end of a list 'my_list'?",
        "my_list.append(item)",
        "python",
    ),
    (
        "What is the syntax for defining a Python function named 'add' that takes two arguments 'a' and 'b' and returns their sum?",
        "def add(a, b): return a + b",
        "python",
    ),
    (
        "How do you remove the last item from a list 'my_list'?",
        "my_list.pop()" "python",
    ),
    ("What is the Python keyword for defining a conditional statement?", "if" "python"),
    (
        "How do you declare a variable 'x' and assign it the value 42?",
        "x = 42" "python",
    ),
    (
        "What method is used to capitalize the first letter of a string 'text'?",
        "text.capitalize()",
        "python",
    ),
    (
        "How do you check if a key 'key' exists in a dictionary 'my_dict'?",
        "'key' in my_dict",
        "python",
    ),
    (
        "How do you open a file named 'file.txt' in Python for writing?",
        "file = open('file.txt', 'w')",
        "python",
    ),
    (
        "How do you create a tuple 'my_tuple' with three elements '1', '2', and '3'?",
        "my_tuple = (1, 2, 3)",
        "python",
    ),
    (
        "What Python keyword is used to create a loop that repeats a block of code a specified number of times?",
        "for",
        "python",
    ),
    (
        "How do you remove all occurrences of the value 'x' from a list 'my_list'?",
        "my_list.remove(x)",
        "python",
    ),
    (
        "How do you define a Python lambda function that squares a number 'x'?",
        "square = lambda x: x ** 2",
        "python",
    ),
    ("What is the Python operator for exponentiation?", "**" "python"),
    (
        "How do you check if a file 'file.txt' exists in the current directory (assume the required packages are already imported)?",
        "if os.path.exists('file.txt'):",
        "python",
    ),
    (
        "How do you replace all occurrences of 'old' with 'new' in a string 'text'?",
        "text.replace('old', 'new')",
        "python",
    ),
    (
        "How do you round a floating-point number 'x' to two decimal places?",
        "rounded = round(x, 2)",
        "python",
    ),
    (
        "What is the syntax for defining a Python class named 'Person'?",
        "class Person:",
        "python",
    ),
    (
        "How do you find the maximum value in a list 'my_list'?",
        "max_value = max(my_list)",
        "python",
    ),
    (
        "Write JavaScript code to convert the string 'hello' to uppercase using the toUpperCase() method.",
        "let str = 'hello';\nlet upperCaseStr = str.toUpperCase();",
        "javascript",
    ),
    (
        "Create an array called 'fruits' and use the push() method to add the string 'apple' to it.",
        "let fruits = [];\nfruits.push('apple');",
        "javascript",
    ),
    (
        "Declare a JavaScript function named 'addNumbers' that takes two parameters, 'num1' and 'num2', and returns their sum.",
        "function addNumbers(num1, num2) {\n  return num1 + num2;\n}",
        "javascript",
    ),
    (
        "Write JavaScript code to remove the last element from the array 'myArray' using the pop() method.",
        "myArray.pop();",
        "javascript",
    ),
    (
        "Select an HTML element with the class 'example' using the querySelector() method and store it in a variable named 'element'.",
        "let element = document.querySelector('.example');",
        "javascript",
    ),
    (
        "Declare a variable 'x' using 'let', a constant variable 'y' using 'const', and a variable 'z' using 'var'.",
        "let x = 5;\nconst y = 10;\nvar z = 'Hello';",
        "javascript",
    ),
    (
        "Use the forEach() method to iterate through the array 'numbers' and log each element to the console.",
        "numbers.forEach(function(element) {\n  console.log(element);\n});",
        "javascript",
    ),
    (
        "Create a JavaScript function named 'multiply' that takes two parameters, 'a' and 'b', and returns the result of multiplying them.",
        "function multiply(a, b) {\n  return a * b;\n}",
        "javascript",
    ),
    (
        "Attach a click event listener to an HTML button with the id 'myButton' and call a function 'handleClick' when the button is clicked.",
        "document.getElementById('myButton').addEventListener('click', handleClick);",
        "javascript",
    ),
    (
        "Use the slice() method to extract elements from the array 'myArray' starting from index 2 to index 4 and store them in a new array called 'subset'.",
        "let subset = myArray.slice(2, 5);",
        "javascript",
    ),
]