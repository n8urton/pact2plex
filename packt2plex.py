import os
import sys
from docx import Document
from pprint import pprint
import json
import time


def main():    
    docx_in = 'masteringlinuxsecurityandhardening.docx'
    show_data = {}

    document = open_docx(docx_in)

    show_data.update(get_show_title(document))
    show_data.update({"seasons" : get_season_titles(document)})

    for season, titles in enumerate(show_data["seasons"]):
        current_season = show_data["seasons"][season]
        episode_titles = get_episode_titles(document, season+1)
        filenames = get_file_names(season+1)
        episode_data_merge = merge(filenames, episode_titles, show_data["show_title"], season + 1)
        current_season.update({"episode":episode_data_merge})
    save_show_data(show_data)
    pprint(show_data)


def open_docx(docx_in):
    try:
        document = Document(docx_in)
        print(f'Opening {docx_in}')
        return document
    except Exception as err:
        sys.exit(f'Error loading docx file: {err}')



def get_show_title(document):
    '''returns the text from the first center formatted paragraph object in 
the docx file the key of "show_title"'''
    for para in document.paragraphs:
        if para.paragraph_format.alignment==1:
            data= {"show_title" : para.text}
            print('Setting Show Title to: {0}'.format(data["show_title"]))
            return data
        else:
            print('No show title found')


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


def merge(filenames, episode_titles, sh_title, seas_num):
    '''merges two arrays of key value pairs into one array with 2 key value pairs per index'''
    if len(filenames) == len(episode_titles):
        merge_data = []
        for enum, file_data in enumerate(filenames):
            episode = episode_titles[enum]
            ep_num = enum +1 
            ep_name = str(episode["new_name"])
            new_filename = f"{sh_title} - s{seas_num:02}e{ep_num:02} - {ep_name}"
            title_data = ({key:episode[key] for key in episode})
            merge_data.append(file_data)
            merge_data[enum].update({"new_name" : new_filename})
        return merge_data
    else:
        sys.exit('Error matching filenames to episodes')


def save_show_data(show_data):
    '''exports show_data to <show_title><timestamp>.json file'''
    timestr = time.strftime("%Y%m%d-%H%M%S")
    title_4_file = show_data["show_title"].replace(" ", "_")
    file_out = f'{title_4_file}{timestr}.json'
    with open(file_out, 'w') as fout:
        json.dump(show_data, fout)
    

if __name__ == "__main__":
    main()