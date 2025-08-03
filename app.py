from flask import Flask, render_template, request, redirect
from scraper import fetch_case_details
from db import init_db, log_query
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    details, raw_html, error = fetch_case_details(case_type, case_number, filing_year)

    # Log in DB
    log_query(case_type, case_number, filing_year, raw_html)

    if error:
        return render_template('result.html', error=error)
    return render_template('result.html', details=details)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
