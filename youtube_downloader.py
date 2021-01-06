from pytube import YouTube
url = input("url:")
eval(f"YouTube('{url}').streams.first().download()")
#eval("YouTube('%s').streams.first().download()"%(url))
#lol