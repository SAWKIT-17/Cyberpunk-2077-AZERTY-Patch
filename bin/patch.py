import os
import shutil
from urllib import request
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

game_path = "C:\Program Files (x86)\GOG Galaxy\Games\Cyberpunk 2077"
game_path = os.path.join(game_path, "r6", "config")
if not os.path.exists(game_path):
    while True:
        game_path = filedialog.askdirectory(title="Sélectionnez le dossier du jeu Cyberpunk 2077")
        game_path = os.path.join(game_path, "r6", "config")
        if os.path.exists(game_path):
            break
        else:
            messagebox.showerror('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'Le dossier sélectionné ne contient pas le jeu Cyberpunk 2077 !')

patch_path = os.path.realpath(__file__)
print(patch_path)
for i in range(2):
    patch_path = os.path.dirname(patch_path)
patch_path = os.path.join(patch_path, "src")

patch_file = os.path.join(patch_path, 'inputUserMappings.xml')
origin_file = os.path.join(game_path, 'inputUserMappings.xml')

try:
    print(f"Patch \'{patch_file}\' ---> \'{origin_file}\'")
    err_copy = shutil.copyfile(patch_file, origin_file)
    if err_copy == origin_file:
        messagebox.showinfo('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'Le patch a été appliqué avec succès !')
except FileNotFoundError:
    url = 'https://github.com/SAWKIT-17/Cyberpunk-2077-mapping-AZERTY-FIX/blob/main/src/inputUserMappings.xml'
    response = request.urlopen(url)
    if response.status_code == 200:
        try:
            request.urlretrieve(url, patch_file)
            messagebox.showinfo('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'Le patch a été appliqué avec succès !')
        except:
            messagebox.showerror('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'ERREUR : Impossible de modifier votre fichier. Vérifiez vos permissions.')
    else:
        messagebox.showerror('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'ERREUR : Impossible de télécharger les fichiers nécessaires. Vérifiez votre connexion internet.')