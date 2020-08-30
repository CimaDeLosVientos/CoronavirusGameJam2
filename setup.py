import cx_Freeze
 
executables = [cx_Freeze.Executable("main.py")]
                                  #base = "Win32GUI",
                                  #icon = "assets/bobi_icon.png")]
 
build_exe_options = {"packages": ["pygame"],
                     "include_files":["src", "assets"]}
 
cx_Freeze.setup(
    name = "LaSuite",
    version = "0.5",
    description = "Juego La Suite",
    options={"build_exe": build_exe_options},
    executables = executables
    )
