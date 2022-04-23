def convert(sentence):
        convert_sentence = sentence.replace(":)", "\N{slightly smiling face}")
        convert_sentence = convert_sentence.replace(":(", "\N{slightly frowning face}")
        print(convert_sentence)


def main():
    sentence = input("Input something with emoji: ")
    convert(sentence)


main()