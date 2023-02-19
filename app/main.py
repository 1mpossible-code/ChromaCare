from flask import Flask, request, redirect
from flask import render_template
from Services.ParsingService import ParsingService
from Services.ColorConversion import ColorConversion
from Services.RatingColorService import RatingColorService

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    errors = []
    if request.method == "POST":
        url = request.form['url']
        try:
            parsingService = ParsingService(url)
            colors = parsingService.parse_colors()
            colors_converted = []
            ratings = []
            rated = []
            avg_rating = 0
            for color in colors:
                rgb = ColorConversion.convert(color)
                colors_converted.append(rgb)
                color_rating = RatingColorService.rate(rgb)
                ratings.append(color_rating)
                rated.append([color, color_rating])
            if len(colors) == 0:
                errors.append(
                    "Colors haven't been found on this website. If the website works correctly, please contact us, so we can fix the issue.")
            else:
                avg_rating = round(sum(ratings) / len(colors), 1)
                url = parsingService.url
            return render_template("index.html", colors_rated=rated, avg=avg_rating, url=url, errors=errors)
        except Exception:
            errors.append("Unexpected error. Please check if the url of the website you sent is correct")
    return render_template("index.html", errors=errors)


@app.errorhandler(404)
def not_found(e):
    return redirect('/')
