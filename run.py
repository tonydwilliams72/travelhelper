from bustimes import BusTimes
from flask import render_template, Flask

from google.cloud import error_reporting

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

@app.route('/lee_baring')
def displaySeTimes():
    lee = ['490001176B']
    baring = ['490007801N']
    bus = ['273', '261']
    return render_template(
        'se_bustimes.html',
        lee=bt.getArrivalTimes(stopCodes=lee),
        baring=bt.getArrivalTimes(stopCodes=baring)
    )

if __name__ == '__main__':
    try:
        import googleclouddebugger
        googleclouddebugger.enable(
            module='travelhelper',
            version='v1.0'
        )
    except ImportError:
        client.report_exception()
    app.run(host='0.0.0.0', port=8080, debug=True)
