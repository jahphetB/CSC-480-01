import os 
import os.path
import re

def find_tar(con):
    sentences = re.split(r'[.!?]', con)  
    collector = [] 
    print(sentences)
    count = 1  
    for sentence in sentences:
        for word in query.split():  
            word = word.strip('+').strip()  
            if word in sentence:  # Check if the word appears in the sentence
                # Ensure that the word appears with its proper logic/regex in the query
                if word.startswith('+'):  
                    if word[1:] in sentence:
                        collector.append((sentence.strip(), count))  
                elif word.startswith('(') and word.endswith(')'):  
                    words_in_parens = word[1:-1].split()  
                    if any(w in sentence for w in words_in_parens):  
                        collector.append((sentence.strip(), count))  
                elif word not in sentence:  
                    continue  
        count += 1  
    print("Collected Sentences:", collector)


def read_file(file_path):
    try:
        with open(file_path, 'r') as con:

            content = con.read()
            find_tar(content)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

def search(current_path):
    items = os.listdir(current_path)
    for i in items:
        full_path = os.path.join(current_path, i)
        if os.path.isdir(full_path):
            print(f"Directory found: {full_path}")
            search(full_path)
        elif os.path.isfile(full_path):
            print(f"File found: {full_path}")
            read_file(full_path)

path = input("enter path of the directory: ")
query = input("enter your query: ")
items_in_cwd = os.listdir(path)
search(path)
