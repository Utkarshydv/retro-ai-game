import os

def clean_title(filename):
    return os.path.splitext(filename)[0].replace("_", " ").replace("-", " ").title()

def get_roms_by_console():
    systems = {
        "psp": "assets/psp_roms",
        "3ds": "assets/3ds_roms"
    }
    rom_data = {}

    for system, folder in systems.items():
        roms = []
        if os.path.exists(folder):
            for file in os.listdir(folder):
                if file.lower().endswith(('.iso', '.bin', '.cia', '.3ds')):
                    roms.append({
                        "title": clean_title(file),
                        "path": os.path.join(folder, file)
                    })
        rom_data[system] = roms
    return rom_data
