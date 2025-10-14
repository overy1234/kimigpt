# 📸 토스 QR 코드 이미지 설정 가이드

## 🎯 준비물
- `tossqr.jpg` 파일 (토스 송금 QR 코드 이미지)

---

## 📁 파일 위치

### 1. 이미지 파일을 다음 경로에 넣으세요:
```
c:\bivecoding\kimigpt\static\images\tossqr.jpg
```

### 2. 폴더 구조:
```
kimigpt/
├── app.py
├── templates/
│   ├── index.html
│   ├── donate.html
│   └── ...
└── static/
    └── images/
        └── tossqr.jpg  ← 여기에 QR 이미지 넣기!
```

---

## 🖼️ 토스 QR 코드 만드는 방법

### 방법 1: 토스 앱에서 생성

1. **토스 앱 열기**
2. **송금** 탭 클릭
3. **내 계좌** 또는 **QR로 받기** 선택
4. **QR 코드 생성**
5. **스크린샷** 또는 **저장하기**
6. 이미지를 `tossqr.jpg`로 이름 변경
7. `static/images/` 폴더에 복사

### 방법 2: 토스 송금 링크를 QR로 변환

만약 토스 송금 링크가 있다면:
- 예: `https://toss.me/yourname`

#### QR 코드 생성 사이트:
1. https://www.qr-code-generator.com/
2. https://www.qrcode-monkey.com/
3. https://goqr.me/

**단계:**
1. 위 사이트 접속
2. URL 입력: `https://toss.me/yourname`
3. 크기: 500x500 픽셀 이상 권장
4. 다운로드 (JPG 또는 PNG)
5. `tossqr.jpg`로 이름 변경
6. `static/images/` 폴더에 복사

---

## 💡 이미지 요구사항

### 권장 사양:
- **형식**: JPG 또는 PNG
- **크기**: 500x500 픽셀 이상
- **용량**: 500KB 이하
- **배경**: 밝은 색 (흰색 권장)
- **QR 코드**: 선명하고 깨끗하게

### 파일명:
- 반드시 `tossqr.jpg` (소문자)
- 다른 이름이면 코드에서 수정 필요

---

## 🔧 이미지 파일명이 다른 경우

만약 `tossqr.png` 또는 다른 이름을 사용한다면:

`templates/donate.html` 파일에서:

```html
<!-- 이 부분 찾아서 -->
<img src="{{ url_for('static', filename='images/tossqr.jpg') }}" 

<!-- 실제 파일명으로 변경 -->
<img src="{{ url_for('static', filename='images/tossqr.png') }}"
```

---

## 📱 QR 코드 테스트

### 1. 이미지 확인:
브라우저에서 직접 접속:
```
http://localhost:5000/static/images/tossqr.jpg
```

이미지가 보이면 성공! ✅

### 2. 후원 페이지 확인:
```
http://localhost:5000/donate
```

QR 코드가 표시되는지 확인

### 3. 토스 앱에서 테스트:
1. 토스 앱 열기
2. 송금 → QR 스캔
3. 컴퓨터 화면의 QR 코드 스캔
4. 송금 화면 나오면 성공!

---

## ⚠️ 문제 해결

### 이미지가 안 보이는 경우:

#### 1. 파일 경로 확인
```python
# app.py에 추가 (이미 있어야 함)
app = Flask(__name__)
```

#### 2. static 폴더 구조 확인
```
static/
└── images/
    └── tossqr.jpg
```

#### 3. 파일 권한 확인
- 읽기 권한이 있는지 확인
- 파일이 손상되지 않았는지 확인

#### 4. 캐시 문제
- 브라우저 새로고침: Ctrl + F5
- 또는 다른 브라우저에서 테스트

#### 5. 서버 재시작
```bash
# 서버 종료 후 재시작
python app.py
```

---

## 🎨 QR 코드 디자인 팁

### 더 예쁘게 만들기:
1. **프레임 추가**: "Scan me" 등의 텍스트
2. **색상 변경**: 토스 파란색 (#0064FF)
3. **로고 삽입**: 중앙에 작은 로고
4. **라운드 코너**: 모서리를 둥글게

**추천 도구:**
- Canva (https://canva.com)
- Figma (https://figma.com)
- QR Code Monkey (커스터마이징 가능)

---

## 📊 QR 코드 vs 계좌번호

### QR 코드 장점:
- ✅ 빠르고 간편
- ✅ 오타 없음
- ✅ 스마트폰에 최적화

### 계좌번호 장점:
- ✅ 모든 은행 지원
- ✅ QR 인식 불가 시 대안
- ✅ 복사/붙여넣기 가능

**→ 둘 다 제공하는 것이 best!** (현재 구현됨)

---

## 🚀 체크리스트

배포 전 확인사항:
- [ ] `tossqr.jpg` 파일을 `static/images/` 폴더에 넣었나?
- [ ] 파일명이 정확한가? (소문자, .jpg)
- [ ] 이미지가 선명한가? (500x500 이상)
- [ ] 브라우저에서 이미지가 보이나?
- [ ] 토스 앱에서 QR 스캔이 되나?
- [ ] 실제 계좌번호도 정확히 입력했나?
- [ ] 예금주 이름도 정확한가?

---

## 💰 추가 개선 아이디어

### 1. 여러 결제 수단 QR 코드
```
tossqr.jpg - 토스 QR
kakaopayqr.jpg - 카카오페이 QR
naverpayqr.jpg - 네이버페이 QR
```

### 2. QR 코드 갤러리
사용자가 원하는 결제 수단 선택

### 3. 동적 QR 생성
금액별로 다른 QR 코드 생성

---

## 📞 도움이 필요하면

### 토스 고객센터:
- 앱 내 채팅 상담
- 전화: 1599-4905

### QR 코드 문제:
- 조명 확인 (너무 어둡거나 밝으면 인식 안 됨)
- 화면 밝기 최대로
- QR 코드 이미지 화질 확인

---

파일을 올바른 위치에 넣고 서버를 재시작하면 됩니다! 🎉
