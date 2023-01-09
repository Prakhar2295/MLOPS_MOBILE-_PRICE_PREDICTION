## It is divided into 4 stages:
1.)Load & save the data
2.)Split the data
3.)Training the data
4.)Evaluation of the model

## Commands Used 
conda create -n DVC-MPRICE python=3.7 -y

conda activate DVC-ML

git init

git remote add origin https://github.com/Prakhar2295/MLOPS_MOBILE-_PRICE_PREDICTION.git

git checkout -b main

touch requirements.txt

pip install -r requirements.txt

dvc init

touch dvc.yaml touch params.yaml

touch requirements.txt

touch .gitignore

mkdir -p src/utils

mkdir config

touch config/config.yaml

touch setup.py 
