# utils.py
import cv2

def load_image(filepath):
    """이미지 파일을 불러오는 함수"""
    img = cv2.imread(filepath)
    if img is None:
        print(f"Error: {filepath} 파일을 찾을 수 없습니다.")
        return None
    return img

def save_image(img, filename="result.jpg"):
    """결과 이미지를 저장하는 함수"""
    cv2.imwrite(filename, img)
    print(f"이미지가 {filename}으로 저장되었습니다.")