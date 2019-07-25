# cool

import sys
import emoji
import json

import argparse
from nltk.stem import *
import random


def emojify(inp):
    split_text = inp.split()

    index = 0
    last_one_was_an_emoji = False
    for word in split_text:
        if emoji.emoji_count(word) > 0 or last_one_was_an_emoji:
            last_one_was_an_emoji = False
            index += 1
            continue
        
        emoji_for_word = emoji_found_for(word)

        if emoji_for_word is not None:
            last_one_was_an_emoji = True
            split_text[index] += emoji_for_word

        index += 1

    reconstructed_with_emoji = " ".join(split_text)

    return reconstructed_with_emoji



def emoji_found_for(inp):
    with open("emoji_meanings.json", "r") as db:
        em_list = json.load(db)

    best_emoji = None
    best_emoji_freq = 0

    inp = stemmer.stem(inp)

    for emoj in em_list:
        
        # need to change this
        wordExists = False
        g_ = {}
        for g in emoj["meanings"]:
            if g["word"] == inp:
                wordExists = True
                g_ = g
                break

        if wordExists:
            #print("{} = {}".format(emoji.emojize(emoj["emoji"]), inp))

            if best_emoji_freq < g_["freq"]:
                best_emoji = emoj["emoji"]
                best_emoji_freq = g_["freq"]

        else:
            continue

    if best_emoji is not None: print("The best emoji for {} is {}".format(inp, emoji.emojize(best_emoji)))
    else: print("No emoji found for {}".format(inp))

    if best_emoji is None and random.randint(1, 3) == 2:
        best_emoji = ":clapping_hands:"
        print("Adding clapping hands anyway")
    return best_emoji


stemmer = PorterStemmer()

if len(sys.argv) < 2:
    print("Need arguments!")

else:
    if sys.argv[1] == "file":
        with open(sys.argv[2], "r") as f:
            out = emoji.emojize(emojify(f.read()))

        with open("output.txt", "w") as f:
            f.write(out)

        print("Emojipastainated version written to output.txt")

    elif sys.argv[1] == "sent":
        print(emoji.emojize(emojify(" ".join(sys.argv[2:]))))

    elif sys.argv[1] == "getemoji":
        print(emoji.emojize(emoji_found_for(sys.argv[2])))


# parser = argparse.ArgumentParser()

# parser.add_argument("-i", "--infile", help="Specify output file", type=str)
# args = parser.parse_args()

# print(args.output)



