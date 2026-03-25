## API & Web Crawling Practice (Day 5,6)

Open API 연동과 웹 크롤링 기법을 활용한 데이터 수집 실습 기록입니다.

### 1. API Integration

다양한 플랫폼에서 제공하는 Open API를 연동하여 정형 데이터를 수집하고 처리하는 과정을 실습했습니다.

- **Naver API**: 네이버 검색 결과 데이터를 호출하고 JSON 형식을 파싱하는 기본 인터페이스 연동 실습
- **KMDB API**: 한국영화데이터베이스(KMDB) API를 활용한 영화 상세 정보 추출 및 데이터 구조화
- **Public Data API**: 공공데이터포털의 데이터를 인증키 기반으로 호출하고 활용하는 테스트 수행

### 2. Web Crawling

API가 제공되지 않는 웹 페이지에서 필요한 정보를 직접 추출하는 크롤링 기술을 학습했습니다.

- **Static Crawling (BeautifulSoup)**
    - **네이버 증권**: 주식 시세 및 종목 정보 수집
    - **네이버 지식인**: 질문 및 답변 텍스트 데이터 추출
    - **핫트랙스**: 도서 및 상품 정보 리스트 수집
- **Dynamic Crawling (Selenium)**
    - **다음 카페**: 로그인 기반 혹은 자바스크립트 렌더링이 필요한 커뮤니티 게시글 크롤링
    - **동적 페이지 테스트**: 비동기 로딩(AJAX) 처리가 필요한 웹 사이트의 데이터 수집 로직 구현

### 3. Tech Stack

- **Language**: Python
- **Library**
    - `Requests`: HTTP 통신 및 API 호출
    - `BeautifulSoup4`: HTML 파싱 및 정적 크롤링
    - `Selenium`: 브라우저 자동화 및 동적 크롤링
    - `Pandas`: 수집 데이터의 표 형식 정리 및 저장

---

## Data Science & NLP Practice (Day 7,8)

데이터 회귀 분석을 통한 가격 및 매출 예측과 자연어 처리(NLP) 기법을 활용한 텍스트 마이닝 및 감정 분석 실습 프로젝트입니다.

### 1. Regression Analysis (회귀 분석)

다양한 데이터셋을 활용하여 연속형 변수를 예측하는 회귀 모델을 구현하고 성능을 평가했습니다.

- **주택 가격 예측**
    - **California Housing**: 사이킷런 기본 데이터셋을 활용하여 주거지 특징에 따른 집값 예측 모델 구축
    - **한국 아파트 가격**: 국내 아파트 단지별 특성 데이터를 전처리하고 가격 예측 수행
- **비즈니스 매출 예측**
    - **여의도 카페 매출**: 위치, 요일, 시간대 등 환경 변수에 따른 카페 매출 영향도 분석 및 예측
- **모델 저장 및 관리**
    - 학습된 모델을 `pickle` 또는 `joblib` 라이브러리를 통해 파일화하여 재사용하는 프로세스 실습

### 2. Natural Language Processing & Sentiment Analysis (자연어 처리 및 감정 분석)

텍스트 데이터의 전처리부터 의미 추출, 감성 분류까지의 과정을 실습했습니다.

- **NLTK 기반 형태소 분석**
    - **영어(English)**: NLTK 라이브러리를 활용한 토큰화(Tokenization), 품사 태깅(POS Tagging), 불용어 제거 실습
    - **한국어(Korean)**: KoNLPy 등 한국어 형태소 분석기를 연동한 한글 텍스트 처리 연습
- **텍스트 마이닝 기본**
    - 빈도수 분석, 워드 클라우드(Word Cloud) 생성 등 비정형 데이터의 특징 추출 실습
- **영화 리뷰 감정 분석**
    - 영화 리뷰 텍스트 데이터를 벡터화(TF-IDF 등)하여 긍정/부정을 분류하는 지도 학습 모델 구현

### 3. Tech Stack

- **Language**: Python
- **Data Analysis**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **NLP**: NLTK, KoNLPy
- **Visualization**: Matplotlib, Seaborn
