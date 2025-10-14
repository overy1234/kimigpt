# 🤖 KorGPT AI Chat

**IndieCode**가 오픈소스를 활용하여 만든 무료 AI 채팅 서비스입니다.

Hugging Face의 Kimi-K2 API를 기반으로 한 대화형 AI 웹 애플리케이션으로, 누구나 무료로 이용할 수 있습니다.

## 👨‍💻 개발자
**Ryu Keon Kon** (IndieCode)

## 🚀 시작하기

### 1. Hugging Face Token 발급

1. [Hugging Face](https://huggingface.co/)에 가입/로그인
2. [토큰 설정 페이지](https://huggingface.co/settings/tokens)로 이동
3. "New token" 클릭하여 새 토큰 생성
4. Read 권한으로 충분합니다

### 2. 환경 설정

1. `.env.example` 파일을 `.env`로 복사:
   ```bash
   copy .env.example .env
   ```

2. `.env` 파일을 열어서 발급받은 토큰을 입력:
   ```
   HF_TOKEN=hf_your_actual_token_here
   ```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 실행

```bash
python app.py
```

브라우저에서 http://localhost:5000 으로 접속하세요!

## 💡 주요 기능

- ✅ 실시간 채팅 인터페이스
- ✅ 대화 히스토리 유지 (세션별)
- ✅ 대화 내역 초기화
- ✅ 반응형 디자인
- ✅ 타이핑 로딩 애니메이션
- ✅ Enter 키로 전송

## 🔧 커스터마이징

### AI 응답 설정 변경

`app.py`의 `chat()` 함수에서 다음 파라미터를 조정할 수 있습니다:

```python
completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Instruct:fireworks-ai",
    messages=conversations[session_id],
    temperature=0.7,  # 창의성 조절 (0.0 ~ 2.0)
    max_tokens=2000   # 최대 응답 길이
)
```

### 디자인 변경

`templates/index.html`의 `<style>` 섹션에서 색상과 레이아웃을 수정할 수 있습니다.

## 📝 참고사항

- 무료 티어에는 사용량 제한이 있을 수 있습니다
- API 응답 시간은 네트워크 상황에 따라 달라질 수 있습니다
- 프로덕션 환경에서는 세션 관리를 Redis 등으로 변경하는 것을 권장합니다

## 🛠️ 기술 스택

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: KorGPT (moonshotai/Kimi-K2-Instruct via Hugging Face)
- **API**: OpenAI SDK (compatible)
- **Deployment**: Vercel
- **Version Control**: Git/GitHub

## 🌟 특징

- **완전 무료**: 누구나 제한 없이 무료로 사용 가능
- **오픈소스**: IndieCode가 오픈소스 기술을 활용하여 개발
- **최신 AI**: Hugging Face의 강력한 AI 모델 활용
- **빠른 응답**: 실시간 대화 처리
- **코드 하이라이팅**: 코드 블록 자동 포맷팅 및 복사 기능
- **반응형 디자인**: 모바일/태블릿/PC 모두 지원

## 📞 문의

- **광고 문의**: overy1234@naver.com
- **후원**: [후원 페이지](/donate)
- **GitHub**: [overy1234/kimigpt](https://github.com/overy1234/kimigpt)

## 📄 라이선스

이 프로젝트는 오픈소스이며, 자유롭게 사용 및 수정 가능합니다.
