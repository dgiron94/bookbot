
def get_lines_from_text(fpath):
    with open(fpath) as f:
        return f.readlines() 

def get_contents_from_text(fpath):
    with open(fpath) as f:
        return f.read() 
def count_characters_in_string(s):
    characters = dict()
    for c in s.lower():
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] = characters[c] + 1

    characterList = [] 
    for l in characters:
        characterList.append({ "letter" : l , "count": characters[l] })

    return characterList


def sort_on(c):
    return c["count"]

def main():
    frankensteinContents = get_contents_from_text("books/frankenstein.txt")
    print('--- Begin report of books/frankenstein.txt ---')
    print(str(len(frankensteinContents.split())) + " words found in the document")
    print()
    characterList = count_characters_in_string(frankensteinContents)
    characterList.sort(reverse=True, key=sort_on)
    for c in characterList:
        if c['letter'].isalpha():
            print(f"The '{c['letter']}' character was found {c['count']} times")

main()
