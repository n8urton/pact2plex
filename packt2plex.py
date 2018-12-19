import os, re
old_filenames = []
new_filenames = {}

for i in range(8):
    old_filenames.append([])
    for filename in os.listdir("."):
        if filename.startswith("video" + str(i+1)):
            old_filenames[i].append(filename)

with open("section_names") as f:
    for line in f:
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
