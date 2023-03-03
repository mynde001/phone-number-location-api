from flask import Flask
from db import country_calling_codes

app = Flask(__name__)

@app.get("/api/number/<num>")
def index(num):
    try:
        # Matches the first 2 numbers of num with number_formats' values
        first_2_numbers_match = [[key, val] for key, val in country_calling_codes.items() if str(val)[0:2] in num[0:2]]

        if len(first_2_numbers_match) > 1:
            # Matches the 3rd number of num with val's 3rd number
            third_number_match = [[key, val] for key, val in first_2_numbers_match if str(val)[2] in num[2]]
            return {
                "country": third_number_match[0][0],
                "country calling code": third_number_match[0][1]
            }

        return {
            "country": first_2_numbers_match[0][0],
            "country calling code": first_2_numbers_match[0][1]
        }

    except IndexError:
        return {"message": "Invalid input"}, 404

if __name__ == '__main__':
    app.run(debug = True)
