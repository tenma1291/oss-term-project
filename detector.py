# detector.py
import cv2

def detect_faces(img):
    """
    이미지에서 얼굴 좌표(x, y, w, h) 리스트를 반환하는 함수
    
    매개변수:
        img (numpy.ndarray): BGR 이미지 배열
    
    반환값:
        faces (list of tuples): 각 얼굴의 (x, y, w, h) 좌표 리스트
    """
    # OpenCV에서 제공하는 사전 학습된 얼굴 인식 모델 불러오기
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # 인식률을 높이기 위해 흑백으로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 얼굴 탐지 (scaleFactor=1.1, minNeighbors=4로 설정)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    
    return faces
