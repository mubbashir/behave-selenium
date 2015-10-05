# behave-selenium
Selenium's example using behave

A quick example of python, behave, selenium, webdriver and docker to run prallel tests

* Install docker and create a selenium grid with say 2 nodes 
  * docker run -d -p 4444:4444 --name selenium-hub selenium/hub:2.47.1 ## To Run the Hub
  * docker run -d -P --link selenium-hub:hub selenium/node-firefox-debug:2.47.1 ## Run it twice to create 2 nodes, Docker will pick a random name 
  * Check the running docker containers
```
$ docker ps
CONTAINER ID        IMAGE                                COMMAND                  CREATED             STATUS              PORTS                     NAMES
34911106818f        selenium/node-firefox-debug:2.47.1   "/opt/bin/entry_point"   2 hours ago         Up 2 hours          0.0.0.0:32769->5900/tcp   condescending_elion
14971ef95408        selenium/node-firefox-debug:2.47.1   "/opt/bin/entry_point"   2 hours ago         Up 2 hours          0.0.0.0:32768->5900/tcp   trusting_mahavira
10688bf744d4        selenium/hub:2.47.1                  "/opt/bin/entry_point"   3 hours ago         Up 3 hours          0.0.0.0:4444->4444/tcp    selenium-hub
```

* Selenium gird  console to have two nodes  http://192.168.99.100:4444/grid/console # if you are on mac or on windows get the ip of the running docker vm e.g. ```docker-machine ip default```
* Clone the repo 
* Create virtulenv ```$virtualenv env```
* Activate the virtualenv and run the requirements file via pip ```source env/bin/activate; pip install -r requirements.txt``` 
* Export GRID_HUB_URL  ```export GRID_HUB_URL='http://192.168.99.100:4444/wd/hub'```
* Run ```behave --processes 2  --parallel-element feature``` 
