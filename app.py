from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('sample_data.csv')
    summary = df.describe().to_html(classes='table table-striped')
    return render_template('index.html', tables=[summary], titles=['Summary Statistics'])

if __name__ == "__main__":
    app.run(debug=True)
