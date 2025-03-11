from tkinter import filedialog
import zipfile
import os


def extract_skins(source_zip, target_directory):
    with zipfile.ZipFile(source_zip, 'r') as main_zip:
        file_list = main_zip.namelist()

        # Filtre anti-chroma
        skin_zips = [f for f in file_list if f.endswith('.zip') and 'chromas' not in f]

        for skin_zip in skin_zips:
            skin_name = os.path.splitext(os.path.basename(skin_zip))[0]
            skin_folder = os.path.join(target_directory, skin_name)
            os.makedirs(skin_folder, exist_ok=True)

            with main_zip.open(skin_zip) as skin_zip_file:
                with zipfile.ZipFile(skin_zip_file, 'r') as skin_archive:
                    skin_archive.extractall(skin_folder)
                    print(f"Extracted {skin_name} to {skin_folder}")

if __name__ == "__main__":
    zip_file_path = filedialog.askopenfilename(
    title="Sélectionner lol-skin-main.zip",
    filetypes=[("Fichiers ZIP", "*.zip")]
)
    output_directory = filedialog.askdirectory(title="Sélectionner le dossier cslol-manager")
    extract_skins(zip_file_path, output_directory)
