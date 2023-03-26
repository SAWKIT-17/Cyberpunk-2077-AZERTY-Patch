import os
import shutil
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
            os.system('cls')
            messagebox.showerror('Dossier introuvable', 'Le dossier sélectionné ne contient pas le jeu Cyberpunk 2077 !')

os.system('cls')

patch_path = os.path.realpath(__file__)
for i in range(2):
    patch_path = os.path.dirname(patch_path)
patch_path = os.path.join(patch_path, "src")

patch_file = os.path.join(patch_path, 'inputUserMappings.xml')
origin_file = os.path.join(game_path, 'inputUserMappings.xml')

print(f"Patch \'{patch_file}\' ---> \'{origin_file}\'")
err_copy = shutil.copyfile(patch_file, origin_file)
if err_copy == origin_file:
    messagebox.showinfo('Patch appliqué', 'Le patch a été appliqué avec succès !')