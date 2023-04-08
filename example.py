from Peakpx import PeakPx


px = PeakPx()

#get wallpapers
wallpapers = px.get_wallpaers() #it will return a list of wallpapers

#pagination 
wallpapers = px.get_wallpaers(page=2) #by deafult its one

#search wallpapers
wallpapers = px.search_wallpapers(query='one piece') #you can also paas a page parameter here like page =2 by default its 1



