# Emojipasta-Inator
 Insert emojis into a text file

## Example
The following text:
```
What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.
```

Becomes this:
```
What😅 the fuck🖕 did you👈 just fucking🖕 say about🤔 me, you👈 little bitch?👏 I’ll have🈶 you know🤔 I graduated👏 top of🏠 my class😡 in the👮 Navy Seals,👏 and I’ve been🗿 involved in➡ numerous secret🙊 raids on🔛 Al-Quaeda, and👀 I have🈶 over 300👏 confirmed kills.👏 I am trained in➡ gorilla warfare👏 and I’m the👮 top sniper in➡ the entire US armed forces.👏 You are🅱 nothing to🅱 me but😩 just another🙌 target. I will😮 wipe you👈 the fuck🖕 out with🎉 precision the👮 likes of🏠 which has😏 never been🗿 seen before✝ on this⬆ Earth, mark my👧 fucking words.👏 You think🤔 you can💤 get away😟 with saying🗣 that shit💩 to me💦 over the👮 Internet? Think🤔 again, fucker. As we👨 speak I am contacting my👧 secret network👏 of spies👏 across the👮 USA and👀 your IP is🈶 being traced right➡ now so🆘 you better👽 prepare for🆘 the storm, maggot. The👮 storm that💯 wipes out🏎 the pathetic👏 little thing⚡ you call🗣 your life.👏 You’re fucking🖕 dead, kid.👏 I can💤 be anywhere,👏 anytime, and👀 I can💤 kill you👈 in over🏠 seven hundred👏 ways, and👀 that’s just😩 with my👧 bare hands. Not🚫 only am I extensively trained in➡ unarmed combat, but😩 I have🈶 access to🅱 the entire👏 arsenal of🏠 the United👏 States Marine👏 Corps and👀 I will😮 use it🤡 to its🤡 full extent👏 to wipe👏 your miserable ass🍑 off the👮 face of🏠 the continent,👏 you little👶 shit. If👏 only you👈 could have🈶 known what😅 unholy retribution👏 your little👶 “clever” comment👏 was about🤔 to bring down⬇ upon you,👏 maybe you👈 would have🈶 held your👉 fucking tongue. But😩 you couldn’t,👏 you didn’t, and👀 now you’re paying👏 the price,👏 you goddamn👏 idiot. I will😮 shit fury all👮 over you👈 and you👈 will drown😱 in it. You’re fucking🖕 dead, kiddo.👏
```

## Usage
`python3 epi.py [command] [info]`

Where `[command]` is one of the following:

* `file` - reads from the filename specified in `[info]` and writes to `output.txt`
* `sent` - reads the rest of the text written and prints the output
* `getemoji` - gets the emoji for a specific word

### Creating or updating the emoji list
Use the file `scraper.py` to construct a list of emoji and related words. You will need a reddit secret key to be in the file `reddit_secret`.

## Dependencies
* `emoji` - handles some emoji stuff. Install with `pip3 install emoji`
* `nltk` - handles some text processing stuff. Install with `pip3 install nltk`

Emoji list-builder only:
* `praw` - used for scraping Reddit. Install with `pip3 install praw`
