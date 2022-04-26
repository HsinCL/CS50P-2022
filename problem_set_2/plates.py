def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # All vanity plates must start with at least two letters.
    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    # Numbers cannot be used in the middle of a plate; they must come at the end. 
    # The first number used cannot be a ‘0’.”
    # No periods, spaces, or punctuation marks are allowed.

    start_with_at_least_two_letters = True
    maximum_6_minimum_2_characters = True
    number_cannot_be_used_in_the_middle = True
    the_first_number_used_cannot_be_0 = True
    no_space_and_punctuation_marks = True



    #if (len(s)<2) or (len(s)>6):
    #    return False
    maximum_6_minimum_2_characters = not((len(s)<2) or (len(s)>6))
    if maximum_6_minimum_2_characters:
        first_letter = (65 <= ord(s[0]) <= 90) or (97 <= ord(s[0]) <= 122)
        second_letter = (65 <= ord(s[1]) <= 90) or (97 <= ord(s[1]) <= 122)
        start_with_at_least_two_letters = first_letter and second_letter

    valid = (maximum_6_minimum_2_characters and start_with_at_least_two_letters and
    number_cannot_be_used_in_the_middle and the_first_number_used_cannot_be_0 and no_space_and_punctuation_marks)

    i = 0
    start_number = False
    while (valid and (i < len(s))):
        ch_ascii = ord(s[i])

        no_space_and_punctuation_marks = (ch_ascii in range(65, 65+26)) or (ch_ascii in range(97, 97+26)) or (ch_ascii in range(48, 48+10))
        if (start_number == False) and (ch_ascii in range(48, 48+10)):
            the_first_number_used_cannot_be_0 = (not (s[i] == '0'))
            start_number = True
        if ((ch_ascii in range(65, 65+26)) or (ch_ascii in range(97, 97+26))) and (start_number == True):
            number_cannot_be_used_in_the_middle = False

        valid = (maximum_6_minimum_2_characters and start_with_at_least_two_letters and 
        number_cannot_be_used_in_the_middle and the_first_number_used_cannot_be_0 and no_space_and_punctuation_marks)

        i = i + 1
    return valid
    """
    if start_with_at_least_two_latters:

        start_number = False
        valid_count = 0
        for i in range(len(s)):
            ch_ascii = ord(s[i])
            no_space_and_punctuation_marks = (ch_ascii in range(65, 65+26)) or (ch_ascii in range(97, 97+26)) or (ch_ascii in range(48, 48+10))
            if no_space_and_punctuation_marks:
                if ch_ascii in range(48, 48+10):
                    
                    if (not start_number) and (s[i] == '0'):
                        return False
                    else:
                        start_number = True
                else:
                    if start_number == True:
                        return False
                    else:
                        print(valid_count)
                        valid_count = valid_count + 1

            else:
                return False

        return valid_count == len(s)

    else:
        return False
    """
   

    



main()