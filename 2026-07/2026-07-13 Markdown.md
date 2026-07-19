# 2026-07-13 
## Markdown & Git remote
일반 텍스트로 문서를 작성하는 간단한 방법
주로 개발자들이 텍스트와 코드를 작성해 문서화하기 위해 사용
개발자의 경우 텍스트와 코드 구분 필요

markdown 특징 
작성된 Markdown 문서는 다른 프로그램에 의해 변환되어 출력됨
마크업 언어
태그 등을 사용하여 문서나 데이터의 논리적인 구조와 의미를 정의하고, 컴퓨터가 이를 어떻게 해석하고 보여줘야 할지
지시하는 언어

왜 markdown인가?
단순히 "글씨를 꾸미는 도구" 가 아닌, "텍스트로 작성된 콘텐츠가 구조로 변환되는 경량 마크업 언어"
개발자가 가장 많이 쓰는 플랫폼( GitHub, GitLab, Discord, Notion 등)이 모두 마크다운을 표준으로 지원

환경 설정

마크다운 미리보기 켜는 법

Markdown 문법
구조 문법
제목 (Heading)
문서의 단계별 제목으로 사용
#개수로 h1부터 h6까지 표현  (뒷숫자 커질수록 제목 작아짐)
본문은 ##으로 시작하는 게 관례

목록(List)
순서 없는 목록
리스트 하위에 리스트를 넣으려면 들여쓰기 (탭) 필요

텍스트 강조(Bold/Italic/Cancel)
굵게(**) 기울임(*) 취소선(~~)

수평선
문법: ---(하이픈 3개 이상)
단락을 구분한 때 사용하는 수평선

인용문 (Blockquote)
문법: >

링크(link) & 이미지(image)
링크: [표시할 텍스트](URL)
이미지: ![대체 텍스트](이미지주소)

이미지의 너비와 높이는 마크다운으로 조절할 수 없습니다. (HTML 필요)

개발자 문법 (핵심)

인라인 코드(Inline Code)
문법:백틱(`)하나로 감싸기
문장 중간에 변수명, 파일명, 짧은 명령어를 언급할 때 "일반 텍스트와 구분하기 위해" 사용

코드 블록(Code blocks)
문법:백틱3개(```)로 감싸기
일반 텍스트와 달리 해당 프로그래밍 언어에 맞춰서 텍스트 스타일을 변환 
백틱3개 뒤에 언어 이름(python) 등을 적으면 하이라이트 처리
개발에서 마크다운을 사용하는 가장 큰 이유  

Markdown Guide
이 외 기타 문법은 가이드 문서를 활용하기
https://www.markdownguide.org/basic-syntax/ 

더 쓰고 싶다? 
마크다운 에디터
유료버전 Typora 
무료버전 MarkText 최신버전 기기맞게 다운


README.md
나의 프로젝트나 코드를 다른 사람에게 소개하는 '대문'이자 친절한 '사용 설명서'
게임: 새로 산 게임의 가이드북
제품: 전자제품 박스를 열면 가장 먼저 보이는 매뉴얼
개발: 내 코드를 처음 보는 사람(혹은 미래의 나)에게 "이건 어떤 프로그램이고, 어떻게 써야 해" 라고 알려주는

README.md를 작성하는 이유
아무리 좋은 코드를 짰어도, 어떻게 실행하는지 모르면 무용지물
개발자들 사이의 가장 기초적인 예의이자 소통 수단

미리 보는 개발자의 세상
곧 배우게 될 '개발자들의 저장소(Github)에 코드를 올리면 이 README 파일 이 자동으로 메인 화면에 나타남

마크다운의 모든 문법을 외울 필요는 전혀 없습니다. 
오늘 배운 핵심 문법 5-6가지만 알아도 됨
마크다운 정리
마크다운은 '예쁘게 꾸미기'보다 '정보를 구조적으로 잘 전달'하기 위한 도구

GIt Remote Repository
-원격 저장소
-remote
-push
-pull & clone
-gitignore
-실습

Remote Repository
 올림    마지막 영역 (commit)

원격 저장소
코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간
다양한 원격 저장소 서비스
GitLab  GitHub          Bitbucket              
           거의 다 가짐

remote
로컬& 원격 저장소
1. GitHub 가입
2.
명령어      /     /          /추가하는 원격 저장소의 주소       
git remote add origin remote_repo_url
                     /이름(추가하는 원격 저장소 별칭)       


README 만들어달라고 했을 시 기본적으로 commit이 하나 생긴 상태로 시작(충돌주의!)

로컬 저장소에 원격 저장소 주소 등록

push 
로컬에 쌓인 커밋을 위로 밀어올림 

GitHub Repository
^                     l
 l  push             v   pull or clone<-복제(전체)

Local Repository

git push origin master
원격 저장소에 commit 목록을 업로드
"git아 push 해줘 origin이라는 이름의 원격 저장소에 master라는 이름의 브랜치를"라는 의미의 명령어
(변경사항 만큼 업로드)

드라이브- 보이는 모든 것을 취합 <> remote- commit만 올리는 것
기기 변경 시 자격 증명 관리자 검색- windows 자격에서 찾아서 제거

원격 저장소에는 commit이 올라가는 것
commit 이력이 없다면 push 할 수 없다.

pull & clone

git pull origin master

원격 저장소의 변경사항만을 받아옴(업데이트)

git clone remote_repo_url  
원격 저장소 전체를 복제(다운로드)
clone 받은 프로젝트는 이미 git init이 되어 있습니다. 

싸피컴<> github<> 집컴    ->  주고받는 연습을 해야 됨

git 기타 명령어

git remote -v 
현재 로컬 저장소에 등록된 원격 저장소 목록 보기

git remote rm <remote_name>
현재 로컬 저장소에 등록된 원격 저장소 삭제

git push -set-upstream origin master (git push -u origin master)
master브랜치의 원본 브랜치를 origin의 master를 원본으로 기록
이후 git pull 등의 다른 명령어에서 특별한 인자가 없을 경우 master를 가져옴

깃헙
commit 1
                  clone받고 시작
로컬

과거가 동일해야 push가 가능

gitignore
DB민감정보->저장소에 올리면 x git이 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용 
(공유하면 안 되는 것들)

gitignore 주의사항
이미 git 의 관리를 받은 이력이 있는 파일이나 디렉토리는 나중에 gitignore에 명령해도 지워지지 않음

TIL (Today I Learned)
-단순히 배운 것 필기 (별 의미 x)
-배운 것 기반해서 + a
-막힌 부분이 있었는데 어떻게 해결했다. (과정)
<문서화 능력> 

무엇을 구하나?
어떤 정보가 주어졌는가?
어떤 공식이 떠오르는가? 

