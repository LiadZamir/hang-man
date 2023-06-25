HANGMAN_ASCII_ART = r"""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6
NUM_OF_TRIES = 0
HANGMAN_PHOTOS = {
0: """
x-------x""",
1: """
x-------x
|
|
|
|
|""",
2: """
x-------x
|       |
|       0
|
|
|""",
3: """
x-------x
|       |
|       0
|       |
|
|""",
4: """
x-------x
|       |
|       0
|      /|\ 
|
|""",
5: """
x-------x
|       |
|       0
|      /|\ 
|      /
|""",
6: """
x-------x
|       |
|       0
|      /|\ 
|      / \ 
|"""}


def open_screen():
    print(HANGMAN_ASCII_ART + '\n' + str(MAX_TRIES))
    return None


def choose_word(file_path, index):
    with open(file_path, 'r') as words_file:
        words = words_file.read()
    words = words.split()
    length_of_words = len(words)
    while index > length_of_words:
        index -= length_of_words
    word = words[index - 1]
    return word.lower()


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    The function checks the correctness of the received character.
    :param The signal guessed.
    :type string
    :param old_letters_guessed: List of guessed letters.
    :type old_letters_guessed: list
    :return: True/False
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    check_user_input_letter = letter_guessed.isalpha()
    if letter_guessed in old_letters_guessed:
        return False
    elif len(letter_guessed) > 1 or not check_user_input_letter:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    """this function get a letter from the user and a list of letter that the user already guessed,
    and check's if the letter is new it will append the letter to the list of the letter allredy guessed and print 'X' and under the list of letter that guessed with -> between them
    :param letter_guessed: letter from the user
    :param old_letter_guessed: list of letter allredy guessed
    :type letter_guessed: string
    :type old_letter_guessed: list
    :return: true or false
    :rtype: bool"""
    global NUM_OF_TRIES
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        old_letters_guessed.sort()
        print(" -> ".join(old_letters_guessed))
    else:
        if letter_guessed.lower() not in secret_word:
            old_letters_guessed.append(letter_guessed.lower())
            NUM_OF_TRIES += 1
            print(':(')
            print(print_status())
            print(show_hidden_word(secret_word, old_letters_guessed))
        else:
            old_letters_guessed.append(letter_guessed.lower())
            print(show_hidden_word(secret_word, old_letters_guessed))


def show_hidden_word(secret_word, old_letters_guessed):
    """
    The function return string that displays the correct letters guessed in their appropriate place.
    :param secret_word: The word to guess.
    :type secret_word: string
    :param old_letters_guessed: List of guessed letters.
    :type old_letters_guessed: list
    :return my_str: The words guessed in their proper place
    :rtype: string
    """
    my_str = ["_"] * len(secret_word)
    for x in old_letters_guessed:
        for t in range(0, len(secret_word)):
            if x == secret_word[t]:
                my_str[t] = x
    my_str = ' '.join(my_str)
    return my_str


def check_win(secret_word, old_letters_guessed):
    my_str = ["_"] * len(secret_word)
    for x in old_letters_guessed:
        for t in range(0, len(secret_word)):
            if x == secret_word[t]:
                my_str[t] = x
    my_str = ''.join(my_str)
    if my_str == secret_word:
        return True
    else:
        return False


def print_status():
    global NUM_OF_TRIES
    return HANGMAN_PHOTOS[NUM_OF_TRIES]


def main():
    global NUM_OF_TRIES
    open_screen()
    secret_word = choose_word(input(r"Please enter file path: ").lower(), int(input(r"Please enter index: ")))
    old_letters_guessed = []

    print('\nLets start!')
    print(HANGMAN_PHOTOS[NUM_OF_TRIES])
    print(show_hidden_word(secret_word, old_letters_guessed))

    while NUM_OF_TRIES < MAX_TRIES:
        try_update_letter_guessed(input('Enter a letter: '), old_letters_guessed, secret_word)
        show_hidden_word(secret_word, old_letters_guessed)
        game_status = check_win(secret_word, old_letters_guessed)
        if game_status:
            print('WIN')
            break

    if not game_status:
        print('LOSE')


if __name__ == '__main__':
    main()