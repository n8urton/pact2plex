import os
import re
from docx import Document

docx_in = "masteringlinuxsecurityandhardening.docx"
text_data_in = "show_data.txt"


def get_text(document):
    """returns array of string values of each paragraph of text from docx file"""
    text_lines = []
    for para in document.paragraphs:
        if para.paragraph_format.alignment==1:
            (para.text)
        text_lines.append(para.text)
    return text_lines


document = Document(docx_in) #open docx file
text_in = get_text(document)

#for item in text_in:
#    print(str(type(item)) + " . . . " + item)
print(text_in[0])

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