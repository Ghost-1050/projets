# python setup.py build

from cx_Freeze import setup, Executable


setup(
    name="Training_Programme",
    version="1.0",
    description="Mon programme d'entrainement",
    executables=[Executable("main.py")]
)
