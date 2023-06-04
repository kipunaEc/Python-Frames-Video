import cv2
 
#Leer imagenes
img1 = cv2.imread('IMG_0001.jpg')
img2 = cv2.imread('IMG_0002.jpg')
img3 = cv2.imread('IMG_0003.jpg')
img4 = cv2.imread('IMG_0004.jpg')
img5 = cv2.imread('IMG_0005.jpg')
img6 = cv2.imread('IMG_0006.jpg')
 
#Dimensiones de la última imagen alto y ancho
height, width  = img6.shape[:2]
 
#Caracteristicas del video
video = cv2.VideoWriter('video1.mp4',cv2.VideoWriter_fourcc(*'mp4v'),2,(width,height))
 
# Poner cada frame en video
video.write(img1)
video.write(img2)
video.write(img3)
video.write(img4)
video.write(img5)
video.write(img6)
 
#liberar recursos
video.release()
