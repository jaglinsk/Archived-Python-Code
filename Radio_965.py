'''Create a program that creates a csv file that contains all songs played on a local radio station over the course of an hour'''
import bs4
import urllib.request
import datetime
import sched
import time



playingnow = []
songs = []
artists = []

time_stop = time.time() + 3600


while time.time() < time_stop:
        
        timestamp = str(datetime.datetime.utcnow())
        radio = urllib.request.urlopen('http://www.quuit.com/Quu/np/88/5/280/234/340')
        soup = bs4.BeautifulSoup(radio)

        song = soup.find("a", ("np_ad_link", "np_music_link"))
        song_fix = song.string
                

        artist = soup.find("label")
        artist_fix = artist.string[(-(len(artist)-15)):]
        
        track = [timestamp, song_fix, artist_fix]
        
        if len(playingnow) == 0:
                playingnow.append(track)
                
        elif len(playingnow) > 0:
                if playingnow[-1][-2:] != track[-2:]:
                        playingnow.append(track)

        print(playingnow)
        sched.scheduler(time.time(),time.sleep(120))


with open("C:/Users/John/Documents/Python/RadioProject/965playlist.csv", "w", newline="") as csvfile:
	playlistwriter = csv.writer(csvfile)
	playlistwriter.writerows(playlist)
        
