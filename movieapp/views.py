from flask import Flask, render_template, url_for, request, render_template_string
from .models import indices, df
import pandas as pd
import re
import numpy as np

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
     return render_template_string("saisissez l'identifiant ou le nom du film à la fin de l'url pour avoir une recommandation. Par exemple : 'https://findmovie0606.herokuapp.com/recommend/2379713' ou https://findmovie0606.herokuapp.com/recommend/spectre") 

@app.route('/recommend/<uid>')
def reco(uid):
    info = ['Film recherché', 'Recommandation 1', 'Recommandation 2', 'Recommandation 3', 'Recommandation 4', 'Recommendation 5']
    if re.match('\d{7}',uid)!=None:
        try:
            idx=df[df['movie_imdb_link'].str.contains(uid)].index[0]
            result = df.iloc[indices.loc[idx]]
            result['info'] = info
            result_html = result[['info','movie_imdb_link','movie_title']].to_html(index=False,justify='center', render_links=True)
        except:
            result_html = "L'identifiant " + uid + " n'existe pas"
    else:
        idx = df[df['movie_title'].str.contains(uid, case=False)].index
        result_html = ''
        for i in np.arange(len(idx)):
            result = df.iloc[indices.loc[idx[i]]]
            result['info'] = info
            result_html = result_html + result[['info','movie_imdb_link','movie_title']].to_html(index=False,justify='center', render_links=True) + ' <p> <br> </p>'
        
        if result_html=='':
            result_html = "Aucun film ne contient " + uid + " dans son titre"
    return render_template_string(result_html)

if __name__ == "__main__":
    app.run()