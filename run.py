from bustimes import BusTimes
from flask import render_template, Flask
import ipdb
from operator import itemgetter

bt = BusTimes()

app = Flask(__name__)

@app.route('/')
def displayTimes():
    putney = [50440]
    clj = [75474,77433]
    return render_template('bustimes.html',
        putney_33=bt.getArrivalTimes(putney),
        putney_disruption=bt.getDisruptionInformation(putney[0]),
        clj_combined=bt.getArrivalTimes(clj),
        clj_disruption=bt.getDisruptionInformation(clj[0]),
        )

if __name__ == '__main__':
    #ipdb.set_trace()
    app.run(host='0.0.0.0', debug=True, port=9000)