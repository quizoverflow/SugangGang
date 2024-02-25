삘타서 만들어본 수강신청 이삭줍기 프로그램

사용 언어 : 파이썬
사용 모듈 : tkinter , datetime, pytautogui, keyboard 등등

아직은 이삭줍기밖에 못하지만, 수강신청의 완전 자동화를 위해 Post 기능도 추가해볼 예정

----
ver 0.5  
수정해야 할 것
1) 버그 : 클릭 지점이 home window 위에 설정될 경우, 2cycle 이상 진행이 안되는 문제 해결해야 함
2) 단일 책임 원칙 위배 : SugangGui 클래스가 홈화면만 생성할 수 있게끔 수정해야 함

구현 할 것
1) pyinstaller 사용해서 exe 실행 파일화
2) 수강신청 id, pw로 로그인 후 수강 과목 신청 post
3) 키 설정 변경

----

