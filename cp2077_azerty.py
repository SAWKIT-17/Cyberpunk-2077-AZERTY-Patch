import os
import shutil
import sys
import requests
import tempfile
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import xml.etree.ElementTree as ET


def download_icon(url):
    response = requests.get(url)
    if response.status_code == 200:
        _, filename = tempfile.mkstemp()
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename
    else:
        raise Exception(f"Impossible de télécharger l'icône depuis {url}")

def set_icon(root, icon_url):
    try:
        icon_path = download_icon(icon_url)
        root.iconbitmap(default=icon_path)
    except Exception as e:
        print(str(e))

root = tk.Tk()
app_path = os.path.dirname(sys.executable)
icon_url = "https://filedn.eu/lWsEldFrD0ljPhHINdv6TVJ/sawkit/static/Cyberpunk-2077-AZERTY-Patch/icon.ico"
set_icon(root, icon_url)
root.withdraw()


def patch():
    if not os.path.exists(backup_file):
        shutil.copyfile(origin_file, backup_file)

    try:
        tree = ET.parse(origin_file)
        root = tree.getroot()

        key_replacements = {
            'IK_W': 'IK_Z',
            'IK_A': 'IK_Q',
            'IK_Z': 'IK_W',
            'IK_Q': 'IK_A'
        }

        attrib_replacements = [
            'popup_prior',
            'popup_halveQuantity',
            'FreeCam_UpDown_Axis',
            'Notification_Button',
            'QuickMelee_Button',
            'BraindancePlayBackward_Button',
            'ToggleQHackDescription',
            'CycleObjectives_Button',
            'PickUpBodyFromTakedown_Button',
            'BodyDrop_Button',
            'VehicleCameraToggle',
            'Vehicle_Horn',
            'UI_MoveUpSms',
            'UI_MoveUp',
            'Dialog_Choice_Up',
            'PrevItem_Button',
            'CameraStepForward',
            'CameraStepLeft',
            'CameraStepDown',
            'video_prior',
            'world_map_menu_cycle_filter_prev',
            'world_map_filter_navigation_up',
            'show_all_popup',
            'disassemble_item',
            'delete_wardrobe_set',
            'option_switch_prev',
            'sub_option_switch_prev',
            'option_switch_prev_settings',
            'brightness_settings',
            'character_preview_rotate',
            'sms_view_scroll_km',
            'PhotoMode_Prior_Menu',
            'minigame_menu_up',
            'roach_race_jump',
            'PocketRadio_Button'
        ]

        for mapping in root.findall('.//mapping'):
            for button in mapping.findall('.//button'):
                button_id = button.get('id')
                overridable_ui = button.get('overridableUI')

                if button_id in key_replacements and overridable_ui and ('forward' in overridable_ui or 'left' in overridable_ui or 'vehicleAccelerate' in overridable_ui or 'vehicleSteerLeft' in overridable_ui):
                    new_button_id = key_replacements[button_id]
                    button.set('id', new_button_id)
                elif 'name' in mapping.attrib and mapping.attrib['name'] in attrib_replacements:
                    if button_id in key_replacements:
                        new_button_id = key_replacements[button_id]
                        button.set('id', new_button_id)

        tree.write(origin_file, encoding='utf-8')
        messagebox.showinfo('Patch AZERTY - Cyberpunk 2077', 'Le patch a été appliqué avec succès !')
        on_closing()

    except Exception as e:
        if os.path.exists(backup_file):
            shutil.copyfile(backup_file, origin_file)
        messagebox.showerror('Patch AZERTY - Cyberpunk 2077', f'ERREUR : {str(e)}')

def restore():
    if os.path.exists(backup_file):
        shutil.copyfile(backup_file, origin_file)
        messagebox.showinfo('Patch AZERTY - Cyberpunk 2077', 'La sauvegarde a été restaurée avec succès !')
        os.remove(backup_file)
        on_closing()
    else:
        messagebox.showerror('Patch AZERTY - Cyberpunk 2077', 'Aucune sauvegarde disponible.')

def on_closing():
    #root.destroy()
    sys.exit(0)

def main():
    root = tk.Tk()
    root.title("Patch AZERTY by SAWKIT - Cyberpunk 2077 v2.1")
    root.protocol("WM_DELETE_WINDOW", on_closing)

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    for i in range(3):
        root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(0, weight=1)


    title_label = tk.Label(frame, text="Patch AZERTY - Cyberpunk 2077", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))


    button_frame = tk.Frame(frame)
    button_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    patch_button = tk.Button(button_frame, text="Patch", font=("Segoe UI", 12), command=patch)
    patch_button.grid(row=0, column=0, padx=10, pady=10)

    restore_button = tk.Button(button_frame, text="Restore", font=("Segoe UI", 12), command=restore)
    restore_button.grid(row=0, column=1, padx=10, pady=10)


    credits_label = tk.Label(frame, text="Developers:\nSAWKIT\n\nContributors:\n...", font=("Segoe UI", 10))
    credits_label.grid(row=2, column=0, columnspan=3, pady=(10, 0))

game_path = "C:\Program Files (x86)\GOG Galaxy\Games\Cyberpunk 2077"
game_path = os.path.join(game_path, "r6", "config")
if not os.path.exists(game_path):
    messagebox.showinfo('Patch AZERTY - Cyberpunk 2077', 'Le dossier du jeu est introuvable ! Veuillez sélectionner le dossier du jeu.')
    while True:
        game_path = filedialog.askdirectory(title="Sélectionnez le dossier du jeu Cyberpunk 2077")
        game_path = os.path.join(game_path, "r6", "config")
        if os.path.exists(game_path):
            break
        else:
            messagebox.showerror('Patch AZERTY - Cyberpunk 2077', 'Le dossier sélectionné ne contient pas le jeu Cyberpunk 2077 !')

origin_file = os.path.join(game_path, 'inputUserMappings.xml')
backup_file = origin_file + '.backup'

if __name__ == "__main__":
    main()
    root.mainloop()