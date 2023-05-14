from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Projet titouan Youtube",
    version = "1.1",
    description = "Programme permettant de telecharger des vidéos youtube",
    executables = [Executable("Projet Titouan Youtube.py", base="Win32GUI",targetName="Projet Titouan Youtube")],
    options={
        "build_exe": {
            "includes": ["PIL.Image","PIL.ImageTk","tkinter.filedialog"],
            'include_files': ["ytico2.ico",'youtube (1).png'],
            "packages": [ "tkinter","pytube"],
            "optimize":1,
        }}
)