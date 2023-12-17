# KDT_NLP
팀-자연사(자연어를 사랑하는 사람들의 모임)


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

