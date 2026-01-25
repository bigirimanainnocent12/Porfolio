import urllib.request
import os

assets_dir = r"c:\Users\Utilisateur\Desktop\Projet a faire\Porfolio\assets"
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

# Using a public Wikimedia URL which is usually very stable
url = "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Lallemand_Inc_Logo.svg/512px-Lallemand_Inc_Logo.svg.png"
logo_path = os.path.join(assets_dir, "lallemand_logo.png")

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

try:
    print(f"Downloading Lallemand logo to {logo_path}...")
    urllib.request.urlretrieve(url, logo_path)
    print("Download successful!")
except Exception as e:
    print(f"Failed to download: {e}")
