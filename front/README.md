# 금융 상품 추천 프로그램 구현


## 팀원 정보 및 업무 분담 내역
- 박수민 (팀장) : 환율 API 기반 계산, 카카오맵 API 기반 주변 은행 찾기, 게시판 및 댓글 CRUD
- 김지용 : 회원 커스터마이징, 금융감독원 API 기반 예적금 금리 비교, 마이 페이지 구성, 기타 코드 세부 디버깅



## 설계 내용 및 실제 구현 정도
- 기본 필수 기능만 구현, zero ui 추구..

### 메인 페이지
- nav bar를 넣은 홈화면 구성

### 회원 커스터마이징
- 회원가입
    - 매뉴얼 반영
    - 전용 serializer 및 저장과 관련된 adapter 사용

- 로그인
    - dj_rest_auth 활용
    - 반환된 토큰 값을 store에 저장
    - is_Login: 현재 상태(로그인 여부)를 나타낼 수 있는 값(token값 존재여부)을 store에 저장

- 로그아웃
    - store에 저장된 토큰 값 삭제

- 패이지 방문 권한
    - 로그인, 회원가입의 경우 로그인 상태에서는 방문하지 못하도록 함
    - 마이페이지의 경우 로그아웃 상태에서는 방문하지 못하고 로그인 화면을 리디렉트


### 예적금 금리 비교
- 데이터 저장
    - axios.get으로 API 응답을 받고, 미리 만들어 놓은 product serializer를 통해 직렬화 한 뒤 DB에 저장
    - 응답 내용 중 상품 유형( 예금의 경우 D, 적금의 경우 S)을 저장할 필드를 추가하여 데이터베이스에 예, 적금 모두를 한 곳에 저장

- 전체 조회

    - 목록 출력 화면에서 데이터베이스에 저장된 상품들을 각각의 상품 유형에 따라 필터링 하여 표시
    - 왼쪽에 은행을 선택할 경우(select-option 사용)(중복 선택 가능) - 페이지상에 받아온 데이터를 각각의 은행에 맞게 필터링하여 실시간 반영
    - 각 상품 클릭 시 각 상품의 상세 정보로 이동

- 상세 조회

    - 가입하기(장바구니 담기) 버튼 구현 - 프로필 페이지 가입 상품 목록에도 반영
    - 이전에 구현했던 좋아요 버튼과 유사한 방식 - 눌렀을 때 가입 상품 목록에 있으면 제거, 없으면 추가

### 환율 계산기
- 한국수출입은행의 환율정보 API 활용해 현재 환율 정보 불러오기
- 실시간 데이터 저장 → 꺼내오기
- 화폐1, 2를 선택할 수 있도록 구성
- 2가지 입력 받도록 구성 (v-model을 이용한 select 메서드 사용)
    - 원화 입력 시 → 선택한 국가의 통화로 변환된 값 출력
    - 타국 통화 입력 시 → 해당 통화를 원화로 변환한 값을 출력
- CORS 에러를 방지하기 위해 django에서 데이터를 가져와 vue로 전달할 수 있도록 구성

### 근처 은행 검색
- 내 주변 은행 찾기
    - 카카오맵 API 활용해 지도 생성 (ex. 카카오맵 API, T맵 API)
    - 은행(selectedSearch1)을 선택하고 위치(keyword)를 입력하면 해당 위치 정보 주변의 은행의 정보를 파악할 수 있도록 구성
    - 지도 상의 핀 선택 시, 해당 위치 근처의 은행 정보를 적절히 출력


### 커뮤니티 (익명 자유 게시판)
- 게시판의 게시글 생성, 수정, 삭제 기능 
- Authorization: `Token ${accountStore.token}`를 통해 회원의 권한에 따라 본인이 작성한 게시글이나 댓글만 조작 가능하도록 출력

### 마이페이지
- 기본 정보
    - 기본 정보 정상적으로 출력
    - 가입된 상품 리스트는 유저 정보에서 역참조로 상품 리스트를 받아와서 출력을 하였다.
    - 가입된 상품 리스트 각각을 클릭하면 각 상품 상세 정보로 이동
    - 로그인 한 상태가 아닐 시 진입하려 할 때 로그인 화면으로 리디렉트

- 회원 정보 수정
    - 회원 정보 수정 - 유저 네임을 포함한 모든 정보 수정 가능 - 비밀번호는 수정 불가
    - 회원 정보 수정 시 기존 비밀번호 값(필수값으로 지정)을 입력 후 전송해야 수정 가능

- 차트
    - chart.js를 활용하였다.
    - 가입된 예금, 적금 상품 정보 리스트 각각에 대해 저축 금리 현황을 바 차트로 나타냄

- 금융 상품 추천 알고리즘
    - 저장된 상품 중 가장 금리가 높은 순으로 정렬
    - 가입 안 된 것들 중 가장 금리가 높은 것부터 5개 추천하는 방식

## 데이터베이스 모델링 (ERD)
![erd drawio](https://lab.ssafy.com/breathin_suemin/final-pjt/front/scr/assets/139521789/f63f546f-aa58-47ea-8ee2-0a82e4ebe26c)

## 금융 상품 추천 알고리즘에 대한 기술적 설장
- 저장된 상품 중 가장 금리가 높은 순으로 정렬해서 가입 안 된 것들ㅈ ㅜㅇ 가장  

## 서비스 대표 기능들에 대한 설깅
- 금융 상품 코드가 겹치는 상품들이 있어서, 응답을 받아서 저장할 때 금융 상품 코드가 아닌 상품 이름을 기준으로 DB상 존재 여부를 판단하여 저장

## 느낀점
- 박수민 : 프론트와 백엔드를 넘나들기 위한 axios 요청이 처리하기 복잡했고, db에는 저장되지만, 화면 상으로는 출력이 안 되는 경우가 많았다. 데이터를 처리하는 과정 중 디버깅하는 과정이 길어 오류에 따른 문제 해결을 하는 방법을 배웠다. 계절학기 기간동안 개인적으로 이 프로젝트를 더 디벨롭시켜서 기능을 추가하거나 ui를 가독성 좋고, 깔끔하게 구현할 예정이다!

- 김지용 : 프론트 백엔드 각각을 다룰 때는 요청과 응답을 다루는 것이 그렇게 어렵지 않았는데, 두 개를 연동하여 응답과 요청을 다룰 때는 또 다른 차원의 어려움이 기다리고 있었다. 데이터를 보내는 방법(method)이나 정보(data)를 다루는 방법을 더 고민해보고 배울 수 있는 좋은 기회였다.
