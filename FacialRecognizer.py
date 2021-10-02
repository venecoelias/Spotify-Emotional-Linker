import cv2
import os 
import numpy as np
import array as arr
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser as web
import time 


#defining the spotify function for searching the song
def openSpotify(emotion):
	
	clientId = '202090dbc03749cb81a924dc99d32c77'
	clientSecret = '20ec88d8c40445ec8420350af6bfc09b'

	author = 'Ariana Grande'
	songs = ['positions','nasty','pov']
	if emotion == 'SERIEDAD' or emotion == 'SORPRESA':
		song = 'none'
	elif emotion == 'TRISTEZA':
		song = songs[0].upper()
	elif emotion == 'ENOJO':
		song = songs[1].upper()
	elif emotion == 'FELICIDAD':
		song = songs[2].upper()

	#searching for author
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(clientId,clientSecret))
	result = sp.search(author)

	for i in range(0, len(result['tracks']['items'])):
	    name_song = result['tracks']['items'][i]['name'].upper()
	    if song in name_song:
	        web.open(result['tracks']['items'][i]['uri'])
	        h = 27
	        return h
	        break
	        
	    else: 
	    	pass



dataPath = 'C:/Users/elisa/Desktop/Final proyect/reconocimientoEmocional/data'
imagePaths = os.listdir(dataPath)
print('imagePaths= ', imagePaths)

#training method 
#method = 'EigenFaces'
#method = 'FisherFaces'
method = 'LBPH'


if method == 'EigenFaces': emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
if method == 'FisherFaces': emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
if method == 'LBPH': emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()


#face_recognizer = cv2.face.EigenFaceRecognizer_create()

#reading model
emotion_recognizer.read('modelo'+method+'.xml')
#---------------------------------------------------------------------

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

variable = 0 
#user_wait = input("Press enter to Spotify: ")

while True: 
	ret, frame = cap.read()
	if ret == False: break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = gray.copy()

	

	faces = faceClassif.detectMultiScale(image=gray,scaleFactor= 1.3, minNeighbors=5,minSize=(30,30))
	

	for (x,y,w,h) in faces: 
		rostro = auxFrame[y:y+h, x:x+w]
		rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
		result = emotion_recognizer.predict(rostro)

		cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

		if method == 'EigenFaces':
			#eigenfaces---------------------------#
			if result[1] < 5700:
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.3,(255,255,0),1,cv2.LINE_AA)			
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

				
			else:
				cv2.putText(frame,'Desconocido',(x,y+35),2,0.8,(0,0,255),1,cv2.LINE_AA)			
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
				
		
		if method == 'FisherFaces':	
			#fisherFaces--------------------------#
			if result[1] < 500:
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.3,(255,255,0),1,cv2.LINE_AA)			
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
				
			else:
				cv2.putText(frame,'Desconocido',(x,y+35),2,0.8,(0,0,255),1,cv2.LINE_AA)			
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
				

		if method == 'LBPH':
			#LBPH------------------------------#
			if result[1] < 70:
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-35),2,1.3,(255,255,0),1,cv2.LINE_AA)			
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
				variable = openSpotify(imagePaths[result[0]].upper())
			else:
				cv2.putText(frame,'Desconocido',(x,y+35),2,0.8,(0,0,255),1,cv2.LINE_AA)			
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)		    
   				
   				         	
    				 
	cv2.imshow('frame', frame)
	k = cv2.waitKey(1)
	j = variable
	if k == 27:
		break
	if j == 27:

		break
	
	

cap.release()
cv2.destroyAllWindows()