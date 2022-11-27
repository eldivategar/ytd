from pytube import YouTube, exceptions, Search

from flask import Flask, redirect, render_template, url_for, request, send_file
app = Flask(__name__)


# ytdownloader flask
@app.route('/', methods=['POST', 'GET'])
def home():
    global link
    if request.method == 'POST':
        link = request.form['linkyt']  
        try:      
            yt = YouTube('{}'.format(link))
            filename = yt.title        
            thumbnail = yt.thumbnail_url                
            
            return render_template('home.html', titles = filename, thumbnails = thumbnail, mp4 = link, mp3 = link, result = link)

        except (exceptions.RegexMatchError, exceptions.VideoUnavailable) as error :
            return render_template('404.html')
        
        
    else:
        return render_template('home.html')

@app.route('/search', methods=['POST', 'GET'])  
def menuVideos():
    if request.method == 'POST':
        title = request.form['title']
        try:            
            s = Search(f'{title}')            
            
            return render_template('menuVideos.html', titles = [ts.title for ts in s.results], urls= [ts.watch_url for ts in s.results], judul = title)

        except (exceptions.RegexMatchError, exceptions.VideoUnavailable) as error :
            return render_template('404.html')

    else:
        return render_template('menuVideos.html')


@app.route('/<title>')
def single_page():

    return render_template('single-page.html')

@app.route('/mp4')
def get_mp4():        
    try:        
        yt = YouTube('{}'.format(link))
        yt.streams.filter(file_extension= 'mp4')
        filename = yt.title        

        data = yt.streams.get_highest_resolution().download()
        
        return send_file(data, as_attachment=True, download_name=f'{filename}.mp4')

    except (exceptions.RegexMatchError, exceptions.VideoUnavailable) as error :
        return render_template('404.html')


@app.route('/mp3')
def get_mp3(): 
    try: 
        yt = YouTube('{}'.format(link))
        yt.streams.filter(only_audio=True)    
        filename = yt.title

        data = yt.streams.get_audio_only('mp4').download()    

        return send_file(data, as_attachment=True, download_name=f'{filename}.mp3')      
    
    except (exceptions.RegexMatchError, exceptions.VideoUnavailable) as error :
        return render_template('404.html')




if __name__=='__main__':
    app.run(debug=True, port=5500)