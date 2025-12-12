import cv2

def apply_mosaic(img, faces, ratio=0.05):
    """찾은 얼굴 영역에 모자이크 처리를 하는 함수"""
    result_img = img.copy()
    
    for (x, y, w, h) in faces:
        # 얼굴 영역 자르기
        roi = result_img[y:y+h, x:x+w]
        
        # 1. 아주 작게 축소 (정보 손실)
        small = cv2.resize(roi, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        
        # 2. 다시 원래 크기로 확대 (픽셀 깨짐 효과 = 모자이크)
        mosaic = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
        
        # 원본 이미지에 덮어쓰기
        result_img[y:y+h, x:x+w] = mosaic
        
    return result_img