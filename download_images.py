import urllib.request
import os

assets_dir = r"c:\Users\Utilisateur\Desktop\Projet a faire\Porfolio\assets"
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

images = {
    "sales.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Business_Dashboard.png/800px-Business_Dashboard.png",
    "insurance.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Deep_Learning.png/800px-Deep_Learning.png",
    "airflow.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Flowchart.png/800px-Flowchart.png",
    "anova.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Boxplot_vs_PDF.png/800px-Boxplot_vs_PDF.png",
    "manala.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/c5/Manala_-_Jean_Paille.jpg/800px-Manala_-_Jean_Paille.jpg"
}

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

for filename, url in images.items():
    try:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, os.path.join(assets_dir, filename))
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
