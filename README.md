## Start Machine Learning Project

### Software and account requirement:

1. Github Account:
[Github Account](https://github.com)
2. [Heruko Account](https://id.heroku.com/login)
3. VS Code IDLE: (https://code.visualstudio.com/download)
4. GIT cli: (https://git-scm.com/downloads)
5.  [Git Tutorial](https://git-scm.com/docs)

### Creating conda Virtual Envirornament
```
 conda create -p venv python==3.7 -y
 ```

 ```
 conda activate venv/
 ```


 ```
 pip install -r requirement.txt
 ```
 

 To add files to git
 ```
 git add.
 ```

 or
 ```
 git add <file_name>
 ```

NOTE: To ignore file or the folder from git we can write the name of file/folder in .gitignore

To check the git status
```
git status
```
To check all version maintined by git log
```
git log
```

To create version/commit all changes by git
```
git commit -m "Message"

To send version/changes to github
```
git push origin main
```

```
to check remote URL
```
git remote -v
```

To Setup CI/CD pipeline in AWS BEANSTACK we need 

1. AWS_BEANSTALK_EMAIL = vinaycshekhar215@gmail.com
2. AWS_API_KEY = Machinelearning-env.eba-7shizg7t.ap-northeast-1.elasticbeanstalk.com
3. AWS_APP_NAME: Machine_Learning



BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .

>Note:Image name for docker should be in lowercase

To list Docker images 
```
docker image
```
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 eb45ab1ff5c6
```
TO Check running container in docker
```
docker ps
```
To Stop Docker Container
```
docker stop <container_id>
```

```
python setup.py install
```

Install ipykernel
```
pip install ipykernel
```

