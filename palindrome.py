# user_input = input("Enter 5 words separated by only a comma:\r\n")
# word_list = user_input.split(',')
# print(word_list)
# for word in word_list:
#     if word == word[ : : -1]:
#         print(f"{word} is a palindrome")


# advanced palindrome check

def make_lower_and_list():
    user_input = input("Enter a word, phrase or sentence to check if it is a palindrome:\r\n")
    lowered_input = user_input.lower()
    lowered_list = list(lowered_input)
    return lowered_list

def remove_spaces_and_punctuations(lowered_list):
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]     
    for i in lowered_list:
        if i in analphabeticList:
            lowered_list.remove(i)
    return lowered_list        

def check_palindrome(normal_list):
    if normal_list == normal_list[ : : -1]:
        print(f"The text is a palindrome")
    else:
        print(f"The text is not a palindrome")    

def main():
    my_list = make_lower_and_list()        
    new_list = remove_spaces_and_punctuations(my_list)
    pal_check = check_palindrome(new_list)

main()
