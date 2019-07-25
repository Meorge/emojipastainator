# cool

import sys
import emoji
import json



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

    with open("output.txt", "w") as f:
        f.write(reconstructed_with_emoji)

    print("Emojipastainated version written to output.txt")

def emoji_found_for(inp):
    with open("emoji_meanings.json", "r") as db:
        em_list = json.load(db)

        for emoj in em_list:
            if inp in emoj["meanings"]:
                print("{} = {}".format(emoji.emojize(emoj["emoji"]), inp))
                return emoji.emojize(emoj["emoji"])

        return None


with open("input.txt", "r") as f:
    emojify(f.read())