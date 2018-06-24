#!/usr/bin/python3
from data import *
from sqldb import *
import webbrowser
from tkinter import *
from kmlparser import *

def makehtmlfile(coordinates):
	html_code = head + coordinates[0] + \
			  middle + coordinates[1] + \
			  tail
	html_fpath = "gmap_polygon.html"
	f = open(html_fpath, "w")
	f.write(html_code)
	f.close()
	return html_fpath

def main():
	root = Tk()
	user_input = Entry()
	user_input.pack()

	OPTIONS = getnamelist()

	strvar = StringVar(root)
	strvar.set(OPTIONS[0])

	opt = OptionMenu(root, strvar, *OPTIONS)
	opt.pack()
	
	def openmap(name):
		kml_file = kml_fpath
		kml = KMLPlacemark(kml_file)		
		coordinates = kml.getcoordinates(getpolyname(name))
		
		html_fpath = makehtmlfile(coordinates)
		webbrowser.open(html_fpath)

	def openmap_entry(event):
		name = user_input.get()
		openmap(name)		

	def openmap_list():
		name = strvar.get()
		openmap(name)


	button = Button(root, text="Open Map", command=openmap_list)
	button.pack()
	
	user_input.bind('<Return>', openmap_entry)


	root.mainloop()




if __name__ == '__main__':
	main()


