def open_book(book_path):
    # Simple file Opener
    with open(book_path) as f:
        file_content = f.read()
        return file_content

def word_counter(book):
    # We use split to delete all blank spaces
    words = book.split()
    words = len(words)
    return words

def character_counter(book):
    # Import our Book and make all chars to lower case
    book = book.lower()

    # We make a dictionary including all alphabet chars
    alphabet = {
            'a' : 0,
            'b' : 0,
            'c' : 0,
            'd' : 0,
            'f' : 0,
            'g' : 0,
            'h' : 0,
            'i' : 0,
            'j' : 0,
            'k' : 0,
            'l' : 0,
            'm' : 0,
            'n' : 0,
            'o' : 0,
            'p' : 0,
            'q' : 0,
            'r' : 0,
            's' : 0,
            't' : 0,
            'u' : 0,
            'v' : 0,
            'w' : 0,
            'x' : 0,
            'y' : 0,
            'z' : 0,
            }

    for words in book:
        for char in words:
            if char == 'a':
                alphabet['a'] += 1
            elif char == 'b':
                alphabet['b'] += 1
            elif char == 'c':
                alphabet['c'] += 1
            elif char == 'd':
                alphabet['d'] += 1
            elif char == 'f':
                alphabet['f'] += 1
            elif char == 'g':
                alphabet['g'] += 1
            elif char == 'h':
                alphabet['h'] += 1
            elif char == 'i':
                alphabet['i'] += 1
            elif char == 'j':
                alphabet['j'] += 1
            elif char == 'k':
                alphabet['k'] += 1
            elif char == 'l':
                alphabet['l'] += 1
            elif char == 'm':
                alphabet['m'] += 1
            elif char == 'n':
                alphabet['n'] += 1
            elif char == 'o':
                alphabet['o'] += 1
            elif char == 'p':
                alphabet['p'] += 1
            elif char == 'q':
                alphabet['q'] += 1
            elif char == 'r':
                alphabet['r'] += 1
            elif char == 's':
                alphabet['s'] += 1
            elif char == 't':
                alphabet['t'] += 1
            elif char == 'u':
                alphabet['u'] += 1
            elif char == 'v':
                alphabet['v'] += 1
            elif char == 'w':
                alphabet['w'] += 1
            elif char == 'x':
                alphabet['x'] += 1
            elif char == 'y':
                alphabet['y'] += 1
            elif char == 'z':
                alphabet['z'] += 1
            
    return alphabet



def generate_report(book_path):
    book = open_book(book_path)
    words = word_counter(book)
    letter = character_counter(book)

    # Report:
    print("--- Report of book ---")
    print(f"{words} words found in the document")
    for l in letter:
        char_num = letter[l]
        print(f"The {l} character was found {char_num} times")
    
    print("--- End Report ---")

generate_report("./books/frankenstein.txt")




