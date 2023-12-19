![wizardbook](https://github.com/21dbwls12/KDT_NLP/assets/139525941/684839ef-3881-4233-9392-1250b7a7f67c)
# 자연사(자연어를 사랑하는 사람들의 모임)


Intel 인공지능 인재양성과정 서울 1기 NLP 팀프로젝트


## 🖥️ 프로젝트 소개
chatGPT를 이용하여 시각장애인과 청각장애인을 위한 게임의 접근성을 높인 게임 플렛폼 구축
<br>

## 🕰️ 개발 기간
* 20231207 ~ 20231220

### 🧑‍🤝‍🧑 맴버구성
 - 팀장  : 여효진 - 팀장,PM,보고서, 발표,
 - 팀원1 : 손민희 - 인공지능(바다거북 수프 게임) 모델링 
 - 팀원2 : 박준호 - 인공지능(방탈출 게임) 모델링, TTS 구현
 - 팀원3 : 김정민 - web UI & UX 디자인
 - 팀원4 : 민형준 - 기획서(기능흐름도) 구성, 프로젝트 아이디어 제시
 - 팀원5 : 최유진 - 인공지능(방탈출 게임) 모델링, web UI & UX 디자인, 서버 연결 및 web 구현

### ⚙️ 개발 환경
- <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
- <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
- <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
- <img src="https://img.shields.io/badge/javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=white"/>
- <img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white"/>
- **Server** : <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/>

## 📌 주요 기능
#### 
- 게임 모델응 이용하여 채팅으로 실시간 게임 진행
#### 
- 방탈출 게임 모델은 모든 시나리오를 직접 실시간 생성

![cutecat](https://github.com/21dbwls12/KDT_NLP/assets/139525941/764cb09a-5c09-4399-af19-0128d7e78edc) ![rabbitwhite](https://github.com/21dbwls12/KDT_NLP/assets/139525941/c417478b-bde4-4b09-8958-4a2bc72e5214)



### 사용한 파일과 사이트 순서

project-base.html, footer.html, project-style.css
      
home.html in mysite

-> gamestart.html in Game

-> turtlesoupgame.html in Game / escapegame.html in Game

----------------------------------------------------------------------------------------------------------------
mysite.urls.py ->

            home
            path('admin/', admin.site.urls),
            # game/을 주소에 붙이면 game.urls참조
            path("game/", include("Game.urls")),
            # path('getImage/', views.getImagepage, name='getImage'),
            # path('create_thread', views.create_thread, name='create_thread'),
            re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
            # 초기화면
            path("", home)

Game.urls.py ->

            path("", views.gamestart, name="gamestart"),
            path('create_thread', views.create_thread, name='create_thread'),
            path("turtlesoupgame", views.turtlesoupgame, name="turtlesoupgame"),

Game.views.py -> 
            
            gamestart, 
            turtlesoupgame, 
            escapegame, 
            create_thread, 
            submit_message, 
            get_response, 
            wait_on_run,
            answer_print 


# 🫡 감사합니다. 
![zipolighter](https://github.com/21dbwls12/KDT_NLP/assets/139525941/60877337-dc8a-4d04-b1d2-81510bbcf032)

