import cv2
import os 
import numpy as np 
import time

def obtainModel(method, facesData, labels):
	if method == 'EigenFaces': emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
	if method == 'FisherFaces': emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
	if method == 'LBPH': emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

	#training recognizer
	print('Training ('+method+')...' )
	inicio = time.time()
	emotion_recognizer.train(facesData, np.array(labels))
	trainingTime = time.time() - inicio
	print('Training time of ('+method+') = ' ,trainingTime)

	#saving model 
	emotion_recognizer.write('modelo'+method+'.xml')



dataPath = 'C:/Users/elisa/Desktop/Final proyect/reconocimientoEmocional/data'
emotionList = os.listdir(dataPath)
print('Lista de emociones: ', emotionList)

labels = []
facesData =[]
label = 0 

for nameDir in emotionList:
	emotionPath = dataPath + '/' + nameDir
	print('leyendo imagenes')

	for filename in os.listdir(emotionPath):
		#print('Rostros', nameDir + '/' + filename)
		labels.append(label)
		facesData.append(cv2.imread(emotionPath + '/' + filename,0))
		#image = cv2.imread(emotionPath + '/' + filename,0)
		#cv2.imshow('image', image)
		#cv2.waitKey(10) 
	label = label + 1

#print ('labels=', labels)


#modelos de entrenamiento
#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
#face_recognizer = cv2.face.LBPHFaceRecognizer_create()

#training

#print('Entrenando..')
#face_recognizer.train(facesData, np.array(labels))

#almacenando el modelo
#face_recognizer.write('modeloEigenFace.xml')
#print('almacenando el modelo..')
obtainModel('EigenFaces', facesData, labels)
obtainModel('FisherFaces', facesData, labels)
obtainModel('LBPH', facesData, labels)

