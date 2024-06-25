from flask import Flask, render_template, request, redirect, url_for, flash
from analysis.data_fetching import fetch_frames
from analysis.trend_analysis import analyze_trends
from analysis.report_generation import generate_report
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trends', methods=['POST'])
def trends():
    username = request.form['username']
    frames = fetch_frames(username)
    trend_results = analyze_trends(frames)
    report_path = generate_report(trend_results, username)
    flash('Trend analysis complete! Download your report.', 'success')
    return redirect(url_for('report', report_path=report_path))

@app.route('/report/<path:report_path>')
def report(report_path):
    return render_template('report.html', report_path=report_path)

if __name__ == '__main__':
    app.run(debug=True)
