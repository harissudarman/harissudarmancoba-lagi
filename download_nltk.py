<import nltk
import os

# Tentukan lokasi unduhan nltk_data
nltk_data_path = os.path.join(os.getcwd(), "nltk_data")

# Buat folder nltk_data jika belum ada
os.makedirs(nltk_data_path, exist_ok=True)

# Unduh dataset 'punkt'
nltk.download('punkt_tab', download_dir=nltk_data_path)
