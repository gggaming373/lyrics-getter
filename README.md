Türkçe readme için aşağı kaydırın
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










# Şarkı Sözü Alıcı

Bu Python betiği, şarkı sözlerini çekmek, onları Türkçe'ye çevirmek ve bir Flask web arayüzü kullanarak göstermek için çeşitli API'leri kullanır. Şarkı sözlerini almak için Genius'i ve mevcut parça bilgilerini almak için Spotify'i entegre eder. Ayrıca, kullanıcı girdisine dayalı olarak şarkı sözlerini bulma işlevselliği sunar.

## Bağımlılıklar

Aşağıdaki bağımlılıkların yüklü olduğundan emin olun:

- `lyricsgenius`
- `spotipy`
- `googletrans`
- `flaskwebgui`

Bunları pip aracılığıyla kurabilirsiniz:

```bash
pip install lyricsgenius spotipy googletrans flaskwebgui
```

## Kullanım

1. API kimlik bilgilerini edinin:
   - Genius API belirteci almanız gerekecek. [Genius Developer](https://genius.com/developers) adresine giderek bir tane alın.
   - Ayrıca Spotify API kimlik bilgilerine ihtiyacınız olacak. Yeni bir uygulama oluşturun ve istemci kimliği ve istemci sırrınızı almak için [Spotify Developer Paneli](https://developer.spotify.com/dashboard/) adresine gidin. Yönlendirme URI'sini `http://localhost:8888/callback` olarak ayarladığınızdan emin olun.

2. Betikteki yer tutucuları değiştirin:
   - `'your_genius_token'` yerine Genius API belirtecinizi girin.
   - `'your_client_id'` ve `'your_client_secret'` yerine Spotify API kimlik bilgilerinizi girin.

3. Betiği çalıştırın:

```bash
python lyrics_getter.py
```

## Ek Notlar

- Betik Spotify çalma durumunu dinler. Web arayüzüne erişmeden önce Spotify'in çalıştığını ve bir parça çaldığınızı kontrol edin.
- Eğer şu anda çalan bir parça yoksa, 'Bulunamadı' sayfasına yönlendirileceksiniz.
- Arama işlevselliği, şarkı ve sanatçı adlarını sağlayarak şarkı sözlerini bulmanızı sağlar.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.