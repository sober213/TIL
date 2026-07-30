# 2026-07-30

## 오늘 공부한 내용

### 웹
HyperText
-웹 페이지를 다른 페이지로 연결하는 링크
Markup Languaage
-태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
인간이 읽고 쓰기 쉬운 형태이며, 데이터의 구조와 의미를 정의하는 데 집중
ex- HTML, Markdown
### Structure of HTML
<!DOCTYPE html>
-해당 문서가 html로 문서라는 것을 나타냄
<html></html>
-전체 페이지의 콘텐츠를 포함
메타데이터
-데이터를 설명하는 데이터
<head></head>
HTML문서에 관련된 설명, 설정 등 컴퓨터가 식별하는 메타데이터를 작성, 사용자에게 보이지 않음
<titile></title>
브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
<body></body>
HTML문서의 내용을 나타냄
페이지에 표시되는 모든 콘텐츠를 작성
한 문서에 하나의 body 요소만 존재
HTML Elenment(요소)
하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
닫는 태그는 태그 이름 앞에 슬래시가 포함됨
닫는 태그가 없는 태그도 존재

### CSS
웹 페이지의 디자인과 레이아웃을 구성하는 언어

#### CSS 적용 방법
1. 인라인(Inline) 스타일
2. 내부(Internal) 스타일 시트
3. 외부(External) 스타일 시트

스타일 적용 우선순위는 인라인>내부>외부 순으로 적용
인라인 스타일은 재사용이 어렵고 유지보수를 방해하니, 테스트나 특수한 경우에만 사용하는 것을 추천

**선택자(Selector)**
잘 선택해야 된다 
'누구를' 꾸밀지 지정하는 부분

선언(Declaration)
'어떻게' 꾸밀지에 대한 구체적인 한 줄의 명령
속성과 값이 한 쌍으로 이루어지며, 세미콜론(;)으로 끝남

속성(Property)
바꾸고 싶은 스타일의 종류를 나타냄

선택자 중 클래스 선택자('.'(dot))
주어진 클래스 속성을 가진 모든 요소를 선택 - 선택자 중 가장 많이 사용

### 명시도(specificity)
결과적으로 요소에 적용할 CSS선언을 결정하기 위한 알고리즘 

Cascading Style Sheet 
웹 페이지의 디자인과 레이아웃을 구성하는 언어

명시도가 높은 순 
1. Importance
 !important
2. Inline 스타일
3. 선택자
   id선택자> class선택자> 요소 선택자

4. 소스 코드 선언 순서
  
  !important
  다른 우선순위 규칙보다 우선하여 적용
  -사용 권장x

### 선언: 값과 단위
절대 단위
- px, pt, cm 등 다른 요소의 영향을 받지 않는 고정된 크기
상대 단위
- % em, rem, vw, vh 등 다른 요소(부모, 화면 표시 영역 등)의 크기에 다라 상대적으로 결정
상대 단위의 해결사: "rem"
"Root em"
em의 단점을 극복하기 위해 등장
부모 요소가 아닌, 최상위 요소(root element)인 <html>의 font-size를 기준으로 크기가 결정
부모를 따를 것인가(em), 뿌리를 지킬 것인가(rem)?
왜 rem이 필요한가?
상속의 복잡성 해결
em은 요소가 중첩될수록(부모의 부모...)최종 크기 계산이 기하급수적으로 복잡해짐
유지보수 용이성
rem은 오직 html 태그 하나만 바라보므로, 전체적인 비율 수정이 쉽고 레이아웃이 깨질
위험이 적음
접근성 향상
사용자가 브라우저에서 설정한 기본 폰트 크기를 html이 상속받으므로, 사용자의 설정에 맞춰 사이트 전체가 유연하게 확대/축소 됨.
CSS Box Model 
웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델

### 상속
CSS 상속
기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임
*상속 되는 속성*
Text 관련 요소(font, color, text-align), opacity, visibility 등
*상속 되지 않는 속성*
Box model 관련 요소(width, height, border, box-sizing...)
position 관련 요소(position, top/right/bottom/left, z-index) 등

### HTML스타일 가이드
#### 대소문자 구분
소문자 사용을 강력히 권장
태그명과 속성명 모두 소문자로 작성
#### 속성 따옴표
속성 값에는 큰 따옴표("")를 사용하는 것이 일반적
#### 코드 구조와 포맷팅
일관된 들여쓰기를 사용(보통 2칸 공백)
#### 각 요소는 한 줄에 하나씩 작성
중첩된 요소는 한 단계 더 들여쓰기
#### 공백 처리
HTML은 연속된 공백을 하나로 처리
Enter키로 줄 바꿈을 해도 브라우저에서 인식하지 않음(줄 바꿈 태그를 사용해야 함)
#### 에러 출력 없음 
HTML은 문법 오류가 있어도 별도의 에러 메시지를 출력하지 않음

### CSS스타일 가이드
코드 구조와 포맷팅
일관된 들여쓰기를 사용(보통 2칸 공백)
선택자와 속성은 각각 새 줄에 작성
중괄호 앞에 공백 넣기
마지막 속성 뒤에는 세미콜론(;)넣기
선택자 사용
class선택자를 우선적으로 사용
id, 요소 선택자 등은 가능한 피할 것
여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유지보수가 어려워지기 때문
속성과 값
속성과 값은 소문자로 작성
0 값에는 단위를 붙이지 않음
명명 규칙
클래스 이름은 의미 있고 목적을 나타내는 이름을 사용
케밥 케이스(kebab-case)를 사용
약어보다는 전체 단어를 사용
CSS적용 스타일
인라인(inline)스타일은 되도록 사용하지 말 것
CSS와 HTML 구조 정보가 혼합되어 작성되지기 때문에 코드를 이해하기 어렵게 만듦
CSS의 모든 속성은 외우는 것이 아님
자주 사용되는 속성은 그리 많이 않으며 주로 활용 하는 속성 위주로 사용하다 보면 자연스럽게 익히게 됨 그 외 속성을은 개발하며 필요할 때마다 검색해서 학습 후 사용할 것
### MDN Web Docs 
Mozilla Developer Network에서 제공하는 온라인 문서로, 웹 개발자와 디자이너를 위한 종합적인 참고 자료 
HTML, CSS, JavaScript, 웹API, 개발 도구 등 웹 기술에 대한 정보를 제공
MDN문서를 활요해야 하는 이유
정확성 및 신뢰성
최신 웹 기술
명확한 설명과 예제
### CSS Layout
3. Position: absolute
4. fixed
5. z-
   
### CSS flexbox
박스 표시(Display)타입
1. Outer display타입
2. Inner display 타입
CSS Flexbox 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
Flexbox(flex)타입은 책장의 책들을 정리하는 것과 같습니다.
요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
'공간 배열' & '정렬' 
### Flexbox 구성 요소
-main axis(주 축)
flex item들이 배치되는 기본 축
main start에서 시작하여 main end 방향으로 배치 (기본 값)
-cross axis(교차 축)
main axis에 수직인 축
corss start에서 시작하여 crossend 방향으로 배치(기본 값)
-flex container
display: flex; 혹은 display: inline-flex;가 설정된 부모 요소
이 컨테이너의 1차 자식 요소들이 Flex Item이 됨
flexbox 속성 값들을 사용하여 자식 요소 FLex Item들을 배치하는 주체
-flex item
Flex Container 내부에 레이아웃 되는 항목
이후 배우는 내용을 이용해 자유로운 순서 변경 및 정렬 가능

### Flexbox 속성
Flex 

3. flex-wrap
flex item 목록이 flex container의 한 행에 들어가지 않을 경우, 다른 행에 배치할지 여부 설정
4. justinfy-content
   주 축을 따라 flex item들을 정렬하고 간격을 조정 
5. align-content
   컨테이너에 여러 줄의 flex item이 있을 때, 그 줄들 사이의 공간을 어떻게 분배할지 지정   
6. align-items
   컨테이너 안에 있는 flex item들의 교차 축 정렬 방법을 지정
7. align-self
   컨테이너 안에 있는 flex item들을 교차 축을 따라 개별적으로 정렬 

목적에 따른 속성 분류
배치(flex-direction, flex-wrap)
공간 분배(justifiy-content, align-content)
정렬(align-items, align-self)
속성 쉽게 이해하는 방법
justify - 주축
align - 교차 축

8. flex-grow
  남는 행 여백을 비율에 따라 각 flex item에 분배
  flex item이 컨테이너 내에서 확장하는 비율을 지정
  felx-basis
  flex item의 초기 크기 값을 지정
  flex-basis와 width 값을 동시에 적용한 경우 flex-basis가 우선

### flex-wrap 응용
반응형 레이아웃 작성
다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식
flex-wrap을 사용해 반응형 레이아웃 작성(flex-grow & flex-basis 활용)
반응형 레이아웃 작성
1. card 요소를 flex 컨테이너로 설정
2. 컨테이너의 공간이 부족할 경우, 여러 줄로 나뉘어 배치되도록 허용
3. 각 flex item의 기본 너비를 설정
4. 컨테이너에 여유 공간이 있을 때 공간을 차지하며 늘어날 수 있도록 함(두 flex item 모두 값이 1 이므로 절반씩 나누어 가짐)
### 마진 상쇄
두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합되는 현상

### 박스 타입 별 수평 정렬
Block 요소의 수평 중앙 정렬
-margin: auto사용
Inline 요소의 수평 중앙 정렬
-text-align 사용 

### Flexbox Shorthand 속성

## 새롭게 배운 점

-

## 실습 코드

```bash
```

## 문제와 해결 방법

-

## 참고 자료

-

## 내일 공부할 내용

-