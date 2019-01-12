import os
import re
import sys
from docx import Document

docx_in = "masteringlinuxsecurityandhardening.docx"
text_data_in = "show_data.txt"
show_data = {}

def open_docx(docx_in):
    try:
        document = Document(docx_in)
        return document
    except Exception as err:
        sys.exit(f"Error loaking docx file: {err}" )



def get_text(document):
    """returns array of string values of each paragraph of text from docx file"""
    #try: 
    text_lines = []
    for para in document.paragraphs:
        if para.paragraph_format.alignment==1:
            (para.text)
        text_lines.append(para.text)
    print("Successfully read .docx file")    
    return text_lines
    #except document.para as e:
    #    print(e)


def get_show_title(text_in):
    show_title = {"show_title":text_in[0]}
    return show_title

document = open_docx(docx_in) #open docx file
text_in = get_text(document)

#for item in text_in:
#    print(str(type(item)) + " . . . " + item)
print(text_in[0])
show_data.update(get_show_title(text_in))
if show_data["show_title"] == text_in[0]:
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