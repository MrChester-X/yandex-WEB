from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/list_prof/<list_type>")
def index(list_type):
    jobs = [
        "инженер-исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов"
    ]

    params = {}
    params["list_type"] = list_type
    params["jobs"] = jobs

    return render_template("index.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
