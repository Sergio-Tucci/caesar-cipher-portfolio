import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Main Caesar cipher function definition receiving 3 parameters
def caesar(original_text, shift_amount, encode_or_decode): # function receiving 3 parameters
    # Initialize empty string to store the processed result
    output_text = ""
    # For decoding, reverse the shift direction (move backward in alphabet)
    if encode_or_decode == "decode":
        shift_amount *= -1
    # Iterate through each character in the input text
    for letter in original_text:
        # Check if character is not in our alphabet (spaces, punctuation, numbers)
        if letter not in alphabet:
            output_text += letter # Keep non-alphabet characters unchanged
        else:
            # Find the current position of the letter in the alphabet list
            shifted_position = alphabet.index(letter) + shift_amount
            # This handles shifts that exceed the alphabet length
            shifted_position %= len(alphabet)
            # Get the new letter from calculated position and add to output
            output_text += alphabet[shifted_position]
    # Display the final result to the user
    print(f"Here is the {encode_or_decode}d result: {output_text}")

#control variable for the main program looping
should_continue = True
# loop keep running until user choses to exit
while should_continue:
    # ask a user direction type
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # validates if user has chosen between the two options
    if direction != "encode" and direction != "decode":
        print("Please type 'encode' or 'decode'")
        # skip the rest of the code and ask again until choose between the two options
        continue
    # user input the message want to be modified and convert to lowercase
    text = input("Type your message:\n").lower()
    # user input number of shift wanted and convert to integer
    shift = int(input("Type the shift number:\n"))

    #call the function passing parameters
    caesar(text, shift, direction)
    # ask user if they wanto to continue or exit
    restart = input("type `yes` if you want to continue and `no` if you want to exit. \n").lower()
    # validate user answer
    if restart == "no":
        # change control variable value to false breaking while loop
        should_continue = False
        print("good bye") # exit message
