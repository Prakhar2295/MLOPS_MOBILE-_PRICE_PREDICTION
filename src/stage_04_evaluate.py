from src.utils.all_utils import create_directory, read_yaml,save_report
import joblib
import os
import argparse
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import pandas as pd
import numpy as np

def evaluate_metrics(actuial_values,predicted_values):
    rmse = np.sqrt(mean_squared_error(actuial_values,predicted_values))
    mae = mean_absolute_error(actuial_values,predicted_values)
    r2  = r2_score(actuial_values,predicted_values)
    return r2,mae,rmse


def evaluate(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    split_data_dir = config["artifacts"]["split_data_dir"]
    test_data = config["artifacts"]["test"]

    test_data_path = os.path.join(artifacts_dir,split_data_dir,test_data)

    test_data = pd.read_csv(test_data_path)

    x_test = test_data.drop("price_range",axis = 1)
    y_test = test_data["price_range"]
    

    model_dir = config["artifacts"]["model_dir"]
    model_filename = config["artifacts"]["model_filename"]

    model_file_path = os.path.join(artifacts_dir,model_dir,model_filename)

    lr = joblib.load(model_file_path)

    predicted_values = lr.predict(x_test)

    rmse, mae, r2 = evaluate_metrics(y_test,predicted_values)

    scores_dir = config["artifacts"]["reports_dir"]
    scores_filename = config["artifacts"]["scores"]

    scores_dir_path = os.path.join(artifacts_dir, scores_dir)

    create_directory([scores_dir_path])

    scores_file_path = os.path.join(scores_dir_path,scores_filename)

    print(scores_file_path)

    scores = {
        "rmse": rmse,
        "mae": mae,
        "r2": r2

    }

    save_report(report = scores, report_path = scores_file_path)






















if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default = "params.yaml")

    parsed_args = args.parse_args()

    evaluate(config_path = parsed_args.config,params_path = parsed_args.params)