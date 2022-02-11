from flask import Flask, render_template, url_for

app = Flask(__name__)

count = 0


@app.route("/training/<prof>")
def index(prof):
    params = {}

    if "инженер" in prof or "строитель" in prof:
        params["place"] = "Инженерные тренажеры"
        params["img"] = url_for('static', filename='img/1.png')
    else:
        params["place"] = "Научные симуляторы"
        params["img"] = url_for('static', filename='img/2.png')

    return render_template("index.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
