import os
import re
import sys
from docx import Document
from pprint import pprint

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
    '''returns the text from the first center formatted paragraph object in 
the docx file the key of "show_title"'''
    for para in document.paragraphs:
        if para.paragraph_format.alignment==1:
            data= {"show_title" : para.text}
            print("Setting Show Title to: {0}".format(data["show_title"]))
            return data
        else:
            print("No show title found")


def get_season_titles(document):
    '''returns an array of key value pairs with keys "title": <text
from each paragraph object starting with the string "Section">''' 
    season_count=0
    season_data = []
    for para in document.paragraphs:
        if para.text.startswith("Section"):
            season_title = {"title" : (para.text.split(":")[1]).strip()}
            #season_title = {"title" : season_title.strip()}
            season_data.append(season_title)
            season_count += 1
        #elif para.text.startswith(str(season_count)):
        #    season_data[season_count].update(para.text)
    return season_data


def get_episode_titles(document, season_num):
    '''returns array of dicts containing "new_name" : <text from each paragaph
object starting with the number of specified season>'''
    season_data = []
    for para in document.paragraphs:
        if para.text.startswith(str(season_num)):
            episode_title = {"new_name" : (para.text.split(" ", 1)[1]).strip()}
            season_data.append(episode_title)
    
    return season_data


def get_file_names(season):





document = open_docx(docx_in) #open docx file
#text_in = get_text(document)

#for item in text_in:
#    print(str(type(item)) + " . . . " + item)
#print(f"data is: \n{}")
show_data.update(get_show_title(document))
show_data.update({"seasons" : get_season_titles(document)})
for season, titles in enumerate(show_data["seasons"]):
    show_data["seasons"][season].update({"episode" : \
get_episode_titles(document, season+1)})




pprint(show_data)
'''
for i in range(8):
    old_filenames.append([])
    for filename in os.listdir("."):
        if filename.startswith("video" + str(i+1)):
            old_filenames[i].append(filename)
"""