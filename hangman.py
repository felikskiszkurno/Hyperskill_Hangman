# import packages
import random

# Main game structure
print('H A N G M A N')
menu_choice = input('Type "play" to play the game, "exit" to quit: ')
print('')
if menu_choice == 'play':
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word_selector = random.randint(0, len(word_list) - 1)
    word_selected = word_list[word_selector]
    word_selected_list = list(word_selected)
    word_selected_set = set(word_selected)
    word_selected_hint = list('-' * len(word_selected))
    word_selected_list_set = set(word_selected_hint)
    guessed = False
    tries = 8
    guessed_letters_set = set()
    while tries > 0:
        word_selected_list_set = set(word_selected_hint)
        print(''.join(word_selected_hint))
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print('You should input a single letter\n')
            continue
        elif letter.islower() is False:
            print('It is not an ASCII lowercase letter\n')
            continue
        # print(word_selected_list_set)
        if letter in word_selected_set:
            if letter not in guessed_letters_set:
                guessed_letters_set.add(letter)
                for character_id in range(len(word_selected_list)):
                    if word_selected_list[character_id] is letter:
                        word_selected_hint[character_id] = letter
                print('')
                if '-' not in word_selected_hint:
                    if tries > 0:
                        print(''.join(word_selected_hint))
                        print('You guessed the word!')
                        print('You survived!')
                        break
                    elif tries == 0:
                        print('You are hanged!')
            else:
                guessed_letters_set.add(letter)
                if tries == 0:
                    print('You already typed this letter')
                else:
                    print('You already typed this letter\n')
        else:
            if letter in guessed_letters_set:
                print('You already typed this letter\n')
            else:
                guessed_letters_set.add(letter)
                tries -= 1
                if tries < 1:
                    print('No such letter in the word')
                    break
                else:
                    print('No such letter in the word\n')
    if tries == 0:
        print('You are hanged!')
elif menu_choice == 'exit':
    exit()