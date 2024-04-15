![wizardbook](https://github.com/21dbwls12/KDT_NLP/assets/139525941/684839ef-3881-4233-9392-1250b7a7f67c)
# 자연사(자연어를 사랑하는 사람들의 모임)


Intel 인공지능 인재양성과정 서울 1기 NLP 팀프로젝트


## 🖥️ 프로젝트 소개
chatGPT를 이용하여 시각장애인과 청각장애인을 위한 게임의 접근성을 높인 게임 플렛폼 구축
<br>

## 🕰️ 개발 기간
* 20231207 ~ 20231220

### 🧑‍🤝‍🧑 맴버구성
 - 팀장  : [여효진](https://github.com/penguinetongtong) - 팀장,PM,보고서, 발표,
 - 팀원1 : [손민희](https://github.com/minibe0) - 인공지능(바다거북 수프 게임) 모델링 
 - 팀원2 : [박준호](https://github.com/junnamu) - 인공지능(방탈출 게임) 모델링, TTS 구현
 - 팀원3 : [김정민](https://github.com/Mingming222345) - web UI & UX 디자인
 - 팀원4 : [민형준](https://github.com/xax219) - 기획서(기능흐름도) 구성, 프로젝트 아이디어 제시
 - 팀원5 : [최유진](https://github.com/21dbwls12) - 인공지능(방탈출 게임) 모델링, web UI & UX 디자인, 서버 연결 및 web 구현

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



### 📁 사용한 파일과 사이트 순서

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

### 🪄 프롬포트 작성 방법(안드로이드 스튜디오 이용해서 수정)
App수준 Gradle
```kotlin
dependencies{
    // 맨 아래에 추가
    // openai용 그래들 + manifest에 인터넷 코드 추가
    // import Kotlin API client BOM
    implementation(platform("com.aallam.openai:openai-client-bom:3.6.1"))
    implementation ("com.aallam.openai:openai-client")
    runtimeOnly ("io.ktor:ktor-client-okhttp")
}
```
AndrodiManifest.xml
```kotlin
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

// 인터넷 코드 추가 부분
<uses-permission android:name="android.permission.INTERNET" />

    <application
    ...
```
MainActivity.kt
```kotlin
@OptIn(BetaOpenAI::class)
@Composable
fun instructions(){
    // project 수준의  gradle.properties에 OPEN_AI_TOKEN, ASSISTANT_KEY를 추가
    // OPEN_AI_TOKEN=""
    // ASSISTANT_KEY=""""
    // app수준의 그래들에 아래 코드 추가
// 이거 결국 안되서 주석처리하고 실행해서 성공함!!
// 위치는 buildTypes{} 위
//    android {
//        defaultConfig {
//            buildFeatures {
//                buildConfig = true
//                compose = true
//            }
//            buildConfigField("String", "OPENAI_API_TOKEN", "\"${project.property("OPEN_AI_TOKEN")}\"")
//            buildConfigField("String", "ASSISTANT_KEY", "\"${project.property("ASSISTANT_KEY")}\"")
//        }
//    }
    // 안되면 clean build하고  rebuild하기
//    val token = BuildConfig.OPENAI_API_TOKEN
//    val assistantKey = BuildConfig.ASSISTANT_KEY
    val token = "YOUR_OPENAI_API_TOKEN"
    val assistantKey = "YOUR_ASSISTANT_KEY"
    val openAI by lazy { OpenAI(token) }
    var asid by remember { mutableStateOf<AssistantId?>(null) }
    var ints by remember { mutableStateOf("") }
    LaunchedEffect(Unit) {
        val assistantResponse = openAI.assistant(
            id = AssistantId(assistantKey), request = AssistantRequest(
                instructions = "방탈출 게임 진행자 겸 도우미가 되어서 방탈출 게임을 진행해줘. 너의 이름은 동수야.\n" +
                        "사용자가 시작을 입력하면 너를 사용자에게 소개하고 사용자에게 게임의 테마를 물어봐. 테마는 사용자가 직접 입력하고 사용자가 원하면 네가 직접 추천해줘. 테마는 여러개 받아도 돼. 그리고 난이도를 물어봐. 난이도는 1부터 5까지고 5가 가장 어려운 난이도고 1이 가장 쉬운 난이도야.\n" +
                        "먼저 사용자가 입력한 테마와 난이도에 해당하는 방탈출 게임을 만들어. 방은 하나여도 되고 연속적으로 이어진 방이 여러개 혹은 큰 장소(병원, 학교, 공원 등) 그 자체여도 괜찮아. 게임의 시작은 네가 정한 한정된 장소에 사용자가 갇힐 거고 끝은 항상 사용자가 닫힌 문을 열 열쇠를 얻거나 비밀번호를 찾아서 입력하거나 특정행동을 한 상황이야. 완료 조건은 1가지 방법이상이어도 되는데 만약 2가지 이상일 경우 모든 방법을 필수적으로 이행해야 하는 것으로 해줘.\n" +
                        "그리고 게임을 시작해. 시작하고 나서는 사용자에게 만든 게임에서 벗어나거나 정해진 시작과 끝은 바꾸지마. 왠만해서는 정한 것을 바꾸지 말고 흐름을 바꾸지마. 네가 처음 만든 게임이 사실이 될거고 이후 게임을 진행하면서 사용자에게 거짓말하지마. 처음으로 사용자에게 제시해주는 것은 네가 만든 방탈출 게임의 설정 상황, 장소, 사용자가 움직이게 될 주인공 캐릭터에 대한 설명 등 사용자가 방탈출 게임을 진행하면서 필수적으로 알아야 할 설정이나 흥미를 유발할 수 있는 부분의 내용이야. 방탈출 게임을 진행할 때는 지정된 선택지를 주어도 되고 사용자에게 자유도를 주어도 돼. 즉, 선택지를 너가 한정지어줘도 되고 일부 상황이나 장소만 제공한 후 그 제공된 텍스트만 보고 사용자가 행동을 직접 입력해주게 해도 돼. 공포나 스릴러테마에서는 중간에 죽거나 다치는 등의 상황을 제공해서 사용자가 해당 선택지를 선택하면 게임을 종료해도 돼. 종료시 적절하고 재치있는 이유와 함께 탈출 실패를 제공해줘. 대신 이런 상황을 넣는다면 10%의 아래의 확률로 제공해줘. 게임이 진행될 때는 중간중간에 퀴즈, 퍼즐등의 요소들도 추가해줘. 퀴즈나 퍼즐은 네가 정한 답과 다를 경우 다음으로 진행시키지말고 답이 틀렸음을 사용자에게 제시하고 다시 풀게해. 이때 힌트나 정답으로 유도하는 말은 절대 하지마. 그냥 틀렸다는 것만 명시하고 다른 행동이나 답을 입력해달라고만 해줘. 사용자가 힌트를 달라고 하지 않았을 경우에는 힌트가 도움말을 출력하지마.\n" +
                        "사용자가 힌트라고 입력하거나 힌트를 원하면 해당 문제에 대한 답이나 행동을 유도할 방법을 제시해줘. 원하는 만큼 사용할 수 있지만 3번을 초과해서 사용하게 되면 사용자가 게임 완료에 해당하는 방법을 적절하게 수행해도 마지막에 적절하고 재치있는 이유와 함께 탈출 실패를 제공해줘. 사용자가 게임을 중간에 그만하기를 원해도 적절하고 재치있는 이유와 함께 탈출 실패를 제공해줘.\n" +
                        "공포나 스릴러테마에서 혹시 빌런이나 사용자를 해치고 가두는 사람이 나온다면 그 사람의 이름은 홍진이야. 대사가 필요하다면 '집에 간다고?!', '코딩해야지!', '어디가??', '나랑 남자~'나 비슷한 대사로 출력해줘.\n" +
                        "사용자에게 반말로 친구와 게임하듯 대화하듯 해줘. 중간에 가끔씩 적절한 이모지도 같이 사용해줘. 너무 과하게 사용하지는 마. 길이는 최소 20분 이상의 게임으로 만들어줘. 만약 사용자가 짧은 걸 원한다고 입력하면 그때는 짧게 만들어주지만 그렇지 않을 경우에는 최소 20분으로 적당히 길게 만들어줘.\n"+
                        "사용자가 혹시 테마를 과거시대를 골랐다거나 타임슬립의 소재라면 그 시대의 그 공간의 말투를 사용해서 게임을 진행해줘. 만약 정보가 부족하다면 조선과 서양 말투 2개만 분리해서 해줘. 아예 그것도 부족하다면 그냥 일반 말투로 해줘.\n"+
                        "공주님이 나오는 방탈출 시나리오라면 그 공주님의 이름은 상은이야. 대사가 필요하다면 '어, 잠만? 그게 맞아?', '사실은 그.... 아니야..', '뾰로롱', '흥', '흥, 칫'이나 비슷하게 새침한 대사로 출력해줘."
            )
        )
        asid = assistantResponse.id
        ints = assistantResponse.instructions?: ""
    }
    Log.d("assistant instructions", "getChatCompletion: ${ints}, ${asid}")
}
```

## 📷 웹 구현 스크린샷

![스샷1](https://github.com/21dbwls12/KDT_NLP/assets/139525941/fc49ccb3-60ec-433b-a86f-2d566f924236) |![스샷2](https://github.com/21dbwls12/KDT_NLP/assets/139525941/d1d394c2-9ffc-40b4-9861-08c0a46e2407) |![스샷3](https://github.com/21dbwls12/KDT_NLP/assets/139525941/f8c312f5-d8b9-4a57-a78e-066da4438091)
--- | --- | --- |
![스샷4](https://github.com/21dbwls12/KDT_NLP/assets/139525941/ebee2ab4-fd32-4024-87d2-3593f72efca0) |![스샷5](https://github.com/21dbwls12/KDT_NLP/assets/139525941/c04e547e-8c56-4569-b02c-3b9e75d5fdb2) |![스샷6](https://github.com/21dbwls12/KDT_NLP/assets/139525941/2127e9b5-866b-404d-b4b2-cdcfd5f8e93c)
![스샷7](https://github.com/21dbwls12/KDT_NLP/assets/139525941/6787dd95-9fa3-4f20-992f-1c2b798722f8) |![스샷8](https://github.com/21dbwls12/KDT_NLP/assets/139525941/8faa204a-b87c-4974-9dbc-7daae8409ac1) |![스샷9](https://github.com/21dbwls12/KDT_NLP/assets/139525941/1127bccc-abf5-47b1-ae86-e8b157fc17b0)
![스샷10](https://github.com/21dbwls12/KDT_NLP/assets/139525941/a53b6aa6-190d-4063-8e7e-56375b10f110) |![스샷11](https://github.com/21dbwls12/KDT_NLP/assets/139525941/e882fa5f-5cd8-4a21-bae7-4235e80d9808) |![스샷12](https://github.com/21dbwls12/KDT_NLP/assets/139525941/0e3d0d84-7378-45ee-abe1-2efacabe2441)
![스샷13](https://github.com/21dbwls12/KDT_NLP/assets/139525941/0bd9600b-3344-4818-bc4d-dcc916d7286e) |![스샷14](https://github.com/21dbwls12/KDT_NLP/assets/139525941/7926d07e-0fc6-4dce-931c-cf0b1454d2af) |![스샷15](https://github.com/21dbwls12/KDT_NLP/assets/139525941/e9f4e157-4eb2-4d74-8575-8686c9c6f864)
![스샷16](https://github.com/21dbwls12/KDT_NLP/assets/139525941/619fa532-20c2-4f83-a9fc-f10b1eae3a10) |![스샷17](https://github.com/21dbwls12/KDT_NLP/assets/139525941/8cdf1845-459f-4ebe-8b95-bf01b97f9cc0)

### [시연 영상](https://www.youtube.com/watch?v=kjJ0cKcAH_c)의 용량이 커서 링크로 올립니다.
https://www.youtube.com/watch?v=kjJ0cKcAH_c

# 🫡 감사합니다. 
![zipolighter](https://github.com/21dbwls12/KDT_NLP/assets/139525941/60877337-dc8a-4d04-b1d2-81510bbcf032)

