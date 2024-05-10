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

Level-2_Task-2_Location_Finder:

Description:
This code defines a Python function named location_of_the_user that uses the Nominatim class from the geopy.geocoders module to get the GPS coordinates of a user's location based on their input (e.g., city, country).
1) Import the Necessary Libraries,here the code imports the Nominatim class from the geopy.geocoders module.
2) The location_of_the_user function is defined to fetch the user's GPS coordinates. Within this function,A Nominatim object named geolocator is created with a user-defined user agent "location_app", A while loop is used to continuously prompt the user to enter their location until a valid location is provided. Inside the loop, the user is asked to enter their location (e.g., city, country), and the geolocator.geocode method is used to get the GPS coordinates based on this input.
3) The if name == "main": block is used to call the location_of_the_user function when the script is executed directly. This ensures that the code inside the if block is executed only when the script is run as the main program. The code then, terminates.

OUTPUT:

![Screenshot (5)](https://github.com/Gnanapriya177/TAI-IP/assets/133194111/a2596b67-9715-4907-b3bf-195ddb298bfc)

Level-3_Task-2_Payment_Application:

Description:
The code defines a payment function that simulates processing of the payment and prints the output.
1) The main_function() prompts the user to enter the payment amount.
2) If the amount entered is not a positive integer a value error is raised and the payment fails, otherwise the payment is successful and the code terminates.

OUTPUT:

![Screenshot (6)](https://github.com/Gnanapriya177/TAI-IP/assets/133194111/61b11901-b107-429c-9c99-b6d21c513872)

Level-3_Task-3_Speech_Recognition:

Description:
1) Firstly import the library speech_recognition.
2) We use a function called the Recognizer() to recognize the speech of the user.
3) The output is printed on the screen and if audio can't be recognized then an error occurs. The code terminates.

OUTPUT:

![Screenshot (7)](https://github.com/Gnanapriya177/TAI-IP/assets/133194111/31b2490f-0b2f-4ac9-a692-4943cd15b2b4)







