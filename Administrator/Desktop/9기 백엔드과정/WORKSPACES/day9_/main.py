# 이미지 회전
import cv2

# 이미지 읽기
img = cv2.imread('input.jpg')
# 이미지 중심을 기준으로 90도 회전
height, width = img.shape[:2]
center = (width / 2, height / 2)
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=90, scale=1)
rotated_img = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))
# 회전된 이미지 표시
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()