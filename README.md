# Book to PDF Converter

Python 스크립트를 이용해 **여러 장의 PNG 이미지**를 하나의 PDF 파일로 변환합니다.  
책 스캔본, 문서 스캔, 필기 자료 등을 PDF로 정리하고 싶을 때 사용합니다.

---

## 기능 소개

- PNG 이미지들을 순서대로 PDF로 병합
- 숫자가 포함된 파일명을 자연스러운 순서(natural sort)로 정렬
- 각 이미지 크기에 맞게 PDF 페이지 크기 자동 조정
---

## 사용 방법

### 1. 이미지 준비
- PNG 파일들을 한 폴더에 넣습니다.
- **파일명을 숫자 순서** (`1.png`, `2.png`, `10.png` 등)로 정리해 주세요.

### 2. 코드 수정
`book_to_pdf.py` 파일에서 다음 부분을 본인 경로에 맞게 수정합니다:

```python
img_folder = r"C:/Users/YourUsername/Downloads/BookScan"
pdf_name = "book_scan.pdf"
```

### 3. 실행
```bash
python book_to_pdf.py
```

PDF가 실행 경로에 생성됩니다.

---

## 설치 필요 라이브러리

```bash
pip install pillow fpdf2
```

> `fpdf2`를 설치해야 `add_page(format=(w, h))` 기능이 정상 작동합니다.

---

##  예시

```bash
📂 BookScan/
 ├── 1.png
 ├── 2.png
 ├── 3.png
 └── ...
```

실행 결과:
```
PDF 생성 완료: book_scan.pdf
```

