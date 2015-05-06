import cv2
from image import Image 
from facedetector import FaceDetector 


images = ["images/1.jpg","images/2.jpg", "images/3.jpg"]

def detect_faces():
	for img_path in images:
		img = Image(img_path, 1).load()
		detector = FaceDetector(img, 1.1, 5, (30, 30), cv2.cv.CV_HAAR_SCALE_IMAGE)
		detector.detect_faces()
		cv2.imshow(images[0], img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()


if __name__ == '__main__':
	detect_faces()