from pytube import YouTube
import os

from flask import Flask, redirect, render_template, url_for, request, send_file
app = Flask(__name__)

# ytdownloader flask
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        link = str(request.form['linkyt'])
        yt = YouTube('{}'.format(link))
        yt.streams.filter(file_extension= 'mp4')
        filename = yt.title
        # data = yt.streams.get_by_resolution('720p')
        # data.download(output_path='')

        data = yt.streams.get_highest_resolution().download()        
        return send_file(data, as_attachment=True, download_name=f'{filename}.mp4')

        

    return render_template('home.html')



if __name__=='__main__':
    app.run()