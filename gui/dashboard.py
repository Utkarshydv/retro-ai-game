import streamlit as st
from api.rom_parser import get_roms_by_console
from api.game_fetcher import fetch_game_data
import os
import subprocess

def launch_rom(path, system):
    emulator_paths = {
        "psp": "/Applications/PPSSPP.app",
        "3ds": "/Applications/Citra.app"
    }
    try:
        subprocess.Popen(["open", "-a", emulator_paths[system], path])
        return True
    except Exception as e:
        st.error(f"Launch failed: {e}")
        return False

def render_game_section(console_name, system_key, roms):
    st.markdown(f"<h2 style='color:#ffcc00;'>{console_name}</h2>", unsafe_allow_html=True)

    cols = st.columns(2)
    for idx, rom in enumerate(roms):
        col = cols[idx % 2]
        with col:
            rom_name = rom["title"]
            rom_path = rom["path"]
            metadata = fetch_game_data(rom_name)

            if metadata:
                st.image(metadata["cover"], width=150)
                st.markdown(f"**{metadata['name']}**  \n🗓 {metadata['released']}  \n⭐ {metadata['rating']}")
            else:
                st.write(f"**{rom_name}**  \n_Metadata not found_")

            if st.button(f"▶ Launch {rom_name}", key=f"{rom_name}_{system_key}"):
                launch_rom(rom_path, system_key)

def render_dashboard():
    roms = get_roms_by_console()
    st.markdown("---")
    render_game_section("🎮 PlayStation Portable", "psp", roms.get("psp", []))
    st.markdown("---")
    render_game_section("🎮 Nintendo 3DS", "3ds", roms.get("3ds", []))
