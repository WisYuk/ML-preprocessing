import time
import os
from google_images_search import GoogleImagesSearch
from googleapiclient.errors import HttpError
import pandas as pd
import re
# Provide API key and CX
gis = GoogleImagesSearch('API_KEY_MU_DEWE', 'CX_KEY_MU_DEWE') 

def check_file_exists(directory, filename):
    filepath = os.path.join(directory, filename)
    
    if os.path.isfile(filepath):
        return True
    else:
        return False
    
# Retry mechanism
def search_with_retries(gis, search_params, retries=3, delay=5):
    for attempt in range(retries):
        try:
            gis.search(search_params=search_params, width=1600, height=1200)
            return gis.results()
        except HttpError as e:
            print(f"Attempt {attempt + 1} failed with error: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise
# df =pd.read_csv("./data tourism - db_hotel.csv")
# df =pd.read_csv("./data tourism - db_ride.csv")
df =pd.read_csv("./data tourism - tourism_with_id.csv")
# Execute search with retries
for id, (index, row) in enumerate(df.iterrows(), start=1):
    # if id <=77:
    #     continue
    kendaraan = row['Nama Kendaraan']
    perusahaan = row['Perusahaan']
    _search_params = {
        # 'q': kendaraan + ' transportation' + ' ' + perusahaan,
        'q' : row['Place_Name'],
        'num': 1,
        'fileType': 'jpg',
        'imgType': 'photo',
        'safe': 'high',
        'imgSize': 'xxlarge'
    }
    try:
        results = search_with_retries(gis, _search_params)
        for image in results:
            image.download('.')  # Download image to the specified directory
            image.resize(1600, 1200)
            downloaded_path = image.path  # Get the downloaded local file path
            new_path = os.path.join('.', '{}.jpg'.format(id))  # Define the new path with the desired name

            if os.path.exists(downloaded_path):  # Check if the image exists
                try:
                    os.rename(downloaded_path, new_path)  # Rename the downloaded file
                except PermissionError as e:
                    print(f"Permission error when renaming the file: {e}")
            else:
                print("Failed to download the image. File does not exist.")
    except HttpError as e:
        print(f"Failed to retrieve images after multiple attempts: {e}")
