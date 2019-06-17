import re
import argparse

def main() :
    parser = argparse.ArgumentParser()
    input_group = parser.add_mutually_exclusive_group()

    input_group.add_argument('-t', '--text', type=str, help='text to be searched')
    input_group.add_argument('-f', dest="filename", type=argparse.FileType('r'), help='file to be searched')

    args = parser.parse_args()
    # REGEX = "\+[-()\s\d]+?(?=\s*[+<])"
    # REGEX = ".*?\(\\(?\d{3}\\)? ?[\.-]? ?\d{3} ?[\.-]? ?\d{4}\).*?"
    REGEX = re.compile("[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*[0-9]")

    text = ''

    if args.filename is not None :
        print("Parsing file " + str(args.filename.name) + "...")

        with open(args.filename.name, encoding='utf8') as f:
            text = f.read().strip()

    elif args.text is not None :
        text = args.text

    extract_phonenumbers(text, REGEX)


def extract_phonenumbers(line, regex):
    numbers = re.findall(regex, line)
    print(numbers) if len(numbers) > 0 else print('nothing')

if __name__ == '__main__':
    main()