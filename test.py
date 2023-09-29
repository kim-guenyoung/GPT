from PIL import Image, ImageDraw, ImageFont

# 이미지 업로드 및 포스터 생성
def create_poster(image_path, text):
    # 이미지 열기
    img = Image.open(image_path)

    # 이미지에 텍스트 추가
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("AppleGothic.ttf", size=36)  # 원하는 폰트와 크기로 설정
    text_color = (255, 255, 255)  # 텍스트 색상 (RGB)

    # 텍스트를 이미지 중앙에 배치 (가로 중앙, 아래쪽)
    text_width, text_height = draw.textsize(text, font)
    image_width, image_height = img.size
    x = (image_width - text_width) / 2
    y = image_height - text_height - 20  # 이미지 하단에 텍스트 배치, 여유 공간을 위해 -20 추가

    draw.text((x, y), text, fill=text_color, font=font)

    # 이미지 저장 또는 표시
    img.save("poster.png")  # 포스터 이미지 저장
    img.show()  # 이미지 표시

# 이미지 경로와 텍스트 설정
image_path = "/Users/kimgeunyoung/2학년 2학기/웹프로그래밍/33-1.png"  # 이미지 파일 경로를 여기에 입력하세요.
poster_text = """
농산물 판매 포스터

🌾 무료배송 🚚
🌿 유기농 제품 🌱

우리의 신선한 농산물을 만나보세요! 저희 제품은 유기농 방식으로 재배되었으며, 무료 배송 서비스로 편리하게 받아보실 수 있습니다. 건강하고 맛있는 농산물을 저렴하게 구매하세요.

주문 및 자세한 정보는 저희 웹사이트를 방문하시거나 아래 연락처로 문의해주세요.

📞 연락처: 123-456-7890
🌐 웹사이트: www.example.com
"""

# 포스터 생성 함수 호출
create_poster(image_path, poster_text)
