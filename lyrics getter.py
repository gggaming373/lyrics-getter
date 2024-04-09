import lyricsgenius
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyOAuth
from googletrans import Translator
from flaskwebgui import FlaskUI # import FlaskUI

def translate_to_turkish(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='tr').text
    return translated_text

genius = lyricsgenius.Genius('nO4jf7EpinHU2AOTEY1P92zF_Z4oeQsd6-plG2hwr-J7qlZC83pGp8ZFnn2Pv0dG')

# Replace 'your_client_id', 'your_client_secret', and 'your_redirect_uri' with your actual credentials
scope = "user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your_client_id',
                                               client_secret='your_client_secret',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope=scope))



from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def redirectingtolyrics():
    return redirect('/lyrics')

@app.route('/lyrics')
def index():
    current_track = sp.current_playback()
    if current_track is not None:
        print(current_track['item']['name'], current_track['item']['artists'][0]['name'])
        getartist = current_track['item']['artists'][0]['name']
        getsong = current_track['item']['name']
        song = genius.search_song(getsong, getartist)
        getimage = song.song_art_image_url
        lyrics = '\n'.join(song.lyrics.splitlines()[1:]).replace('Embed', '')
        turkish = translate_to_turkish(lyrics)
        return render_template('test.html',getartist=getartist, getsong=getsong, lyrics=lyrics, turkish=turkish, getimage= getimage )
    else:
        print("No track is currently playing.")
        return redirect("/notfound")




    
@app.route('/notfound')
def notfound():
    return render_template('notfound.html')

@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'GET':
        return render_template('enter.html')
    elif request.method == 'POST':
        usersong = request.form['song']
        userartist = request.form['artist']
        print(usersong, userartist)
        return redirect(f'/search/{usersong}/{userartist}')

@app.route('/search/<usersong>/<userartist>')
def result(usersong, userartist):
    print(userartist, usersong)
    getartist = userartist
    getsong = usersong
    song = genius.search_song(getsong, getartist)
    getimage = song.song_art_image_url
    print(song)
    lyrics = '\n'.join(song.lyrics.splitlines()[1:]).replace('Embed', '')
    print(lyrics)
    turkish = translate_to_turkish(lyrics)
    print(turkish)
    
    return render_template('test.html',getsong=getsong, lyrics=lyrics, turkish=turkish, getimage = getimage, getartist = getartist)


if __name__ == '__main__':
    FlaskUI(app=app, server="flask").run()
    