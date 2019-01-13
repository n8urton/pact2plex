import os
import re
import sys
from docx import Document
test_show_title = "Mastering Linux Security and Hardening"
docx_in = "masteringlinuxsecurityandhardening.docx"
text_data_in = "show_data.txt"
show_data = {}

def open_docx(docx_in):
    try:
        document = Document(docx_in)
        print(f". . . Opening {docx_in}")
        return document
    except Exception as err:
        sys.exit(f"Error loading docx file: {err}" )



def get_show_title(document):
    '''returns the text from the first center formatted paragraph object in the docx file the key of "show_title"'''
    for para in document.paragraphs: #iterates through paraghraphs
        print(para.text)
        try: 
            if para.paragraph_format.alignment==1: # 
                print(para.text)
                data= {"show_title" : para.text}
                print("Setting Show Title to: {0}".format(data["show_title"]))
                return data
            else:
                print("No show title found")
        except TypeError:
            sys.exit(f"Error reading Show Title from {docx_in}. Show \
Title should be the first CENTER FORMATTED line in the document")


#def get_season_titles(document):



document = open_docx(docx_in) #open docx file
#text_in = get_text(document)

#for item in text_in:
#    print(str(type(item)) + " . . . " + item)
#print(f"data is: \n{}")
show_data.update(get_show_title(document))
if test_show_title == show_data["show_title"]:
    print("correct title")
else:
    print("try again")


old_filenames = []
new_filenames = {}
"""
for i in range(8):
    old_filenames.append([])
    for filename in os.listdir("."):
        if filename.startswith("video" + str(i+1)):
            old_filenames[i].append(filename)

with open(text_data_in) as infile:
    for line in infile:
        if line.startswith("Section"):
            season_title = (line.split(":")[1])
            season_title = season_title.strip()
            new_filenames[season_title] = []
            # print(len(new_filenames))
        elif line.startswith(str(len(new_filenames))):
            show_title = line.split(" ", 1)[1]
            # print(new_filenames[(len(new_filenames)-1)] +
            #       " . . . *" + show_title + "*")
            new_filenames[season_title.strip()].append(show_title.strip())
            

for enum, season in enumerate(new_filenames):
    print("Season " + (str(enum+1)) + ": " + season)
    for count, episode in enumerate(new_filenames[season]):
        print(old_filenames[enum][count] + " . . . " + episode)
"""
"""
with open(text_data_in) as infile:
    for line in infile:
        print(line)


print(data)
"""