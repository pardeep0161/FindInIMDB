import webbrowser
import re


string = "Escape.Plan.2013.1080p.BluRay.x264.YIFY"

searchString = re.search(r'',string).group().replace('.', ' ')

webbrowser.open('www.google.com',new=0)
