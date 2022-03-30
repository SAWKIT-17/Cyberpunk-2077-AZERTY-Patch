import os
import shutil

jeu_chemin = "C:\Program Files (x86)\GOG Galaxy\Games\Cyberpunk 2077"
jeu_chemin = os.path.join(jeu_chemin, "r6", "config")
if not os.path.exists(jeu_chemin):
    while True:
        jeu_chemin = input('Veuillez indiquer le chemin jusqu\'au jeu: ')
        jeu_chemin = os.path.join(jeu_chemin, "r6", "config")
        if os.path.exists(jeu_chemin):
            break
        else:
            os.system('cls')
            print('Jeu non trouvé, veuillez réessayer.\n')

os.system('cls')

patch_chemin = os.path.realpath(__file__)
for i in range(2):
    patch_chemin = os.path.dirname(patch_chemin)
patch_chemin = os.path.join(patch_chemin, "src")

patch_file = os.path.join(patch_chemin, 'inputUserMappings.xml')
origin_file = os.path.join(jeu_chemin, 'inputUserMappings.xml')

print(f"Patch \'{patch_file}\' ---> \'{origin_file}\'")
err_copy = shutil.copyfile(patch_file, origin_file)
if err_copy == origin_file:
    print('\nTerminé avec succès !')