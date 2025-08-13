from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/malware-analysis')
def malware_analysis():
    return render_template('malware_analysis.html')

@app.route('/penetration-testing')
def penetration_testing():
    return render_template('penetration_testing.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
