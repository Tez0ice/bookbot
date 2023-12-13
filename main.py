def main():
    books_path = "./books/frankestein.txt"
    content = get_book_contents(books_path)
    print(content)

def get_book_contents(books_path):
    with open(books_path) as file:
        return file.read()

main()