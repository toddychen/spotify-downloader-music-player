from tkinter import *
from about import *

def homebackground():
	root = Tk()
	root.title('spotify-downloader-music-player')

	frame1 = Frame(root, borderwidth=2, relief='ridge')  
	frame2 = Frame(root, borderwidth=2, relief='ridge')  
	frame3 = Frame(root, borderwidth=2, relief='ridge')
	frame4 = Frame(root, borderwidth=0, relief='ridge')
	frame5 = Frame(root, borderwidth=0, relief='ridge')
	 
	frame1.grid(column=0, row=0, sticky="nsew")  
	frame2.grid(column=0, row=1, sticky="nsew")  
	frame3.grid(column=0, row=2, sticky="nsew")
	frame4.grid(column=1, row=0, sticky="nsew")
	frame5.grid(column=2, row=0, sticky="nsew")
	 
	home = Button(frame1, text="HOME",width=15, command=homebackground)  
	playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
	about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
	songName = Entry(frame4, width=40)
	download = Button(frame5, text="Download")
	 
	home.pack(fill='x')  
	playlist.pack(fill='x')  
	about.pack(fill='x')
	songName.pack()
	download.pack()
	 
	root.mainloop() 

def aboutbackground():
	root = Tk()
	root.title('spotify-downloader-music-player')

	frame1 = Frame(root, borderwidth=2, relief='ridge')  
	frame2 = Frame(root, borderwidth=2, relief='ridge')  
	frame3 = Frame(root, borderwidth=2, relief='ridge')
	frame4 = Frame(root, borderwidth=0, relief='ridge')
	frame5 = Frame(root, borderwidth=0, relief='ridge')
	frame6 = Frame(root, borderwidth=0, relief='ridge')
	 
	frame1.grid(column=0, row=0, sticky="nsew")  
	frame2.grid(column=0, row=1, sticky="nsew")  
	frame3.grid(column=0, row=2, sticky="nsew")
	frame4.grid(column=1, row=0, sticky="nsew")
	frame5.grid(column=1, row=1, sticky="nsew")
	frame6.grid(column=1, row=2, sticky="nsew")
	 
	home = Button(frame1, text="HOME",width=15, command=homebackground)  
	playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
	about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
	Label(frame4, text="A GUI version of spotify-downloder of Ritiek Malhotra.").pack()
	Label(frame5, text="It can download music from YouTube in MP3 format and can play them.").pack()
	Label(frame6, text="It can download songs directly by typing name or typing the link.").pack()
	 
	home.pack(fill='x')  
	playlist.pack(fill='x')  
	about.pack(fill='x')
	 
	root.mainloop() 

def playlistbackground():
	root = Tk()
	root.title('spotify-downloader-music-player')

	frame1 = Frame(root, borderwidth=2, relief='ridge')  
	frame2 = Frame(root, borderwidth=2, relief='ridge')  
	frame3 = Frame(root, borderwidth=2, relief='ridge')
	frame4 = Frame(root, borderwidth=0, relief='ridge')
	frame5 = Frame(root, borderwidth=0, relief='ridge')
	frame6 = Frame(root, borderwidth=0, relief='ridge')
	 
	frame1.grid(column=0, row=0, sticky="nsew")  
	frame2.grid(column=0, row=1, sticky="nsew")  
	frame3.grid(column=0, row=2, sticky="nsew")
	frame4.grid(column=1, row=0, sticky="nsew")
	frame5.grid(column=1, row=1, sticky="nsew")
	frame6.grid(column=1, row=2, sticky="nsew")
	 
	home = Button(frame1, text="HOME",width=15, command=homebackground)  
	playlist = Button(frame2, text="PLAYLIST",width=15, command=playlistbackground)  
	about = Button(frame3, text="ABOUT",width=15, command=aboutbackground)
	 
	home.pack(fill='x')  
	playlist.pack(fill='x')  
	about.pack(fill='x')
	 
	root.mainloop() 

if __name__ == '__main__':
	homebackground();