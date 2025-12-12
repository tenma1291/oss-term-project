import cv2
# 팀원들이 만든 모듈을 여기서 불러옵니다 (이게 핵심!)
from utils import load_image, save_image
from detector import detect_faces
from processing import apply_mosaic

def main():
    print("=== 얼굴 모자이크 프로그램 시작 (Team Leader Integration) ===")
    
    # 1. 이미지 준비 (팀원 A 기능 테스트)
    # 테스트할 이미지 이름을 'sample.jpg'로 맞춰주세요.
    img = load_image("god.jpg")
    if img is None:
        return

    # 2. 얼굴 찾기 (팀원 B 기능 테스트)
    print("얼굴을 찾는 중입니다...")
    faces = detect_faces(img)
    print(f"발견된 얼굴 개수: {len(faces)}")
    
    # 3. 모자이크 처리 (팀원 C 기능 테스트)
    print("모자이크 필터 적용 중...")
    result_img = apply_mosaic(img, faces)
    
    # 4. 결과 보여주기 및 저장
    cv2.imshow("Final Result", result_img)
    save_image(result_img, "final_result.jpg")
    
    print("작업 완료! 아무 키나 누르면 종료됩니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()