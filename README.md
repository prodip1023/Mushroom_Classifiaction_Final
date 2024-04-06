## Mushroom_Classifiaction_Final

| PROJECT TITLE | MUSHROOM CLASSIFICATION |
|----------|----------|
| TECHNOLOGIES| MACHINE LEARNING TECHNOLOGY|
|DOMAIN|AGRICULTURE|
|PROJECT DEFICULTIES LEVEL|INTERMEDIATE|
|NAME|PRODIP SARKAR|
|EMAIL ID|prodip1023@gmail.com|
|GITHUB LINK|https://github.com/prodip1023|
|DATE CREATED| 25th February, 2024|
|DATE MODIFIED| 27th February, 2024|
|KAGGLE LINK|https://www.kaggle.com/prodip1023|
|LINKEDN LINK|https://www.linkedin.com/in/prodip1023/|
|PROJECT LINK | https://github.com/prodip1023/Mushroom_Classifiaction_Final|

### Software and Account Requirements:

1. [Github Account](https://github.com/)
2. [VSCode](https://code.visualstudio.com/)
3. [Git-SCM](https://git-scm.com/)
4. [AWS](https://aws.amazon.com/console)
5. [Git Documentation](https://git-scm.com/docs/git)
6. [Git Action](https://docs.github.com/en/actions)


Creating conda environment
```
conda create -p venv python==3.10 -y #prefix - current  directory create  a new environment with the name 'venv'.
```
Activate the environment
```
conda activate venv/
```
Create reqiremnts.txt file on `Project Directory`
```
pip install -r requirements.txt
```

OR 
```
bash init_setup.sh
```

Add git file
```
git add <file_name>
```
OR 
```
git add .
```
> Note: To ignore file or folder  just write `.<filename>` or `<folder_name>` in `.gitignore

To Check the git status 
```
git status
```
To check all version maintained  by Git
```
git log
```

To  commit your changes with a message :
```
git commit -m "<Your Message>"
```
To send version/changes to Github 
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in AWS we need 2 information
1. AWS_ACCESS_KEY_ID:
2. AWS_SECRET_ACCESS_KEY:
3. AWS_REGION:

Build Docker Image
```
docker build -t <image_name>:<tag_name> .
```
> Note: Image name for docker must be lower case

To list docker iamge 
```
docker images
```
or 
```
docker image ls
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 a16d595f993f # ImageID
```
To check the running Container in docker
```
docker ps 
```

To  stop running Container
```
docker stop <container_id>
```

```
python3 setup.py install
```
Install ipykernel
```
pip install ipykernel
```
Read the yaml file using PyYAML 
```
pip install PyYAML
```
