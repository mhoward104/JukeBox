#Python Jukebox
#by Matthew Howard

#create a shuffle function  that selects inputOne/inputTwo randomly

import vlc , os , random , string
from random import randrange

class newPlayer(object):
    def __init__(self):
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
    
    def Open(self):
        Hex = ['A', 'B', 'C', 'D', 'E', 'F']
        pause = False
        
        while True:
            #Get inputs
            inputOne = input('Enter a character from A-F or H: ').upper()
            
            #P == Pause/play
            if inputOne == "P" and pause == False:
                self.player.pause()
            elif inputOne == "P" and pause == True:
                self.player.play()
            #S == Shuffle
            elif inputOne == "S":
                inputOne = Hex[random.randrange(0, 6)]
                print(inputOne)
                inputTwo = random.randrange(0,10)
                print(inputTwo)
            elif inputOne == "H" or inputOne == "HELP":
                print("To Choose a Song type a letter from A-F and press enter.")
                print("Next choose a number from 0-9 and hit enter")
                print("to pause/play press the 'p' key")
                print("To play a random song press 's'")
                continue
            elif inputOne == "":
                continue
            else:
                inputTwo = eval(input('Enter an integer from 0-9: '))           
####find song
            if inputOne == 'A':
                genre = "HipHop/" # done
                songList = ["01 Check the Rhime.m4a", "02 DNA..mp3", "03 Ch-Check It Out.m4a",
                            "03 Work.m4a", "03 Stan.m4a", "10 Juicy.m4a",
                            "10 It Was a Good Day.m4a", "06 Handlebars.m4a", "05 Clint Eastwood.m4a",
                            "02 N.Y. State of Mind.m4a"]
            elif inputOne == "B":
                genre = "Country/" # done
                songList = ["01 I'm Not Gonna Miss You.m4a", "02 Going Down To the River.m4a",
                            "2-04 Folsom Prison Blues (Live).m4a", "03 Tennessee Whiskey.m4a",
                            "08 Are the Good Times Really Over.m4a","09 A Country Boy Can Survive.m4a",
                            "12 Whiskey River.m4a", "09 The Yellow Rose (With Lane Brody).m4a",
                            "2-10 Seven Spanish Angels (with Ray.m4a", "09 Whiskey Lullaby (feat. Alison Kra.m4a"]
            elif inputOne == "C":
                genre = "Rock/" # done
                songList = ["01 Bye Bye Miss American Pie.m4a", "01 Hysteria (2013 Re-Recorded Versio.m4a",
                            "1-01 Bohemian Rhapsody.m4a", "1-04 Roxanne.m4a", "08 Juke Box Hero.m4a",
                            "08 Every Rose Has Its Thorn.m4a", "10 Rock and Roll Ain't Noise Polluti.m4a",
                            "01 Hotel California.m4a", "04 Simple Man.m4a", "06 John the Fisherman.m4a"]
            elif inputOne == "D":
                genre = "Oldies/"# done
                songList = ["07 Stand By Me.m4a", "01 Dancing In the Moonlight (Origina.m4a",
                            "01 Please Mr. Postman.m4a", "08 Brandy (You're a Fine Girl).mp3",
                            "09 Come a Little Bit Closer.mp3", "14 Boogie Shoes.m4a",
                            "17 Lovers Who Wander.m4a", "02 A Whiter Shade of Pale.m4a",
                            "09 Minnie the Moocher.m4a", "08 Fly Me to the Moon (feat. Count B.m4a"]
            elif inputOne == "E":
                genre = "Soul/" # done
                songList = ["01 Lovely Day.m4a", "01 Tired of Being Alone.m4a", "03 September.m4a",
                            "04 Me and Mrs. Jones.m4a", "05 Love On a Two Way Street.m4a",
                            "06 Redbone.m4a", "07 I Can't Help Myself (Sugar Pie, H.m4a",
                            "07 Risin' to the Top.m4a", "09 (Sittin' On) The Dock of the Bay.m4a",
                            "13 Brother Louie.m4a"]
            elif inputOne == "F":
                genre = "Pop/" # done
                songList = ["01 Escape (The Pina Colada Song).m4a", "01 Uptown Funk (feat. Bruno Mars).m4a",
                            "1-09 Rasputin.m4a", "1-16 Billie Jean (Single Version).m4a",
                            "04 Treasure.m4a", "05 Happy (From _Despicable Me 2_).m4a",
                            "11 Do It.m4a", "06 Lose Yourself to Dance (feat. Pha.m4a",
                            "13 History.m4a", "01 Stayin' Alive.m4a"]
            else :
                continue
            #assign song
            songName = songList[inputTwo]
            
##plays song
            self.Media = self.Instance.media_new_path("Music/" + genre + songName)
            self.player.set_media(self.Media)
            
            title = self.player.get_title()
            print("now playing: " + songName)
            self.player.play()
            continue

    def Play(self):
        self.player.get_media()
        
Spelar = newPlayer()
Spelar.Open()
Spelar.Play()

