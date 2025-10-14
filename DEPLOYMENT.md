# 🚀 무료 배포 가이드

이 프로젝트를 무료로 배포할 수 있는 방법들입니다.

## 📦 배포 옵션

### 1. Render (추천! 가장 쉬움) ⭐

**장점:**
- 완전 무료 (Free tier)
- 자동 배포
- SSL 인증서 자동
- 간단한 설정

**단점:**
- 15분 동안 요청이 없으면 슬립 모드 (첫 요청 시 깨어나는데 시간 소요)

**배포 방법:**

1. GitHub에 코드 업로드
2. [Render](https://render.com) 가입
3. "New +" → "Web Service" 클릭
4. GitHub 저장소 연결
5. 설정:
   - **Name**: `kimi-chat` (원하는 이름)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment Variables** 추가:
     - Key: `HF_TOKEN`
     - Value: `your_huggingface_token_here`
6. "Create Web Service" 클릭

완료! 몇 분 후 URL이 제공됩니다 (예: `https://kimi-chat.onrender.com`)

---

### 2. Railway.app 🚂

**장점:**
- 무료 티어 $5 크레딧/월
- 빠른 배포
- 슬립 모드 없음

**배포 방법:**

1. [Railway](https://railway.app) 가입
2. "New Project" → "Deploy from GitHub repo"
3. 저장소 선택
4. Environment Variables 추가:
   - `HF_TOKEN`: `your_huggingface_token_here`
5. 자동으로 배포 시작

---

### 3. Vercel (프론트엔드 최적화) ⚡

**장점:**
- 매우 빠름
- 무료 티어 관대함
- 자동 HTTPS

**주의:** Flask 앱을 ASGI로 변환 필요

**배포 방법:**

1. [Vercel](https://vercel.com) 가입
2. `vercel.json` 파일이 이미 준비되어 있음
3. Vercel CLI 설치:
   ```bash
   npm i -g vercel
   ```
4. 배포:
   ```bash
   vercel
   ```
5. Environment Variable 설정:
   - Vercel Dashboard → Settings → Environment Variables
   - `HF_TOKEN` 추가

---

### 4. PythonAnywhere 🐍

**장점:**
- Python 특화 플랫폼
- 무료 티어 항상 활성

**단점:**
- 느린 시작 시간
- 제한적인 무료 티어

**배포 방법:**

1. [PythonAnywhere](https://www.pythonanywhere.com) 가입
2. "Web" 탭에서 "Add a new web app"
3. Flask 선택
4. 코드 업로드 및 설정

---

### 5. Fly.io 🪁

**장점:**
- 무료 티어 좋음
- 전 세계 배포 가능

**배포 방법:**

1. [Fly.io](https://fly.io) 가입
2. Fly CLI 설치
3. `fly launch` 실행
4. Environment Variable 설정:
   ```bash
   fly secrets set HF_TOKEN=your_huggingface_token_here
   ```

---

## 🎯 추천 순위

1. **Render** - 가장 쉽고 안정적 (초보자 추천)
2. **Railway** - 빠르고 슬립 없음
3. **Vercel** - 속도 최우선
4. **Fly.io** - 글로벌 배포
5. **PythonAnywhere** - Python 전용

---

## 📝 GitHub에 업로드하기

배포 전에 먼저 GitHub에 올려야 합니다:

```bash
# Git 초기화
git init

# 파일 추가 (.gitignore가 .env를 자동으로 제외)
git add .

# 커밋
git commit -m "Initial commit: Kimi-K2 Chat App"

# GitHub에서 새 저장소 만든 후
git remote add origin https://github.com/your-username/kimi-chat.git
git branch -M main
git push -u origin main
```

---

## ⚠️ 중요 사항

### 환경 변수 설정
배포 시 반드시 `HF_TOKEN` 환경 변수를 설정해야 합니다:
- 값: `your_huggingface_token_here` (실제 토큰으로 교체)

### .env 파일 주의
`.env` 파일은 `.gitignore`에 포함되어 있어 GitHub에 올라가지 않습니다.
각 배포 플랫폼에서 직접 환경 변수로 설정해야 합니다.

---

## 🔧 문제 해결

### 502 Bad Gateway
- `gunicorn` 설치 확인: `pip install gunicorn`
- `Procfile` 확인

### API 오류
- 환경 변수 `HF_TOKEN`이 제대로 설정되었는지 확인
- Hugging Face 토큰이 유효한지 확인

### 느린 응답
- 무료 티어의 제한일 수 있음
- Render는 슬립 모드에서 깨어나는데 시간이 걸림

---

## 💰 비용

모든 플랫폼 **완전 무료**로 사용 가능!
- Render: 완전 무료 (슬립 모드 있음)
- Railway: $5/월 크레딧 제공
- Vercel: 넉넉한 무료 티어
- Fly.io: 무료 티어 제공

---

## 🎨 커스텀 도메인 (선택사항)

대부분의 플랫폼에서 커스텀 도메인 연결 가능:
1. 도메인 구매 (Namecheap, GoDaddy 등)
2. 플랫폼 설정에서 도메인 추가
3. DNS 레코드 설정

무료 도메인: [Freenom](https://freenom.com)

---

질문이 있으면 GitHub Issues에 남겨주세요! 🚀
