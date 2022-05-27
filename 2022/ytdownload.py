from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=0FcU9xT-qqA")
#streams = yt.streams.filter(resolution="2160p",file_extension="mp4").first()
#streams.download("C:/Users/Fox/Desktop")
for i in yt.streams.filter(file_extension="webm"):
    print(i)
