from pytube import YouTube
from tqdm import tqdm, trange

SAVE_PATH = "D:/Kuliah Amikom/Kuliah SEM 5/Pemrograman Python/Final Project"


print('Masukkan Link Youtube: ')
link = 'https://youtu.be/E7NgR0LEMbI'

def ytDownload():
    
    yt = YouTube('{}'.format(link))
    print(yt.title)
    yt.streams.filter(only_audio=True)
    y= yt.streams.get_by_resolution(resolution='480p') 
    data = yt.streams.get_audio_only('mp4')
    
    
    # print(yt.streams.filter(file_extension='mp4'))   
    # print(s)
    print(data)
    # print(yt.streams.filter(only_audio=True))   
    # print(type(yt.streams[0:3]))  
    # print(y)   

         

ytDownload()