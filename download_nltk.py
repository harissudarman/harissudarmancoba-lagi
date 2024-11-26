import nltk
import os

# Tentukan path untuk data NLTK
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
os.makedirs(nltk_data_path, exist_ok=True)
nltk.data.path.append(nltk_data_path)

# Unduh dataset 'punkt'
nltk.download('punkt', download_dir=nltk_data_path)
