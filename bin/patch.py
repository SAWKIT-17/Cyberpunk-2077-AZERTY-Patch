import os
import sys
import shutil
import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

game_path = "C:\Program Files (x86)\GOG Galaxy\Games\Cyberpunk 2077"
game_path = os.path.join(game_path, "r6", "config")
if not os.path.exists(game_path):
    messagebox.showinfo('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'Le dossier du jeu est introuvable ! Veuillez sélectionner le dossier du jeu.')
    while True:
        game_path = filedialog.askdirectory(title="Sélectionnez le dossier du jeu Cyberpunk 2077")
        game_path = os.path.join(game_path, "r6", "config")
        if os.path.exists(game_path):
            break
        else:
            messagebox.showerror('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'Le dossier sélectionné ne contient pas le jeu Cyberpunk 2077 !')

if getattr(sys, 'frozen', False):
    patch_path = os.path.dirname(sys.executable)
    patch_path = os.path.join(patch_path, 'src')
else:
    patch_path = os.path.dirname(os.path.abspath(__file__))
    patch_path = os.path.join(patch_path, 'src')

patch_file = os.path.join(patch_path, 'inputUserMappings.xml')
origin_file = os.path.join(game_path, 'inputUserMappings.xml')

try:
    err_copy = shutil.copyfile(patch_file, origin_file)
    if err_copy == origin_file:
        messagebox.showinfo('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'Le patch a été appliqué avec succès !')
except FileNotFoundError:
    url = 'https://raw.githubusercontent.com/SAWKIT-17/Cyberpunk-2077-AZERTY-Patch/main/src/inputUserMappings.xml'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            patch_file = response.content
            with open(origin_file, "wb") as f:
                f.write(patch_file)
            messagebox.showinfo('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'Le patch a été appliqué avec succès !')
        except:
            messagebox.showerror('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'ERREUR : Impossible de modifier votre fichier.')
    else:
        messagebox.showerror('Patch AZERTY - Cyberpunk 2077 by SAWKIT', 'ERREUR : Impossible de télécharger les fichiers nécessaires. Vérifiez votre connexion internet.')