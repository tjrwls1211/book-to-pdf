import os
import re
from PIL import Image
from fpdf import FPDF

# 숫자 포함된 문자열 정렬을 위한 유틸
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    """이미지 파일 이름을 자연스럽게 정렬 (예: 1.png, 2.png, ..., 10.png)"""
    return [atoi(c) for c in re.split(r'(\d+)', text)]

# 설정 부분 -----------------------------------------
pdf_name = "book_scan.pdf"  # 출력될 PDF 파일명
img_folder = r"C:/Users/YourUsername/BookScan"  # 이미지 폴더 경로 (반드시 수정)
# --------------------------------------------------

# 이미지 파일 정렬
image_files = sorted(
    [f for f in os.listdir(img_folder) if f.lower().endswith(".png")],
    key=natural_keys
)

# PDF 객체 생성 (pt 단위: 이미지 픽셀과 호환 용이)
pdf = FPDF(unit="pt")

# 이미지 순회하며 페이지 추가
for file in image_files:
    path = os.path.join(img_folder, file)
    img = Image.open(path)
    w, h = img.size  # 이미지 크기에 맞춰 페이지 크기 지정
    pdf.add_page(format=(w, h))
    pdf.image(path, 0, 0, w, h)

# PDF 저장
pdf.output(pdf_name)
print(f"PDF 생성 완료: {pdf_name}")
