#asd
import requests as r
from conky_styles import get_style
#print = pprint

STYLE_TEXT = get_style(size=10)
STYLE_TITLE = get_style(size=12, color="color0")
STYLE_SUBTITLE = get_style(color="color2")

STYLE_TEXT_2 = get_style(size=10, goto=200)
STYLE_TITLE_2 = get_style(size=12, goto=200, color="color0")
STYLE_SUBTITLE_2 = get_style(goto=200, color="color2")

def getJson():
    try:
        restaurants = r.get("https://skinfo.dy.fi/api/complete.json")
        return restaurants.json()
    except:
        line = STYLE_TEXT_2 + "oops :("
        print(line)


def parseJson():
    restaurants = ["ylioppilastalo", "laseri", "lut-buffet", "amk"]
    rc_lines = []
    r_json = getJson()
    r_json = r_json["restaurants"]

    for j, restaurant in enumerate(restaurants):
        days = []
        for day in r_json[restaurant]["days"]:
            days.append(day)

        if j == 0:
            title = "${voffset 20}" + STYLE_TITLE + restaurant + ":\n"
        elif j == 1:
            title = STYLE_TITLE + restaurant + ":\n"
        elif j == 2:
            title = "${voffset -280}" + STYLE_TITLE_2 + restaurant + ":\n"
        else:
            title = STYLE_TITLE_2 + restaurant + ":\n"
        line = ""

        try:
            for food in r_json[restaurant]["days"][days[0]]["foods"]:
                if j <= 1:
                    line += STYLE_SUBTITLE + food["category"] + "\n"
                    line += STYLE_TEXT + food["title_fi"] + "\n"
                else:
                    line += STYLE_SUBTITLE_2 + food["category"] + "\n"
                    line += STYLE_TEXT_2 + food["title_fi"] + "\n"
            rc_lines.append(title + line)

        except IndexError:
            if j <= 1:
                line += STYLE_TEXT + "Ei ruokalistaa :("
            else:
                line += STYLE_TEXT_2 + "Ei ruokalistaa :("
            rc_lines.append(title + line)

    return rc_lines


def main():
    lines = parseJson()
    for line in lines:
        print(line)


if __name__ == '__main__':
    main()
