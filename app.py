from flask import Flask, render_template

app = Flask(__name__)

jobs = [
            {'id' : 1,
                'title': 'Data Scientist',
                'Location': 'Bengaluru',
                'salary': 'Rs 12 lpa'
            },
                {'id' : 2,
                    'title': 'Data Analyst',
                    'Location': 'Bengaluru',
                    'salary': 'Rs 10 lpa'
                }
        ]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs = jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug = True)