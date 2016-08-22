from bustimes import BusTimes
from flask import render_template, Flask

bt = BusTimes()

app = Flask(__name__)


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


@app.route('/se')
def displaySeTimes():
    lewisham = [48893, 47492]
    bus = ['273', '261']
    return render_template(
        'se_bustimes.html',
        lewisham_buses=bt.getArrivalTimes(stopCodes=lewisham, filter=bus)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9000)
