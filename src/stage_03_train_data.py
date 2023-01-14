from src.utils.all_utils import create_directory, read_yaml
import joblib
import os
import argparse
from sklearn.linear_model import ElasticNet
import pandas as pd


def train_data(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    split_data_dir = config["artifacts"]["split_data_dir"]

    train_data_path = config["artifacts"]["train"]

    train_data_file_path = os.path.join(artifacts_dir,split_data_dir,train_data_path)

    train_data = pd.read_csv(train_data_file_path)

    x_train = train_data.drop("price_range",axis=1)
    y_train = train_data["price_range"]

    alpha = params["model_params"]["alpha"]
    l1_ratio = params["model_params"]["l1_ratio"]
    random_state = params["base"]["random_state"]

    lr = ElasticNet(alpha = alpha, l1_ratio = l1_ratio, random_state = random_state)
    lr.fit(x_train,y_train)

    model_dir = config["artifacts"]["model_dir"]
    model_filename = config["artifacts"]["model_filename"]

    model_dir_path = os.path.join(artifacts_dir, model_dir)

    create_directory([model_dir_path])

    model_file_path = os.path.join(model_dir_path, model_filename)

    joblib.dump(lr ,model_file_path)









if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default = "params.yaml")

    parsed_args = args.parse_args()

    train_data(config_path = parsed_args.config,params_path = parsed_args.params)