import yaml
import os
import pandas as pd
import json

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)


    return content



def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok = True)
        print(f"directory has been created at {dir_path}")


def save_local_df(data, data_path):
    data= data.to_csv(data_path, index = False)
    print(f"training data & testing data has been saved at {data_path}")
    return data

def save_report(report: dict,report_path: str, indentation= 4):
    with open(report_path,"w") as f:
        json.dump(report, f, indent= indentation)
    print(f"report are saved at {report_path}")    
        

  
