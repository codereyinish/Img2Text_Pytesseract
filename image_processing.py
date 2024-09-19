import cv2
import pytesseract
# import asyncio
def getTextFromImage(img):
  grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  ret, thresh1 = cv2.threshold(grayImg, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
  rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,25))
  contours, heirarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
  grayImg2 = grayImg.copy()
  cnt_list = [] #stores output text and its position co-ordinate(x,y)
  for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

  #Drawing the fixed definite Rectangle Boundary around the irregular shaped contour
  rect = cv2.rectangle(grayImg2,(x,y), (x+w, y+h), (0,255,0),2)
  #Drawing the circle to mark the start of the text region
  cv2.circle(grayImg2,(x,y), 8, (255,255,0), 8)
  #do 2D Numpy slicing to only get the detected text region, that means to slice out the rectangle boundary by using its boundary co-ordinates
  croppedImgRegions = grayImg2[y:y+h, x:x+w]
  #Now apply OCR on the cropped image
  text = pytesseract.image_to_string(croppedImgRegions)
  cnt_list.append([x,y, text])
  #this function sorts the text block from top to bottom(stick with y for now, x later if needed)
  sorted_list = sorted(cnt_list, key = lambda x: x[1])
  file = open("scanned_textfile", "w+")
  file.write("")
  file.close()

  for(x,y,text) in sorted_list:
    file = open("scanned_textfile", "w")
    #appending the text
    file.write(text)
    file.write("\n")
    file.close()
  with open("scanned_textfile", "r") as f:
    textContent = f.read()
    return textContent

