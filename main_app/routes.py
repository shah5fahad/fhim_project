from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/peer_reviewed')
def peer_reviewed():
    return render_template('peer_reviewed.html')


@app.route('/ugc_care')
def ugc_care():
    return render_template('ugc_care.html')


@app.route('/DOI_Allocation')
def DOI_Allocation():
    return render_template('DOI_Allocation.html')


@app.route('/Payment')
def Payment():
    return render_template('Payment.html')

@app.route('/cauti_prevention')
def cauti_prevention():
    return render_template('cauti_prevention.html')


@app.route('/current_issue')
def current_issue():
    return render_template('Current_issue.html')


@app.route('/respectful_maternity_care')
def respectful_maternity_care():
    return render_template('respectful_maternity_care.html')


@app.route('/diabetes_data_intelligence')
def diabetes_data_intelligence():
    return render_template('diabetes_data_intelligence.html')


@app.route('/ai_drug_discovery')
def ai_drug_discovery():
    return render_template('ai_drug_discovery.html')


@app.route('/data_science_hospital_management')
def data_science_hospital_management():
    return render_template('data_science_hospital_management.html')

@app.route('/group')
def group():
    return render_template('group.html')
