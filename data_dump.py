import pymongo
import pandas as pd
import json
#provide the mongodb localhost url to connct python to mongodb
client=pymongo.MongoClient("mongodb+srv://abhi0557:abhi29894@clustor0.zr9ru.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "D:/proj_1_adult_census_prediction/final_data_with_SMOTE.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "aps_final_train_set1"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

   #convert dataframe to jason format so thet we can dump record in mongo db
   #df.reset_index(drop=True, inplace=True)

   #json_record = list(json.loads(df.T.to_json()).values())
   #print(json_record[0])