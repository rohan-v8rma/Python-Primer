import re

def print_matched_substrings(regex_object, text):
    matches = regex_object.finditer(text)
    print("\nThe matches are:\n")
    for match in matches:
        print(f'----> {text[match.start():match.end()]}')
    print('\n')
    
def main():
    file_handle = open(r"C:\Users\rverm\Dropbox\Shared\Computer_code\Python\Modules\Regular_expressions.py\random_text.txt", 'r')
    text = file_handle.read()

    regex_object_num = re.compile(r'([+]\d{2}[-]?)?\d{10}')
    regex_object_email = re.compile(r"[a-zA-Z][\w.-]+[@][a-zA-Z-]+([.][a-zA-Z]+)*")
    regex_object_url = re.compile(r"https?://(www[.])?\w+([.]\w+)*[a-zA-Z]")

    option = input('''
    What do you want?
    1. Phone numbers
    2. Email addresses
    3. URLs
    Enter the option ---> ''')
    if option == '1':
        print_matched_substrings(regex_object_num, text)
    elif option == '2':
        print_matched_substrings(regex_object_email, text)    
    else:
        print_matched_substrings(regex_object_url, text)

main()

