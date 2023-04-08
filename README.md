# PeakPX
Unofficial python wrapper for PeakPX.com API
## Important

<p align="center"><a href="https://discord.otakatsu.studio"> <img src="https://img.shields.io/badge/Discord%20Server-pink?style=for-the-badge" width="220" height="38.45"/></a></p>
<p align="center"><a href="https://telegram.otakatsu.studio"> <img src="https://img.shields.io/badge/Telegram%20Channel-pink?style=for-the-badge" width="220" height="38.45"/></a></p>


## Installation
```$ pip install Peakpx```

## Usage
```
from Peakpx import PeakPx

px = PeakPx()

#get wallpapers
wallpapers = px.get_wallpapers() #it will return a list of wallpapers

#pagination 
wallpapers = px.get_wallpapers(page=2) #by deafult its one

#search wallpapers
wallpapers = px.search_wallpapers(query='one piece') #you can also paas a page parameter here like page =2 by default its 1
```


