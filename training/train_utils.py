import os

DATA_DIR='data'
data_file_name='car-details.csv'

data_file_path=os.path.join(DATA_DIR,data_file_name)


app_dir='app'
model_dir_name='models'
model_name='model.joblib'
model_dir=os.path.join(app_dir,model_dir_name)
model_path=os.path.join(model_dir,model_name  )