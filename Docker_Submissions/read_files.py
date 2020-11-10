import os, pandas as pd, random, sys

# Sample Deep Learning Run
import sample_deep_learning_model

# for local development
#IN = 'directory_of_files'
#OUT = 'output_dir'

# for use with docker mounts
IN = '/mnt/in'
OUT = '/mnt/out'


if __name__ == "__main__":
    files_dir = os.path.join(IN,'Pathology')
    print(files_dir)
    files = [file[0:-5] for file in os.listdir(files_dir) if file.find('.tiff') != -1]
    classes = ['A','O','G']
    submission_csv = pd.DataFrame({"CPM_RadPath_2020_ID":files, "class":[random.choice(classes) for file in files]})
    
    # Deep Learning Model
    sample_deep_learning_model.run()
    # Deep Learning Model

    submission_csv.to_csv(os.path.join(OUT,"random.csv"), index=None)


