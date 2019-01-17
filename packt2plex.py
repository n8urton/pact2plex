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
        print(f"Opening {docx_in}")
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
    '''returns an array of key value pairs with keys "season_title": <text
from each paragraph object starting with the string "Section">''' 
    season_count=0
    season_data = []
    for para in document.paragraphs:
        if para.text.startswith("Section"):
            season_title = {"season_title" : (para.text.split(":")[1]).strip()}
            season_data.append(season_title)
            season_count += 1
    return season_data


def get_episode_titles(document, season_num):
    '''returns array of dicts containing "new_name" : <text from each paragaph
object starting with the number of specified season>'''
    episode_data = []
    for para in document.paragraphs:
        if para.text.startswith(str(season_num)):
            episode_title = {"new_name" : (para.text.split(" ", 1)[1]).strip()}
            episode_data.append(episode_title)
    return episode_data


def get_file_names(season):
    file_data = []
    for filename in os.listdir("."):
        if filename.startswith("video" + str(season)):
            old_name = {"old_name" : filename}
            file_data.append(old_name)
    return file_data


def merge(filenames, episode_titles):
    '''merges two arrays of key value pairs into one array with 2 key value pairs per index'''
    if len(filenames) == len(episode_titles):
        merge_data = []
        for enum, file_data in enumerate(filenames):
            episodes = episode_titles[enum]
            title_data = ({key:episodes[key] for key in episodes})
            merge_data.append(title_data)
            merge_data[enum].update(file_data)
        return merge_data
    else:
        sys.exit("Error matching filenames to episodes")

document = open_docx(docx_in)

show_data.update(get_show_title(document))
show_data.update({"seasons" : get_season_titles(document)})

for season, titles in enumerate(show_data["seasons"]):
    current_season = show_data["seasons"][season]
    episode_titles = get_episode_titles(document, season+1)
    filenames = get_file_names(season+1)
    episode_data_merge = merge(filenames, episode_titles)
    current_season.update({"episode":episode_data_merge})

pprint(show_data)