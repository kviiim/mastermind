import random

turn = 1
number_turns = 6
pattern_length = 4
pattern = ""
for letter in range(pattern_length):
    pattern += str(chr(random.randint(97,101)))

print("welcome to mastermind")
print("guess the 4 digit code in ten guesses")
print("each letter is a color in the game mastermind")
print("a '0' back means a right color in the right spot")
print("a '1' back means a right color in the wrong spot")
print("you will get a combination of 0s and 1s in response to each guess")

guess_pattern = input("input a 4 letter code using a-e: ")

while turn < number_turns and guess_pattern != pattern:
    #find black
    output_sting = ''
    white_potential = {}
    white_potential_actual = []
    for letter_index in range(len(guess_pattern)):
        if guess_pattern[letter_index] == pattern[letter_index]:
            output_sting += '0'
        else:
            white_potential_actual += pattern[letter_index]
            letter = guess_pattern[letter_index]
            try:
                white_potential[letter] += 1
            except:
                white_potential[letter] = 1
    #find white
    for letter in white_potential.keys():
        if white_potential_actual.count(letter) >= white_potential[letter]:
            output_sting += (white_potential[letter] * '1')
        else:
            output_sting += (white_potential_actual.count(letter) * '1')
    print(f"output: {output_sting}")
    guess_pattern = input("input a new guess: ")
    turn += 1

if number_turns == turn:
    print(f'you lose, the pattern was {pattern}')
else:
    print('congrats u won')