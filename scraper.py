# scraper
import praw
import emoji
from string import punctuation
import json

global big_emoji_list


# from Curtis Lusmore on Quora https://www.quora.com/How-do-I-remove-punctuation-from-a-Python-string
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def add_emoji_to_dict(word, emj):
    global big_emoji_list

    word = strip_punctuation(word.lower())
    emj = emoji.demojize(emj)
    print("Adding an emoji {} for the word {}".format(emj, word))
    for i in big_emoji_list:
        print("{} vs {}".format(emj, i["emoji"]))
        if i["emoji"] == emj: print("SAME EMOJI")

        if i["emoji"] == emj and word not in i["meanings"]:
            i["meanings"].append(word)
            return
        elif i["emoji"] == emj and word in i["meanings"]:
            return

    big_emoji_list.append({"emoji": emj, "meanings": [word]})


big_emoji_list = []

emoji_list_format = [
    {"emoji": "😎",
    "meanings": [
        "cool",
        "rad"
    ]}
]

with open("reddit_secret", "r") as sec:
    secret = sec.read()

reddit = praw.Reddit(client_id='R8tA-6j8rVLojg',
                     client_secret=secret,
                     user_agent='emojipastainator')

count = 1
for post in reddit.subreddit('emojipasta').search('self:yes', sort="top", time_filter="all"):

    print("POST #{}".format(count))
    list_of_emojis = emoji.emoji_lis(post.selftext)

    for emoji_instance in list_of_emojis:
        string_ending_with_emoji = post.selftext[0:emoji_instance["location"]]
        try:
            if len(string_ending_with_emoji):
                last_word_in_string = string_ending_with_emoji.split()[-1]
                if emoji.emoji_count(last_word_in_string) == 0:
                    # print("{} goes with {}".format(last_word_in_string, emoji_instance["emoji"]))

                    add_emoji_to_dict(last_word_in_string, emoji_instance["emoji"])
        except:
            continue

    count += 1

    if count > 50:
        break
    print('\n')

print(big_emoji_list)

with open("emoji_meanings.json", "w") as f:
    json.dump(big_emoji_list, f)
