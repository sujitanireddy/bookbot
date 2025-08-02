#Function that accpets the text from the book as a string
def count_words(contents_of_file_to_string):
    words_list = contents_of_file_to_string.split()
    print(f'Found {len(words_list)} total words')

#Function to count characters and save it in a dictonary
def count_characters(contents_of_file_to_string):
    final_counts = {}
    counter = 0
    for letter in contents_of_file_to_string:
        lower_letter = letter.lower()
        if lower_letter in final_counts:
            final_counts[lower_letter] = final_counts[lower_letter] + 1
        else:
            final_counts[lower_letter] = counter + 1
    return final_counts

#helper function for sorting based on count
def sort_on(final_character_counts_dict):
        return final_character_counts_dict["num"]

#Function to sort the dictnary
def sorted_dict(final_counts):
    new_sorted_list = []
    for char, num in final_counts.items():
        new_sorted_dict = {}
        new_sorted_dict["char"] = char
        new_sorted_dict["num"] = num
        new_sorted_list.append(new_sorted_dict)
    new_sorted_list.sort(reverse=True, key = sort_on)
    return new_sorted_list