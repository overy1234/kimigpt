# Vercel 배포 가이드

## 🚀 빠른 배포 방법

### 1단계: GitHub에 코드 업로드

```bash
# Git 초기화 (이미 했다면 스킵)
git init

# 모든 파일 추가
git add .

# 커밋
git commit -m "Kimi-K2 Chat App for Vercel"

# GitHub에서 새 저장소 만들기 (https://github.com/new)
# 그 다음 아래 명령어 실행 (your-username을 실제 사용자명으로 변경)
git remote add origin https://github.com/your-username/kimi-chat.git
git branch -M main
git push -u origin main
```

### 2단계: Vercel 배포

#### 방법 A: Vercel 웹사이트 사용 (추천)

1. [Vercel](https://vercel.com) 가입/로그인
2. "Add New..." → "Project" 클릭
3. GitHub 계정 연결
4. 저장소 `kimi-chat` 선택
5. "Deploy" 클릭하기 **전에** 환경 변수 설정:
   - **Environment Variables** 섹션에서:
   - Name: `HF_TOKEN`
   - Value: `your_huggingface_token_here` (실제 토큰으로 교체)
   - Environment: `Production`, `Preview`, `Development` 모두 체크
6. "Deploy" 클릭!

#### 방법 B: Vercel CLI 사용

```bash
# Vercel CLI 설치
npm i -g vercel

# 로그인
vercel login

# 배포
vercel

# 환경 변수 설정
vercel env add HF_TOKEN
# 프롬프트가 나오면 토큰 입력: your_huggingface_token_here
# 환경 선택: Production, Preview, Development 모두 선택

# 다시 배포하여 환경 변수 적용
vercel --prod
```

### 3단계: 완료! 🎉

배포가 완료되면 Vercel이 URL을 제공합니다:
- 예: `https://kimi-chat-xxxx.vercel.app`

## 📝 중요 사항

### 환경 변수 확인
배포 후 작동하지 않으면:
1. Vercel Dashboard → 프로젝트 선택
2. Settings → Environment Variables
3. `HF_TOKEN`이 제대로 설정되었는지 확인
4. 변경 후 다시 배포:
   ```bash
   vercel --prod
   ```

### 재배포
코드 변경 시:
```bash
git add .
git commit -m "Update"
git push
```
Vercel이 자동으로 감지하고 재배포합니다!

## ⚡ Vercel의 장점

- ✅ **초고속 CDN** - 전 세계 어디서든 빠름
- ✅ **자동 HTTPS** - SSL 인증서 자동
- ✅ **자동 배포** - Git push만 하면 자동 배포
- ✅ **무료 도메인** - vercel.app 도메인 무료 제공
- ✅ **프리뷰 배포** - PR마다 미리보기 URL 생성

## 🔧 문제 해결

### "Build failed" 오류
```bash
# requirements.txt 확인
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push
```

### API 작동 안 함
- Vercel Dashboard에서 환경 변수 확인
- Logs 탭에서 에러 확인

### 느린 응답
- 무료 티어는 첫 요청이 느릴 수 있음 (콜드 스타트)
- 사용 중이면 빠름

## 🌐 커스텀 도메인 (선택사항)

1. Vercel Dashboard → 프로젝트 → Settings → Domains
2. 도메인 입력 (예: `mychat.com`)
3. DNS 설정 지시사항 따라하기

## 💰 비용

**완전 무료!**
- Hobby 플랜: 무료
- 대역폭: 100GB/월
- 빌드 시간: 100시간/월
- 충분히 넉넉합니다!

## 📊 모니터링

Vercel Dashboard에서:
- 실시간 로그
- 사용량 통계
- 에러 추적

---

문제가 있으면 [Vercel 문서](https://vercel.com/docs) 참고하세요!
