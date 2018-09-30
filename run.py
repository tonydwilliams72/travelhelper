from bustimes import BusTimes
from flask import render_template, Flask

bt = BusTimes()

app = Flask(__name__)   

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/sw')
def displaySwTimes():
    putney = ['490012985W']
    clj = ['490012985EG', '490012985E']
    return render_template(
        'sw_bustimes.html',
        putney_33=bt.getArrivalTimes(putney),
        putney_disruption=[],
        clj_combined=bt.getArrivalTimes(clj),
        clj_disruption=[],
    )

@app.route('/lee_harland')
def displaySeTimes():
    lee_harland = ['490001176B']
    harland_lee = ['490007801N']
    bus = ['273', '261']
    return render_template(
        'se_bustimes.html',
        lee_harland=bt.getArrivalTimes(stopCodes=lee_harland),
        harland_lee=bt.getArrivalTimes(stopCodes=harland_lee)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
