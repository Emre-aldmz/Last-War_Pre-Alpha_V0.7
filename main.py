#  //==========================================================================\\
# ((----------------------------------Libraries---------------------------------))
#  \\==========================================================================//

import random
import time 
import os
import sys
from rich.console import Console
from rich.panel import Panel

#  //==========================================================================\\
# ((---------------------------------FUNCTIONS----------------------------------))
#  \\==========================================================================//

console = Console() # console başlat

# <----------------------------Slow_Write_Mode---------------------------------->
def slow_write(write, speed=0.04,style=None):
    for letter in write:
        console.print(letter, style=style, end="")    
        time.sleep(speed)         
    print() 

# <------------------------------Terminal_clear--------------------------------->
def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

red = "bold red"
green = "bold green"
blue = "bold blue"
cyan = "cyan"
black = "bold black"
purple = "bold purple"

#  //==========================================================================\\
# ((------------------------------Login_Screen----------------------------------))
#  \\==========================================================================//

screen_clear()

slow_write(r" _____                      ___  _     _",0.01,style=green)
slow_write(r"|  ___|                    / _ \| |   | |",0.01,style=green)
slow_write(r"| |__ _ __ ___  _ __ ___  / /_\ \ | __| |_ _ __ _ __ ___   __ _ ____",0.01,style=green)
slow_write(r"|  __| '_ ` _ \| '__/ _ \ |  _  | |/ _` | | '__| '_ ` _ \ / _` |_  /",0.01,style=green)
slow_write(r"| |__| | | | | | | |  __/ | | | | | (_| | | |  | | | | | | (_| |/ / ",0.01,style=green)
slow_write(r"\____/_| |_| |_|_|  \___| \_| |_/_|\__,_|_|_|  |_| |_| |_|\__,_/___|",0.01,style=green)

time.sleep(1.5)
screen_clear()

slow_write(r" _              _____     _     _____ _",0.01,style=blue)
slow_write(r"| |            |  ___|   (_)   |  _  | |",0.01,style=blue)
slow_write(r"| |__  _   _   | |__ _ __ _ ___| | | | |_ ___",0.01,style=blue)
slow_write(r"| '_ \| | | |  |  __| '__| / __| | | | __/ _ \ ",0.01,style=blue)
slow_write(r"| |_) | |_| |  | |__| |  | \__ \ \/' / ||  __/",0.01,style=blue)
slow_write(r"|_.__/ \__, |  \____/_|  |_|___/\_/\_\\__\___|",0.01,style=blue)
slow_write(r"        __/ |",0.01,style=blue)
slow_write(r"       |___/ ",0.01,style=blue)

time.sleep(1.5)
screen_clear()

slow_write(r"              _       ___   _____ _____   _    _  ___  ______",0.01,style=purple)
slow_write(r"             | |     / _ \ /  ___|_   _| | |  | |/ _ \ | ___ \ ",0.01,style=purple)
slow_write(r"             | |    / /_\ \\ `--.  | |   | |  | / /_\ \| |_/ /",0.01,style=purple)
slow_write(r"             | |    |  _  | `--. \ | |   | |/\| |  _  ||    /",0.01,style=purple)
slow_write(r"             | |____| | | |/\__/ / | |   \  /\  / | | || |\ \ ",0.01,style=purple)
slow_write(r"             \_____/\_| |_/\____/  \_/    \/  \/\_| |_/\_| \_|",0.01,style=purple)     


        
        

#  //==========================================================================\\
# ((--------------------------------Interface-----------------------------------))
#  \\==========================================================================//

Character_pool = {                                                  
    "Gladyator" : ["Alonzo","Erok","Proxgaint","Rockby"],
    "Wizard" : ["Gloria","Adam","Kun","Samuel"],                             # Statları eklenecek v1.5
    "Archer" : ["Emrey","Ahu","Elegante","Eriksen"],
    "King" : ["Mr. Salvo","Kin","T.U.R.X"]
}

Pick_Character_lst = []
Character_lst = ["Gladyator","Wizard","Archer","King"]

pick0=" "
while pick0 != "quit" and pick0 != "3":
    slow_write("<<==========================================================================>>",0.001)
    slow_write("                          (1)  #Oyna",0.001)
    slow_write("                          (2)  #Ayarlar",0.001)
    slow_write("                          (3)  #Quit",0.001)

    pick0 = input().lower()
    screen_clear()
    if pick0 == "1" or pick0 == "oyna":

        for x in Character_lst:
            attemp = 3 # deneme hakki
            character_now = Character_pool[x]
            character_number = len(character_now)
            True_pick = False
            while 0 < attemp :

                try:
                    print("*"*100)
                    time.sleep(1)
                    number = "/".join([str(sayi) for sayi in range(1,character_number+1)]) # bunun sayesinde 1/2/3 yazırıyorum ne kadar varsa 1 den character_numer +1 e kadar
                    slow_write(f"Mevcut karakterler: {character_now}")                          # çünkü character_number 0 dan başlıyor 1 den +1 ine kadar
                    time.sleep(1)
                    pick = int(input(f"{x} için Seçin: {number}: "))
                    time.sleep(1)
                    if pick != 0:
                        Pick_Character_lst.append(character_now[pick-1])
                        print(f"{character_now[pick-1]} Seçildi.")
                        time.sleep(1)
                        True_pick = True
                        break
                    else:
                        attemp -= 1
                        if attemp != 0:
                            print("Lütfen geçerli bir rakam giriniz!!")
                            time.sleep(1)
                            print(f"Deneme Hakkınız: {attemp}")
                            time.sleep(1)
                        else:
                            print(f"Deneme hakkınız bitmiştir {x} rastgele atanmıştır!!")
                            time.sleep(1)
                except:
                    attemp -= 1
                    if attemp != 0:
                        print("Lütfen geçerli bir rakam giriniz!!")
                        time.sleep(1)
                        print(f"Deneme Hakkınız: {attemp}")
                        time.sleep(1)
                    else:
                        print(f"Deneme hakkınız bitmiştir {x} rastgele atanmıştır!!")
                        time.sleep(1)

            if attemp == 0 or True_pick == False:
                randomCharacter = random.choice(character_now)
                Pick_Character_lst.append(randomCharacter)
        

        print(f"Takım oluşturuldu: {Pick_Character_lst}")
        time.sleep(1)

        EnemyPick_Character_lst = [] # LETS GO FUCKİNG GO
        for i in Character_lst:
            EnemyPick_Character = random.choice(Character_pool[i])   # Botun takımı 
            EnemyPick_Character_lst.append(EnemyPick_Character)
        print(f"Rakip takımın savaşçıları ve kralı: {EnemyPick_Character_lst}")
        break

#  //==========================================================================\\
# ((--------------------------------Settings------------------------------------))
#  \\==========================================================================//   

    if pick0 == "ayarlar" or pick0 == "2":          # settings kısmı şuanlık boş
        print("empty for now")
        break





        
        


















