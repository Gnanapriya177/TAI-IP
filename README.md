Task Output and Description is given below:

Level-1_Task-1_Number_Guessing_Name:

Description:
This Python code defines a simple number guessing game. Here's the working of the code :
1) A random number between ( 1 to 50 ) is generated using the random.randint(1, 50) function.
2) The user is prompted to guess the level of the game, If the level is easy you have 10 attempts and if it is hard you have 5 attempts to guess the number right.
3)  Now, the user starts guessing the number, if the number is correct it prints "Your guess is right". If the number is incorrect and attemps > 0 the code gives a hint but if the number is incorrect and attempts = 0 then it prints "You are out of guesses... you lose". The code Terminates.

OUTPUT:

![Screenshot (2)](https://github.com/Gnanapriya177/TAI-IP/assets/133194111/d3982e43-2097-4a42-bd78-f4800ee4a4cf)

Level-1_Task-2_Countdown_Timer:

Description:
This Python code defines simple the countdown timer using the time module and the sleep() function.
1) Import sleep from time module.
2) Take seconds as input from the user and convert it into the integer, if the seconds > 0 convert it into minutes and seconds using the divmod() function.
3) print the time, with sleep(1) and reduce the seconds by 1.
4) If the seconds < 0 then, the code prints "Seconds must be greater than 0". Terminate the code.

OUTPUT:

![Screenshot (3)](https://github.com/Gnanapriya177/TAI-IP/assets/133194111/f200ac07-4cb9-4daf-a27a-947286f2ee4c)

Level-2_Task-1_Credit_Card_Validator:

Description:
This Python code validates the credit card number taken from the user input and produce output as valid or invalid credit card.
1) Take the input from the user input and remove all the '-' or ' '.
2) Add all the digits in the odd places from right to the left store it as odd_sum.
3) Double every second digit from right ot left, If result is two digit number, add the two digit number together to get a single digit and store it as even_sum.
4) Sum the totals of odd_sum and even_sum.
5) If sum is divisible by 10, then the output prints as credit card is valid else it prints as credit is invalid.

OUTPUT:

![Screenshot (4)](https://github.com/Gnanapriya177/TAI-IP/assets/133194111/efe166f7-82e1-4aba-9ad8-38fa1efd4674)




