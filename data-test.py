import json

show_title = "Mastering Linux Security and Hardening"

with open('test_data_struct.json') as infile:
    data = json.load(infile)
# print(data)
print(show_title)
for season_num, season in enumerate(data, start=1):
    title = season["title"]
    print(f"\tSeason {season_num} - {title}")
    for episode_num, episode in (enumerate(season["episode"], start=1)):
        old_name, new_name = episode["old_name"], episode["new_name"]
        print(f"\t\t{old_name} . . . {show_title} - s{season_num:02}e{episode_num:02} - {new_name}")