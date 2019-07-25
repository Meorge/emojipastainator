# scraper
import praw
import emoji
from string import punctuation
import json
import sys
from nltk.stem import *

global big_emoji_list, stemmer


# from Curtis Lusmore on Quora https://www.quora.com/How-do-I-remove-punctuation-from-a-Python-string
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

# from emile on stackoverflow https://stackoverflow.com/questions/4391697/find-the-index-of-a-dict-within-a-list-by-matching-the-dicts-value
def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

def add_emoji_to_dict(word, emj):
    global big_emoji_list, stemmer

    word = strip_punctuation(word.lower())

    word = stemmer.stem(word)

    emj = emoji.demojize(emj)
    print("Adding an emoji {} for the word {}".format(emj, word))
    for i in big_emoji_list:
        print("{} vs {}".format(emj, i["emoji"]))

        # need to find if i["meanings"] contains a dictionary where key "word" has value of word
        wordExists = False
        for g in i["meanings"]:
            if g["word"] == word:
                wordExists = True
                break
        
        if i["emoji"] == emj and not wordExists:
            i["meanings"].append({"word": word, "freq": 1})
            return
        elif i["emoji"] == emj and wordExists:
            i["meanings"][find(i["meanings"], "word", word)]["freq"] += 1
            return

    big_emoji_list.append({"emoji": emj, "meanings": [{"word": word, "freq": 1}]})


big_emoji_list = []

emoji_list_format = [
    {"emoji": "😎",
    "meanings": [
        "cool",
        "rad"
    ]}
]

stemmer = PorterStemmer()

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

    if count > 200:#int(sys.argv[1]) if len(sys.argv) < 2 and sys.argv[1].isdigit() else 50:
        break
    print('\n')

print(big_emoji_list)

with open("emoji_meanings.json", "w") as f:
    json.dump(big_emoji_list, f)
