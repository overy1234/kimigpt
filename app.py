import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

app = Flask(__name__)

# Vercel에서는 정적 파일을 직접 서빙하므로 이 설정 추가
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# KorGPT API 클라이언트 설정
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ.get("HF_TOKEN", "your-huggingface-token-here"),
    default_headers={"Content-Type": "application/json"}
)

# 대화 히스토리를 저장할 딕셔너리 (세션별로 관리)
conversations = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/donate')
def donate():
    return render_template('donate.html')


@app.route('/ad-inquiry')
def ad_inquiry():
    return render_template('ad-inquiry.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        # 세션별 대화 히스토리 초기화
        if session_id not in conversations:
            conversations[session_id] = []
        
        # 사용자 메시지 추가
        conversations[session_id].append({
            "role": "user",
            "content": user_message
        })
        
        # KorGPT API 호출
        completion = client.chat.completions.create(
            model="moonshotai/Kimi-K2-Instruct:fireworks-ai",
            messages=conversations[session_id],
            temperature=0.7,
            max_tokens=2000
        )
        
        # AI 응답 추출
        ai_message = completion.choices[0].message.content
        
        # AI 응답을 히스토리에 추가
        conversations[session_id].append({
            "role": "assistant",
            "content": ai_message
        })
        
        return jsonify({
            'success': True,
            'message': ai_message
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/clear', methods=['POST'])
def clear_history():
    try:
        data = request.json
        session_id = data.get('session_id', 'default')
        
        if session_id in conversations:
            conversations[session_id] = []
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# Vercel을 위한 handler (WSGI 애플리케이션)
app.wsgi_app = app.wsgi_app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
