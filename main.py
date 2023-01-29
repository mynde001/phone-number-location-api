from flask import Flask, jsonify

app = Flask(__name__)

# First 2 numbers are unique
number_formats = {
    'Greece': 30,
    'Netherlands': 31,
    'Belgium': 32,
    'France': 33,
    'Spain': 34,
    'Hungary': 36,
    'Italy': 39,
    'Romania': 40,
    'Switzerland': 41,
    'Austria': 43,
    'United Kingdom': 44,
    'Denmark': 45,
    'Sweden': 46,
    'Norway': 47,
    'Poland': 48,
    'Germany': 49,
    'Turkey': 90,
    'Faroe Islands': 298,
    'Gibraltar': 350,
    'Portugal': 351,
    'Luxembourg': 352,
    'Ireland': 353,
    'Iceland': 354,
    'Albania': 355,
    'Malta': 356,
    'Cyprus': 357,
    'Finland': 358,
    'Bulgaria': 359,
    'Lithuania': 370,
    'Latvia': 371,
    'Estonia': 372,
    'Moldova': 373,
    'Armenia': 374,
    'Belarus': 375,
    'Andorra': 376,
    'Monaco': 377,
    'San Marino': 378,
    'Ukraine': 380,
    'Serbia': 381,
    'Montenegro': 382,
    'Kosovo': 383,
    'Croatia': 385,
    'Slovenia': 386,
    'Bosnia and Herzegovina': 387,
    'North Macedonia': 389,
    'Czech Republic': 420,
    'Slovakia': 421,
    'Liechtenstein': 423,
    'Georgia': 995
}

@app.route("/api/number/<num>")
def index(num):
    # Matches <num>'s first 2 numbers with number_formats first 2 values
    matches = [[key, val] for key, val in number_formats.items() if str(val)[0:2] in num[0:2]]

    if len(matches) > 1:
        # If the first 2 numbers are duplicates - matches the 3rd number of <num> and val
        return jsonify([[key, val] for key, val in matches if str(val)[2] in num[2]])

    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug = True)