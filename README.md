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
* Get port of VNC if you want to connect to a node  
```
docker port <container-name|container-id> 5900
docker port 34911106818f
#=> 0.0.0.0:49338
```
* Clone the repo
* Create virtulenv ```$virtualenv env```
* Activate the virtualenv and run the requirements file via pip ```source env/bin/activate; pip install -r requirements.txt```
* Export GRID_HUB_URL  ```export GRID_HUB_URL='http://192.168.99.100:4444/wd/hub'```
* Run ```behave --processes 2  --parallel-element feature```

#### Contributing

* Run the requiremetns file in the virtual environment  

* Run `pre-commit install` ## To install [pre-commit](http://pre-commit.com/#usage)

Run pre-commit install to install pre-commit into your git hooks. pre-commit will now run on every commit. Every time you clone this project  running ```pre-commit install``` should always be the first thing you do.

If you want to manually run all pre-commit hooks on a repository, ```run pre-commit run --all-files```. To run individual hooks use ```pre-commit run <hook_id>```.

The first time pre-commit runs on a file it will automatically download, install, and run the hook. Note that running a hook for the first time may be slow. For example: If the machine does not have node installed, pre-commit will download and build a copy of node.

* To Run all pre-commit manually on all file type `pre-commit run --all-files`
* To run specific hook (via the id in .pre-commit-config.yaml) on specific file(s) `pre-commit run flake8 --files bdd_feature_tests/features/steps/dubizzle_homepage_steps.py`
* To run autopep 8 manually (which will run automatically once pre-commit is configured) type `pre-commit run 'autopep8-wrapper' --files bdd_feature_tests/features/steps/dubizzle_homepage_steps.py`

#### Refrence
* https://github.com/hugeinc/behave-parallel
* https://github.com/behave/behave/
* https://github.com/SeleniumHQ/docker-selenium
* https://github.com/SeleniumHQ/docker-selenium#debugging
* http://pre-commit.com/
