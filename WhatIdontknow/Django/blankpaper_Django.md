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

### Django Orm

#### 1 Orm(Objects relative mapping?)
파이썬 객체와 SQLquery문 사이의 통역사  
#### 2 Query
데이터베이스에 원하는 데이터를 요청하는 명령문, 데이터베이스는 SQLite 형식만 알아들을 수 있음
직접 query문을 일일히 작성해 데이터를 다루는 대신 Django의 Orm프레임워크를 거쳐 파이썬의
객체 지향 프로그래밍으로 추상적 관점에서 데이터베이스를 두루 다룰 수 있음
#### 3 메서드
class를 만들어 자료를 추가? 3가지 방법 1. 클래스 생성 2. save()로 자료 추가 3. create()메서드로 생성과 등록 동시에  
filter(조건?), get(단일), all(모두), delete(삭제?), startswith? title() 등 메서드를 활용해 데이터를 직관적으로 
생성, 조회하거나 수정 및 삭제가 가능   
#### 4 CRUD
데이터 다룰 때 주요한 기능 Create/ Read/ Update/ Delete
각각 생성, 조회, 수정, 삭제 queryset을 가져오거나 그 중에서 조건을 걸어 특정 자료를 가져옴 
#### 5 Orm을 쓰는 이유?
데이터베이스를 다룰 때 간편하게 자동화되기 때문??

### Django Orm with view

#### 1 QuerysetAPI
요청을 데이터베이스에 반영?
#### 2 get
조회 메서드. 서버에 데이터를 전달? 반대? url에 넣어 보낼 수 있는 데이터 용량은 제한적
캐싱 가능 (서버 자체를 바꾸는 게 아닌 보여주는 기능) 
#### 3 post
서버 자체의 수정과 변경 기능을 가진 메서드. 사용 순간 표시나 조회가 아닌 데이터 자체에 변경사항이 생기기에
캐싱은 불가능 
#### 4 CSRF(cross-site-R?-F?)
클라이언트의 인지 밖에서 기기로 일종의 위조 요청을 보내는 방식의 공격. 인증 시스템을 요함. 
현재 위조 요청을 식별할 수 있도록 토큰을 끼워넣는 식으로 방지한다
#### 5 response 대기?
불필요하게 get메서드를 