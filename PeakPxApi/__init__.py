import requests
from bs4 import BeautifulSoup

class PeakPx:
    def __init__(self):
        self.url = 'https://www.peakpx.com'
    
    def get_wallpapers(self,page : int = 1):
        p = {'page' : page}
        r = requests.get(f'{self.url}/',params=p) 
        soup = BeautifulSoup(r.content,'html.parser')
        search = soup.find_all('img')
        all_links = []
        for link in search:
            try:
                if link:
                    img = str(link.get('data-srcset')).split()[0]
                    if img.endswith('jpg') or img.endswith('png'):
                        to_add = dict(url=img) 
                        all_links.append(to_add)
            except:
                continue
        return all_links
    
    def search_wallpapers(self,query : str,page : int = 1):
        p = {'q' : query,'page' : page}
        r = requests.get(f'{self.url}/en/search',params=p)
        soup = BeautifulSoup(r.content,'html.parser')
        search = soup.find_all('img')
        all_links = []
        for link in search:
            try:
                if link:
                    img = str(link.get('data-srcset')).split()[0]
                    if img.endswith('jpg') or img.endswith('png'):
                        to_add = dict(url=img) 
                        all_links.append(to_add)
            except:
                continue
        return all_links


