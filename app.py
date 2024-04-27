from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)


data = pd.read_csv("Tamil_movies_dataset.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies/<genre>')
def get_movies(genre):
    
    genre_data = data[data['Genre'] == genre]

    
    movies_info = []
    for _, row in genre_data.iterrows():
        movie_info = {
            'Movie Name': row['MovieName'],
            'Rating': row['Rating'],
            'Director': row['Director']
        }
        movies_info.append(movie_info)

    return jsonify(movies_info)

if __name__ == '__main__':
    app.run(debug=True)

