def sort_on(dict):
    return dict["count"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        
        #print(file_contents)

        words = file_contents.split()
        print(f"{len(words)}")

        charDictionary = {}
        for character in file_contents:
            if character.isalnum():
                if character in charDictionary :
                    charDictionary[character] += 1
                else:
                    charDictionary[character] = 1

        list_of_dictionaries = []
        for record in charDictionary:
            dictionary = {}
            dictionary["char"] = record
            dictionary["count"] = charDictionary[record]
            list_of_dictionaries.append(dictionary)

        list_of_dictionaries.sort(reverse=True, key=sort_on)

        print(f"{list_of_dictionaries}")

        #print(f"{charDictionary}")



main()