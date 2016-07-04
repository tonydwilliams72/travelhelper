from bustimes import BusTimes
from flask import render_template, Flask
from operator import itemgetter

bt = BusTimes()

app = Flask(__name__)

@app.route('/sw')
def displaySwTimes():
    putney = [50440]
    clj = [75474,77433]
    return render_template('sw_bustimes.html',
        putney_33=bt.getArrivalTimes(putney),
        putney_disruption=bt.getDisruptionInformation(putney[0]),
        clj_combined=bt.getArrivalTimes(clj),
        clj_disruption=bt.getDisruptionInformation(clj[0]),
        )

@app.route('/se')
def displaySeTimes():
    lewisham = [48893, 47492]
    bus = ['273', '261']
    return render_template('se_bustimes.html',
        lewisham_buses=bt.getArrivalTimes(stopCodes=lewisham,filter=bus)
        )

if __name__ == '__main__':
    #ipdb.set_trace()
    app.run(host='0.0.0.0', debug=True, port=9000)
