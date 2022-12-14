from pytube import YouTube

def Download(link):
  ytObject=YouTube(link);
  ytObject=ytObject.streams.get_highest_resolution()
  try:
    ytObject.download()
  except:
    print("Error occurred during download process")
  print("Video has been downloaded check it out go!!!!!!!!!! 👍")
    
link=input("plz enter the YT video link here: ")
Download(link)