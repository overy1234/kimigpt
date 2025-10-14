# 🚨 토스 링크 만들기 - 문제 해결 가이드

## ❌ 토스 링크가 안 만들어지는 이유

### 가능한 원인:
1. 토스 앱 버전이 오래됨
2. 계좌가 연동되지 않음
3. 본인인증이 안됨
4. 기능을 찾을 수 없음

---

## ✅ 해결 방법

### 방법 1: 토스 앱에서 송금 링크 만들기 (가장 쉬움)

#### 단계별 설명:

1. **토스 앱 업데이트**
   - Play Store / App Store
   - 최신 버전으로 업데이트

2. **토스 앱 열기**

3. **하단 메뉴에서 "전체" 클릭**

4. **"송금" 또는 "이체" 찾기**

5. **"내 송금링크" 또는 "송금받기" 선택**
   - 버전에 따라 이름이 다를 수 있음

6. **링크 만들기**
   - 원하는 계좌 선택
   - 링크 생성 버튼 클릭

7. **링크 복사**
   - 생성된 링크: `https://toss.me/아이디`

---

### 방법 2: 토스뱅크 계좌번호 직접 공개 (가장 확실)

토스 링크가 안 만들어지면, **계좌번호를 직접 공개**하는 것이 더 간단합니다!

#### 장점:
- ✅ 링크 생성 필요 없음
- ✅ 토스뱅크 계좌만 있으면 됨
- ✅ 사용자가 토스 앱에서 계좌번호로 송금

#### 설정:

`templates/donate.html` 파일 수정:

```html
<!-- 토스 링크 대신 계좌 정보만 표시 -->
<div class="donate-section">
    <h2>💳 토스로 후원하기</h2>
    <p style="margin-bottom: 20px;">
        토스 앱에서 아래 계좌번호로 송금해주세요!
    </p>
    <div class="account-info">
        <p><strong>토스뱅크</strong></p>
        <p style="font-size: 24px; font-weight: bold; color: #0064FF;">
            1000-1234-5678
        </p>
        <p>예금주: 홍길동</p>
    </div>
    <p style="font-size: 14px; opacity: 0.7; margin-top: 15px;">
        💡 토스 앱 → 송금 → 계좌번호 입력 → 금액 입력 → 송금
    </p>
</div>
```

---

### 방법 3: 카카오페이 QR 코드 (대안)

토스가 안 되면 **카카오페이**를 사용하세요!

#### 단계:
1. **카카오페이 앱 열기**
2. **"받기"** 선택
3. **"QR코드 받기"** 클릭
4. **QR 코드 저장** (스크린샷)
5. **링크 복사** (공유하기)

#### 설정:
```html
<a href="https://qr.kakaopay.com/Ej8KNE838" target="_blank" class="donate-button kakaopay">
    카카오페이로 후원하기
</a>
```

---

### 방법 4: 네이버페이 송금 링크

#### 단계:
1. **네이버 앱** 또는 **네이버페이** 앱 열기
2. **페이** 탭
3. **송금** → **내 송금 링크**
4. 링크 생성 및 복사

---

### 방법 5: 간단한 계좌 공개 (추천!) ⭐

**가장 쉽고 확실한 방법:**

```html
<div class="donate-section">
    <h2>💰 후원 계좌</h2>
    <div class="account-info">
        <p><strong>토스뱅크</strong></p>
        <p style="font-size: 28px; font-weight: bold; color: #0064FF; margin: 15px 0;">
            1000-1234-5678
        </p>
        <p style="font-size: 18px;">예금주: 홍길동</p>
    </div>
    
    <div style="margin-top: 30px; padding: 20px; background: rgba(255,255,255,0.05); border-radius: 12px;">
        <p style="font-size: 14px; line-height: 1.8;">
            📱 <strong>토스로 송금하기:</strong><br>
            토스 앱 → 송금 → 계좌번호 입력 → 금액 입력<br><br>
            
            💳 <strong>다른 은행에서도 가능:</strong><br>
            카카오뱅크, KB국민, 신한, 우리 등 모든 은행
        </p>
    </div>
</div>
```

---

## 🎯 즉시 적용 가능한 코드

`templates/donate.html` 파일을 다음과 같이 수정하세요:

```html
<div class="donate-section">
    <h2>💳 간편 후원 (토스/카카오페이)</h2>
    
    <div class="account-info" style="margin: 30px 0;">
        <p style="font-size: 16px; opacity: 0.8; margin-bottom: 15px;">
            토스뱅크 계좌번호
        </p>
        <p style="font-size: 32px; font-weight: bold; color: #0064FF; letter-spacing: 2px; margin: 20px 0;">
            1000-1234-5678
        </p>
        <p style="font-size: 20px; font-weight: 600;">
            예금주: 홍길동
        </p>
    </div>

    <div style="background: rgba(0, 100, 255, 0.1); padding: 20px; border-radius: 12px; margin: 20px 0;">
        <p style="font-size: 15px; line-height: 2;">
            <strong>💡 토스 앱에서 송금하는 방법:</strong><br>
            1️⃣ 토스 앱 열기<br>
            2️⃣ 하단 "송금" 또는 "이체" 클릭<br>
            3️⃣ 계좌번호 입력: <strong>1000-1234-5678</strong><br>
            4️⃣ 토스뱅크 선택<br>
            5️⃣ 금액 입력 후 송금!
        </p>
    </div>

    <p style="font-size: 13px; opacity: 0.7; margin-top: 20px;">
        * 토스뱅크가 없어도 다른 은행 앱에서도 송금 가능합니다
    </p>
</div>
```

---

## 💡 추가 팁

### 1. 토스뱅크 계좌 개설
- 토스 앱에서 5분 만에 계좌 개설 가능
- 완전 무료
- 추천인 코드: (있다면)

### 2. 다양한 결제 수단 제공
```
✅ 토스뱅크 (계좌번호)
✅ 카카오페이 (QR 코드)
✅ 일반 계좌 이체
✅ PayPal (해외)
✅ Buy Me a Coffee
```

### 3. QR 코드 직접 생성
- https://www.qr-code-generator.com/
- 계좌번호를 QR로 변환
- 이미지로 저장 후 업로드

---

## 🚀 지금 바로 적용하기

토스 링크가 안 만들어진다면:

1. ✅ **계좌번호 직접 공개** (가장 쉬움)
2. ✅ **카카오페이 사용** (QR 코드)
3. ✅ **여러 결제 수단 제공** (선택의 폭 넓히기)

---

## 📞 문제가 계속되면?

### 토스 고객센터:
- 앱 내 채팅 상담
- 전화: 1599-4905
- 24시간 운영

### 대안:
1. **카카오페이** 사용
2. **네이버페이** 사용
3. **일반 은행 계좌** 공개
4. **PayPal** (해외 후원)
5. **Buy Me a Coffee** (전문 후원 플랫폼)

---

계좌번호만 공개해도 충분히 후원받을 수 있습니다! 🎉
