from ultralytics import YOLOv10
import os

MODEL_PATH = 'yolov10n.pt'
model = YOLOv10(MODEL_PATH)
IMG_PATH = './images/HCMC_Street.jpg'
OUTPUT_PREDICTED_PATH = './images/'
result = model(source=IMG_PATH)[0]
result.save(OUTPUT_PREDICTED_PATH + 'HCMC_Street_predict.jpg')

# YOUTUBE_VIDEO_PATH = 'https://www.youtube.com/watch?v=wqPSsu7XQ74'
YOUTUBE_VIDEO_PATH = "https://rr2---sn-4g5lznle.googlevideo.com/videoplayback?expire=1719941581&ei=beWDZovNB62ji9oP7ZuRyAs&ip=148.251.137.140&id=o-AOWuN0WeM7eiMxFf9wdI5lvQGqhxatCa1dvi6fvvTRTR&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=e-&mm=31%2C29&mn=sn-4g5lznle%2Csn-4g5ednsr&ms=au%2Crdu&mv=m&mvi=2&pl=21&initcwndbps=543750&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&cnr=14&ratebypass=yes&dur=39.543&lmt=1719878312275328&mt=1719919515&fvip=5&c=ANDROID_TESTSUITE&txp=5309224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRAIgD0KT3UWdd7aTZyaOpwtTfUVOT-pcypwAZ4cSk6Ctt80CIBNL8BpS-8XYqTC1YIl493X8kYFXMht_Vtar-PoUTNg-&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHlkHjAwRQIhAOAeQCXFZqF2Uvidx1_TlNdAVd49NltkEnwy09jMcoNBAiAes4jO3Mg5wGNT7TqVl1-l82sXuLoniXez713caA_nFw%3D%3D&title=How%20to%20cross%20a%20street%20in%20Ho%20Chi%20Minh%20City%20(Saigon)%2C%20Vietnam"
video_result = model(source=YOUTUBE_VIDEO_PATH)

OUTPUT_VIDEO_PATH = "./video_images"

if not os.path.exists(OUTPUT_VIDEO_PATH):
  os.makedirs(OUTPUT_VIDEO_PATH)

for i, img in enumerate(video_result):
  video_result[i].save('./video_images/' + f"frame_{i}.jpg")
