from pytube import YouTube
from pathlib import Path
import os

from flask import Flask, redirect, render_template, url_for, request, send_file
app = Flask(__name__)


reso1 = '1080p'
reso2 = '720p'
reso3 = '480p'
reso4 = '360p'
reso5 = '240p'
reso6 = '144p'


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

# def uploaded_file(filename):
#     filename_processed = 'processed' + '-' + filename
#     return send_from_directory("downloads", filename, as_attachment=True, attachment_filename=filename_processed)


# ytdwonloader
def mp4Download():
    print('Masukkan Link Youtube: ')
    link = input('> ')

    while True:
        print("Pilih Resolusi: 1-5")
        print('1.', reso1)
        print('2.', reso2)
        print('3.', reso3)
        print('4.', reso4)
        print('5.', reso5)
        print('6.', reso6)

        reso = int(input("> "))
        if reso == 1:
            reso = reso1            
            break
                   
        elif reso == 2:
            reso = reso2
            if reso != None:
                break
            else:
                print('Resolusi tidak tersedia')

        elif reso == 3:
            reso = reso3
            if reso != None:
                break
            else:
                print('Resolusi tidak tersedia')

        elif reso == 4:
            reso = reso4
            if reso != None:
                break
            else:
                print('Resolusi tidak tersedia')

        elif reso == 5:
            reso = reso5
            if reso != None:
                break
            else:
                print('Resolusi tidak tersedia')

        elif reso == 6:
            reso = reso6
            if reso != None:
                break
            else:
                print('Resolusi tidak tersedia')

        print("Pilih 1-5!!")
        continue
        

    try:
        yt = YouTube('{}'.format(link))
        print(f'{yt.title} - {reso}') 
        print('Connecting to Youtube...')      
        yt.streams.filter(file_extension= 'mp4')
        data = yt.streams.get_by_resolution(f'{reso}')           
                        
        
            
    except:
        print("Connection Error")
        exit()

    print('Downloading....')
        
    # for _ in tqdm(range(100), unit= 'KB'):        
    data.download()    

    print('Task Completed')
    print(f'Video Saved in')

def mp3Download():
    print('Masukkan Link Youtube: ')
    link = input('> ')
        

    try:
        yt = YouTube('{}'.format(link))
        print(f'{yt.title} - mp3') 
        print('Connecting to Youtube...')      
        yt.streams.filter(only_audio=True)
        data = yt.streams.get_audio_only('mp4')

    except:
        print("Connection Error")
        exit()

    print('Downloading....')
        
    # for _ in tqdm(range(100), unit= 'KB'):        
    #     data.download(SAVE_PATH)    

    print('Task Completed')
    print(f'Video Saved in')

def menu():
    print('Pilih menu:')
    while True:
        print('1. Download Video mp4')
        print('2. Download Audio mp3 - (only audio)')
        menu = int(input('> '))

        if menu == 1:
            mp4Download()
            break
        elif menu == 2:
            mp3Download()
            break
        print("Pilih menu yang ada!!")
        continue

if __name__=='__main__':
    app.run(debug=True)