## Django 백지복습

### 웹 애플리케이션

#### 1 웹 서비스 구조
웹 서비스는 웹 브라우저나 앱 등 클라이언트의 요청을 서버나 데이터베이스가 받음
응답을 돌려주면 웹 브라우저에서 서버가 돌려준 응답에 따라 html등의 형태로 서비스
#### 2 웹 프레임워크
디자인 패턴은 개발 중 공통적으로 나오는 문제점에 대처하는 양식들 개발에 있어 유용히 활용되는
도구를 웹 프레임워크라 함. 파이썬의 대표적인 프레임워크로 Django가 있음
#### 3 가상환경
python -m venv venv 각방쓰는 느낌 가상환경 내에서만 글로벌 환경과 다른 패키지 등
다른 설정에서 작업할 수 있는 방식 freeze로 현재 가상환경 > requirements.txt로 저장 가능
역으로 requirements에서 읽어와 다른 작업자들과 동일한 환경 내 충돌없는 작업
#### 4 프로젝트
프로젝트와 앱의 관계서 프로젝트는 카페, 앱은 글작성 공지 등 한 서비스 내 특정 기능을 담당하는 구조
애플리케이션은 여러 개 가능
#### 5 MTV, MCV구조
Models, Templates, Views/ Models, Controllers, Views? 데이터의 흐름에 따라 코드 작성
둘이 거의 비슷한 뜻이나 Django가 자기 기준대로 명명? 모델은 데이터를 저장하거나 서비스의 골자 부분, 
Views(=Controllers)은 전체적 동작 담당, Templates(=Views)는 요청 + 템플릿 = 응답을 돌려주는 느낌 

### Django 템플릿 언어

#### 1 DTL
파이썬과 앱?을 분리해 따로 다룰 수 있게 하는 언어 형식? html
form 은 편리하게 클라이언트의 입력값 요청을 받아 대응
서버가 url로 요청을 받아 해당 url과 연결된 앱을 호출, html render 등과 조합해 대응되는 페이지 반환
#### 2 base template
언제든지 재정의할 수 있는 양식을 정의하는 방식? base template으로 여러 번 사용할 템플릿 형태 작성
template 상속 특정 양식을 여러 html에 적용할 수 있게 자손이 extends로 전달받음 
block, endblock으로 재정의할 수 있는 부분 구분, href로 해당 base 사용한다 강조?  
#### 3 tag 
%% {{}}등으로 html 상 변수를 파이썬 비스무리하게 조건, 반복, 제어를 가능케 하는 기능
형태는 파이썬 문법과 같으나 실제로는 표기만 그렇고 논리 구조 명시 목적이 강함
급양 메뉴판 구현? if, elif, for 등 %{tag}%
#### 4 throw & catch
.get 메서드 사용? messages input 입력값이 딕셔너리 형태로 모인 곳에서 키 대응값을 가져온다
url variable -> 변수/ url filter -> 변수 수정, num, str등 5가지 형태 
url ??? -> 키워드   
#### 5 Urls
프로젝트상 url이 하나만 있을 때 대응하기 어려운 때가 있다 
앱마다 url을 따로 만들어서 include로 연결?
Url, render, views 호출 

### Django Model

#### 1 class Model.models
클래스로 모델과 데이터베이스를 연결해 생 코딩 대신 자동적으로 python 상 데이터 정리와 적용을
가능하게끔 하는 Django 프레임워크
#### 2 Field, ???
컬럼으로 데이터를 나타낸다? max_length, blank=False 등의 ??로 틀을 잡을 수 있음 
#### 3 migrate
models.py makemigrations? 모델이나 데이터에 변경사항이 있을 때 반영하기 위해 세팅, migrate로 실제 적용 
#### 4 crud
create read u?? delete
#### 5 SQLite