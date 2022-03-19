import os, datetime
os.system("pip install pyinstaller")
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
colorama.init()
class DESIGN():
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    BLUE = '\x1b[36m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    greenplus = f"{WHITE}[ {GREEN}+{WHITE} ]"
    blueplus = f"{WHITE}[ {BLUE}+{WHITE} ]"
    redminus = f"{WHITE}[ {RED}-{WHITE} ]"
    bluefile = f"{WHITE}[ {BLUE}FILE {WHITE}]"
    redfile = f"{WHITE}[ {RED}FILE {WHITE}]"
    xrblue = f"\n{blueplus} Py To Exe {BLUE}/ {WHITE}Instagram{BLUE}: {WHITE}@xnce {BLUE}/ {WHITE}@ro1c"
class Xnce():
    def __init__(self):
        print(DESIGN.xrblue)
    def inex(self):
        print(f"\n{DESIGN.redminus} Enter To Exit: ", end="")
        input()
        exit()
    def py_to_exe(self, path):
        my_path = os.path.realpath(__file__).replace('\\', '/')
        if '"' in path:
            filename = path.split('"')[1].split("\\")[-1]
        else:
            filename = path.split("\\")[-1]
        dt = f"{str(datetime.datetime.now().date())} {str(datetime.datetime.now().time()).split('.')[0].replace(':', '.')}"
        os.system(f'pyinstaller --distpath "exe/{filename}({dt})" --workpath "exe/{filename}({dt})" --specpath "exe/{filename}({dt})" --noconfirm --onefile --console {path}')
        print(f"\n{DESIGN.blueplus} Saved In {DESIGN.BLUE}{my_path.replace(my_path.split('/')[-1], '')}exe/{filename}({dt})")
x = Xnce()
print(f"\n{DESIGN.bluefile} Drag Python File Here: ", end="")
path = input()
if ".py" not in path[-4:]:
    print(f"\n{DESIGN.redfile} Please Drag (.py) File", end="")
    x.inex()
x.py_to_exe(path)
x.inex()
