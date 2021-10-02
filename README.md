# Spotify-Emotional-Linker
__OVERVIEW__
In general terms my code  uses the cv2 python library to recognize faces through a pre-trained
facial recognizer. Once the faces are recognized, it classifies  the type of faces depending on the emotion.The  emotions were pre recorded in the data folder full of images, so the code  in general terms is just comparing fotos. 
The code is able to distinguish among: angriness, seriousness, amazeness, sadness, and happiness.
Once the recognizer identifies an emotion (different from seriousness) it will send the name to the Spotify  function which is waiting for a specific emotion to play a  song related to your mood.


__FIRST SCRIPT__
**reconocimientofacial.py**
In this script I used three principal libraries: cv2, os ,and imutils.
First, I created a data folder which contains all the  faces linked to a specific emotion. After the folder has been created, the code will activate the camera through the “cv2.VideoCapture(0)” to capture your current face expression using it to I call  a pre-train frontal face recognizer
stored in the `faceClassifier` variable. This classifier allows the program  to recognize faces in a specific angle, in this case it is only for frontal faces. I decided to just use the frontal face model because the code is supposed to work while using a computer.

Inside the while loop I am resizing all the frames that the `cap` variable is loading. Then the code turns all the frames detected into gray scale so that the classifier will be able to detect the frontal faces and store them inside the “faces” variable in a 1.3 scale size.
For each face detected, I set up a rectangle around it (this is what the for loop does) and then give it a specific “key name” to store it inside the emotion folder. Once I got 300 hundred images of a respective emotion (count variable keeps count of the faces) the code breaks.

__SECOND SCRIPT__
**entrenamiento.py**
This is a short script. In general terms I am training an emotion recognizer using three different methods:
-EigenFaces
-FisherFaces
-LBPH
For training each method the code is first loading the images into “facesDate”, while assigning each one of them a specific label. Then It creates  the `emotion_recognizer` that will store the method to then train it with the images I just loaded into `facesData`. The recognizer is trained by reading all the images  through the specific labels I just assigned.
After the recognizer is created the code will show the training time and then it will store the recognizer inside an “xml” file with the name of the specific method used, so that I can later access it in the third script.

 __THIRD SCRIPT__
**FacialRecognizer.py**
libraries used:
-cv2
-os
-numpy
-spotipy
-sys
-webbrowser

Once again, I access the data folder with all the emotions, loading each one of the faces stored into the “faces” variable. At the same time the code is  loading the method meant  to be used for recognizing the emotions. Then inside the “for loop” I am constantly checking for the method
being used. I normally prefer to use”`LBPH ''  due  to its accuracy in the detection so as to prevent the code from errors, still it works with any method specified.
The program will compare the face to one of the faces stored in the data folder.  If it detects a match  it will show the name of the emotion related to the folder.
The name of the emotion detected is then sent to the “variable”  which calls the function “OpenSpotify”.

How does the Spotify function work?
It uses the spotify free developers’ software online  which gives you a specific ID and client secret to let you use your spotify account for coding purposes.
The function spotify  takes as  argument the name of the emotion the recognizer detected. The emotion acquired will be used to enter the ramification assigned to its name (one of the if statements).
 I created a list of songs that I want to listen to depending on my “Emotional state”. With “sp” I open Spotify, while with “result” the code stores the result search of Ariana Grande (it could be any author I just used her for personal reasons). Then,  inside the for loop, just like in an
html code spotify has tags,so the program is  checking for each song that appears in the search using the "tags" supplied by spotify. Once all the songs are stored in the “name song” list, the code starts checking for each song until it is equal to the specific song required to the emotion. At last, the “web.open” allows the program  to play the song and the “h” variable is used to  break the code  by initializing it to 27 and with it closing the camera.
__NOW YOU CAN LISTEN TO A SONG JUST DEPENDING ON HOW YOU FEEL! __

**P.d: The code could work a little better using `threads` but for time purposes (I am still at school and work) using threads wasn't an option for me due to the complex ramification process it requires. Consequently, as an alternative, I had to keep “seriousness” as a “none result” so the code wouldn’t break every time it runs. **

