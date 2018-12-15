import os, re
files_list = []
sections_list = {}
season = []
title = []

for i in range(8):
    files_list.append([])
    for filename in os.listdir("."):
        if filename.startswith("video" + str(i+1)):
            files_list[i].append(filename)

with open("section_names") as f:
    season = []
    show_title = []
    for line in f:
        if line.startswith("Section"):
            temp_season, temp_season_title = (line.split(":"))
            season.append(temp_season_title.strip())
            #sections_list.update({key : []})
            #section = key[8]
            #print(section)        
            print(len(season))    
        elif line.startswith(str(len(season))):
            temp_number, temp_show_title = line.split(" ", 1)
            print(temp_number + " . . . *" + temp_show_title + "*")
                          

'''
for item in files_list:
    print(item)

for key in sections_list:
    print(key + ". . . " + value)

'''