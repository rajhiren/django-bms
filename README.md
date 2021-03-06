# Django Basketball Managment System


## Description of Project
You were hired by a basketball league to develop a management system to monitor games statistics and rankings of a recent tournament.
A total of 16 teams played in the first qualifying round, 8 moved to the next round, and so forth until one team was crowned as champion.
* Each team consists of a coach and 10 players. not all players participate in every game.
* There are 3 types of users in the system - the league admin, a coach, and a player.
* All 3 types of users can login to the site and logout.   Upon login they will view the scoreboard, which will display all games and final scores,  and will reflect how the competition progressed and who won.
* A coach may select his team in order to view a list of the players on it, and the average score of the team. when one of the players in the list is selected,his personal details will be presented, including - player’s name, height, average score, and the number of games he participated in. 
* A coach can filter players to see only the ones whose average score is in the 90 percentile across the team.
* The league admin may view all teams details - their average scores, their list of players, and players details. 
* The admin can also view the statistics of the site’s usage - number of times each user logged into the system,the total amount of time each user spent on the site, and who is currently online. (i.e. logged into the site)


## Notes:

* The project should be developed using Django on the server side and Angular/Django Template on the Front-end.
* We expect you to create the supporting models, business logic and views. 
* Please create a management command to generate fake users of all types with all the needed relations, 
and activities OR create a fixture to generate fake data.



## Prerequisites:
* Docker & docker-compose
* git


## SetUp

```
  docker-compose up --build
  docker-compose exec web python manage.py init_bms_data

```

## Urls 

```
Note : Default password for everything is `mydemo`

    Admin : 
        Url  :  http://0.0.0.0:8000/admin/
        User :  mydemo
        pswd :  mydemo

    BMS : 
        Url  :  http://0.0.0.0:8000/login/
        User :  mydemo
        pswd :  mydemo

    PGAdmin : 
        Url  :  http://localhost:8080/browser/
        User :  mydemo
        pswd :  mydemo

Login in PGAdmin and create super admin account. ( Forgive me for not automating this)
```

## Assumptions
* all player height will be in `Centimeters`
* all username will be `Email`


## screenshots

![alt text](https://github.com/rajhiren/django-bms/blob/master/screenshots/Screen%20Shot%202020-02-03%20at%2000.39.13.png)
![alt_text](https://github.com/rajhiren/django-bms/blob/master/screenshots/Screen%20Shot%202020-02-03%20at%2000.39.33.png)
![alt_text](https://github.com/rajhiren/django-bms/blob/master/screenshots/Screen%20Shot%202020-02-03%20at%2000.41.28.png)
![alt_text](https://github.com/rajhiren/django-bms/blob/master/screenshots/Screen%20Shot%202020-02-03%20at%2000.41.42.png)
![alt_text](https://github.com/rajhiren/django-bms/blob/master/screenshots/Screen%20Shot%202020-02-03%20at%2000.43.45.png)
![alt_text](https://github.com/rajhiren/django-bms/blob/master/screenshots/Screen%20Shot%202020-02-03%20at%2000.43.54.png)
![alt_text](https://github.com/rajhiren/django-bms/blob/master/screenshots/Screen%20Shot%202020-02-03%20at%2000.50.21.png)
![alt_text](https://github.com/rajhiren/django-bms/blob/master/screenshots/Screen%20Shot%202020-02-03%20at%2000.50.39.png)
![alt_text](https://github.com/rajhiren/django-bms/blob/master/screenshots/Screen%20Shot%202020-02-03%20at%2000.51.14.png)
