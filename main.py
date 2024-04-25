from flask import Flask, render_template, request
from calc_dist import calc_dist


app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/result")
def result():
    q_cidade = request.args.get('q_cidade')
    q_estado = request.args.get('q_estado')
    result = calc_dist(q_cidade, q_estado)

    return render_template('result.html',
                           q_cidade=q_cidade,
                           q_estado=q_estado,
                           result=result)


if __name__ == '__main__':
    app.run(debug=True)
