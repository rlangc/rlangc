# Simple Fortune Cookie (with improvements shown)

This project is a simple fortune-teller program that randomly generates a lucky number and a fortune message. It uses Python's random module to select a number between 1 and 100 as the lucky number and picks ```random``` fortune statement from a predefined set of messages. The program provides a fun and lighthearted way to predict the user's day or future with a random element of surprise!

<h2></h2>

<h3>Orignal Code</h3>

```
import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = ''

if fortune_number == 1:
    fortune_text = 'You will have a great day!'
if fortune_number == 2:
    fortune_text = 'Today will be tough, but worth it!'
if fortune_number == 3:
    fortune_text = 'You will get married this year!'

print(f'{fortune_text} Your lucky number is: {lucky_number}')

```

<h3>Description of the Original Code</h3>

The original script is a simple fortune-teller program that:

1. Generates a random lucky number between 1 and 100
2. Generates a random fortune number between 1 and 3
3. Uses a series of if statements to determine a fortune based on fortune_number:
    - If ```fortune_number == 1```: "You will have a great day!"
    - If ```fortune_number == 2```: "Today will be tough, but worth it!"
    - If ```fortune_number == 3```: "You will get married this year!"   
4. Prints the fortune message and lucky number.

<h3>Problems in the Original Code</h3>

While the code works correctly, it has some inefficiencies:

- Multiple ```if``` statements: Instead of checking conditions separately, a dictionary lookup would be cleaner
- Manual string assignment: Assigning ```fortune_text``` manually in each condition is unnecessary
- Harder to scale: If you wanted to add more fortunes, you'd need to add more ```if``` statements, making the code harder to maintain

<h2>Improvement</h2>

I wanted to improve the fortune-teller program by making it more efficient, readable, and scalable. Instead of using multiple if statements to assign a fortune message, I aimed to streamline the process using a dictionary lookup, which simplifies the code and makes it easier to expand. By implementing these improvements, the program became cleaner, more maintainable, and better suited for adding new fortunes in the future.

<h3>Optimzied Code</h3>

```

import random

lucky_number = random.randint(1, 100)

fortunes = {
    1: 'You will have a great day!',
    2: 'Today will be tough, but worth it!',
    3: 'You will get married this year!'
}

fortune_text = fortunes.get(random.randint(1, 3), 'Unexpected fortune!')

print(f'{fortune_text} Your lucky number is: {lucky_number}')

```

<h3>Improvements in the Optimized Code</h3>

| **Aspect**          | **Original Code** | **Improved Code** | **Benefit** |
|---------------------|-------------------|-------------------|-------------|
| **Fortune Selection** | Used multiple `if` statements to assign `fortune_text` | Used a dictionary (`fortunes`) with `.get()` to retrieve the fortune message | More readable, easier to update          |
| **Code Efficiency**  | Each fortune assignment required a separate check | One dictionary lookup finds the message in a single step | Reduces redundant condition checks       |
| **Scalability**      | Adding more fortunes means more `if` statements   | Just add a new key-value pair to the dictionary | Easier to expand                          |
| **Error Handling**   | No handling for unexpected values                 | `.get()` includes a fallback message         | Prevents potential errors                 |

<h3>Summary of Key Changes</h3>

- Replaced ```if``` conditions with a dictionary lookup for simplicity
- Used ```.get()``` method to avoid errors and improve readability
- Made the code scalable – Adding new fortunes now only requires updating the dictionary
- Used an ```f-string``` more effectively to make the print statement cleaner

<h2>Final Thought</h2>

Both versions work, but the improved version makes it more readable, maintainable, and efficient. If you want to add more fortunes, just update the dictionary without modifying the logic!

<h2></h2>
<p align="center">
  <a href="https://github.com/rlangc"><b>Return to Home</b></a>
