# 2026-07-10 

## GIT
(분산)버전 관리 시스템 

버전 관리: 변화를 기록하고 추적하는 것 ex) v0.1 -> v0.2 -> v0.5 (롤백하려면 어디서 어떻게?)

Google Docs 예시 

빈 페이지 -> 한 줄 

우리는 버전 관리를 알고있다.
ex) 최종 찐최종

졸업논문 진짜최종
졸업논문 변경사항
변경사항을 기록하는 파일 만들기

 마지막 파일과, 이전 변경사항만 남기기 


기존 (누적식)지붕+ 벽 + 창문 
개선 생성 전 지붕/ 벽/ 창문/ 문/ 집
                  ver1  ver2 ver3 ver4 최종

중앙 집중식-버전은 중앙 서버에 저장 / 분산식-버전을 여러 개의 복제된 저장소에 저장 및 관리

분산 구조에서의 장점
중앙 서버에 의존하지 않고도 동시에 다양한 작업을 수행할 수 있음

Git의 역할
코드의 버전(히스토리)을 관리
개발되어 온 과정 파악
이전 버전과의 변경 사항 비교

코드의 '변경 이력'을 기록하고 '협업'을 원활하게 하는 도구

Git의 영역

Working Directory->    Staging Area ->     Repository
눈으로 보고 있는             중간 영역         버전 영역     

CLI에서 해야됨;;

Staging Area (무대에 올림)
Working Directory에서 변경된 파일 중
다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

a.txt    셋 중 둘만 올려야 될 때 ver0.1
b.py
c.txt 

Repository 
버전들이 쌓여있는 영역 
버전(commit) 이력과 파일들이 영구적으로 저장되는 영역 모든 버전(commit)과 변경 이력이 기록됨

Commit "버전" 
변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다 하여 'snapshot'이라고도 함

Git의 동작 

`git init`                                              
로컬 저장소 설정(초기화)
git의 버전 관리를 시작할 디렉토리에서 진행

`git add`
변경사항이 있는 파일을 staging area에 추가

`git commit`
staging area에 있는 파일들을 저장소에 기록
해당 시점의 버전을 생성하고 변경 이력을 남기는 것

변화 1 - 아무것도 없던 상태에서 sample.txt 파일이 생성됨

`git status` 
git 상태 확인 

`git log` 
commit history 보기

`git init` 
`git add sample.txt`
`git status`
`git commit -m "first commit"`
`git config --global user.email`
`git config --global user.name`

`git commit -m "first commit"`

`git log` #repository 확인
`git status`
`git commit -m "second commit"`
`git status `

`git add .` (현재 모든 디렉토리 추가)

참고 
  local(내 컴) -remote(인터넷과 연결된 온라인 저장소)

!!!!`git init` 주의사항!!!!
Git 로컬 저장소 내에 또다른 Git 로컬 저장소를 만들지 말 것
Git저장소 안에 Git저장소가 있을 경우 가장 바깥쪽의 Git 저장소가 안쪽의 git 저장소의 변경사항을 추적할 수 없기 대문
즉, 이미 Git로컬 저장소인 디렉토리 내부 하단에서 git init 명령어를 다시 입력하지 말 것

바탕화면에서 git init 실행 시 그 안 모든 기존 git init 무효화 
복구? 
숨김폴더 탐색기 옵션에서 숨김해제  .git폴더 찾아서 삭제 






 
