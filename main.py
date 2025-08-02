import sys

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import count_words, count_characters, sorted_dict

#Function to open the file and return the contents of the file as a string
def get_book_test(file_path):
    with open(file_path) as f:
        contents_of_file = f.read()
    return contents_of_file


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    contents_of_file_to_string = get_book_test(sys.argv[1])
    count_words(contents_of_file_to_string)
    print("--------- Character Count -------")
    final_character_counts_dict = count_characters(contents_of_file_to_string)
    final_sorted_list = sorted_dict(final_character_counts_dict)
    for item in final_sorted_list:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()