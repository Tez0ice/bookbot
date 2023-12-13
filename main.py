def main():
    books_path = "./books/frankestein.txt"
    content = get_book_contents(books_path)
    content_length = get_words_length(content)
    char_count = get_char_count(content)
    char_summarization = get_char_summary(char_count)

   
    print(f"--- Begin report of {books_path} ---")
    print(f"Number of words found {content_length}")
    print()
    for dict in char_summarization:
        print(f"The {dict['char']} character was found {dict['count']} times")
    print()
    print("--- End Report ---")

def get_words_length(text):
    ls_words = text.split()
    return(len(ls_words))

def get_char_count(text):
    unique_chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in unique_chars:
            unique_chars[lowered] += 1
        else:
            unique_chars[lowered] = 1
    return unique_chars

def sort_based_on(dict):
    return dict["count"] # sort based on the count 

def get_char_summary(char_count):
    char_list = []
    for char in char_count:
        if char.isalpha():
            char_list.append({"char":char,"count":char_count[char]})
    char_list.sort(reverse=True,key=sort_based_on) #function refer i think?? //key accept function that will do operation for each individual item on the list and then use that return value for operation
    return char_list

def get_book_contents(books_path):
    with open(books_path) as file:
        return file.read()

main()