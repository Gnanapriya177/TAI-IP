odd_digit_sum = 0
even_digit_sum = 0
total = 0

card_number = input("Enter a credit card number: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

for i in card_number[::2]:
    odd_digit_sum += int(i)

for i in card_number[1::2]:
    i = int(i)*2
    if i >= 10:
        even_digit_sum += 1+(i%10)
    else:
        even_digit_sum += i

total = odd_digit_sum + even_digit_sum

if total % 10 == 0:
    print("Valid Credit Card Number")
else:
    print("Invalid Credit Card Number")
