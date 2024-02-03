# Lyrics Translator

This Python script utilizes various APIs to fetch song lyrics, translate them into Turkish, and display them using a Flask web interface. It integrates with Genius for lyrics retrieval and Spotify for current track information. Additionally, it offers a search functionality for finding lyrics based on user input.

## Dependencies

Make sure you have the following dependencies installed:

- `lyricsgenius`
- `spotipy`
- `googletrans`
- `flaskwebgui`

You can install them via pip:

```bash
pip install lyricsgenius spotipy googletrans flaskwebgui
```

## Usage

1. Obtain API credentials:
   - You'll need a Genius API token. Get one by signing up at [Genius Developer](https://genius.com/developers).
   - You'll also need Spotify API credentials. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) to create a new app and get your client ID and client secret. Make sure to set the redirect URI to `http://localhost:8888/callback`.

2. Replace placeholders in the script:
   - Replace `'your_genius_token'` with your Genius API token.
   - Replace `'your_client_id'` and `'your_client_secret'` with your Spotify API credentials.

3. Run the script:

```bash
python lyrics getter.py
```


## Additional Notes

- The script listens to your Spotify playback state. Make sure you have Spotify running and playing a track before accessing the web interface.
- If no track is currently playing, you'll be redirected to a 'Not Found' page.
- The search functionality allows you to find lyrics by providing the song and artist names.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
