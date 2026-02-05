#  //==========================================================================\\
# ((----------------------------------Libraries---------------------------------))
#  \\==========================================================================//

import random
import time 
import os
import sys
import copy

from rich.console import Console
from rich.panel import Panel
from rich import print


from character_db import *

console = Console() # consolu başlat

red = "bold red"
green = "bold green"
blue = "bold blue"
cyan = "cyan"
black = "bold black"
purple = "bold purple"
white = "bold white"

#  //==========================================================================\\
# ((---------------------------------FUNCTIONS----------------------------------))
#  \\==========================================================================//

# <----------------------------Slow_Write_Mode---------------------------------->
def slow_write(write, speed=0.04,style=None):
    for letter in write:
        console.print(letter, style=style, end="")    
        time.sleep(speed)         
    print() 

# <------------------------------Terminal_clear--------------------------------->
def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# <------------------------------Game_Intro--------------------------------->

def game_intro():
    screen_clear()

    slow_write(r" _____                      ___  _     _",0.01,style=green)
    slow_write(r"|  ___|                    / _ \| |   | |",0.01,style=green)
    slow_write(r"| |__ _ __ ___  _ __ ___  / /_\ \ | __| |_ _ __ _ __ ___   __ _ ____",0.01,style=green)
    slow_write(r"|  __| '_ ` _ \| '__/ _ \ |  _  | |/ _` | | '__| '_ ` _ \ / _` |_  /",0.01,style=green)
    slow_write(r"| |__| | | | | | | |  __/ | | | | | (_| | | |  | | | | | | (_| |/ / ",0.01,style=green)
    slow_write(r"\____/_| |_| |_|_|  \___| \_| |_/_|\__,_|_|_|  |_| |_| |_|\__,_/___|",0.01,style=green)

    time.sleep(1)
    screen_clear()

    slow_write(r" _              _____     _     _____ _",0.01,style=blue)
    slow_write(r"| |            |  ___|   (_)   |  _  | |",0.01,style=blue)
    slow_write(r"| |__  _   _   | |__ _ __ _ ___| | | | |_ ___",0.01,style=blue)
    slow_write(r"| '_ \| | | |  |  __| '__| / __| | | | __/ _ \ ",0.01,style=blue)
    slow_write(r"| |_) | |_| |  | |__| |  | \__ \ \/' / ||  __/",0.01,style=blue)
    slow_write(r"|_.__/ \__, |  \____/_|  |_|___/\_/\_\\__\___|",0.01,style=blue)
    slow_write(r"        __/ |",0.01,style=blue)
    slow_write(r"       |___/ ",0.01,style=blue)

    time.sleep(1)
    screen_clear()

    slow_write(r"              _       ___   _____ _____   _    _  ___  ______",0.01,style=purple)
    slow_write(r"             | |     / _ \ /  ___|_   _| | |  | |/ _ \ | ___ \ ",0.01,style=purple)
    slow_write(r"             | |    / /_\ \\ `--.  | |   | |  | / /_\ \| |_/ /",0.01,style=purple)
    slow_write(r"             | |    |  _  | `--. \ | |   | |/\| |  _  ||    /",0.01,style=purple)
    slow_write(r"             | |____| | | |/\__/ / | |   \  /\  / | | || |\ \ ",0.01,style=purple)
    slow_write(r"             \_____/\_| |_/\____/  \_/    \/  \/\_| |_/\_| \_|",0.01,style=purple)
    loginScreen()     

#  //==========================================================================\\
# ((------------------------------Login_Screen----------------------------------))
#  \\==========================================================================//

EnemyPick_Character_lst = []
Pick_Character_lst = []
Character_lst = ["Gladyator","Gladyator","Wizard","Wizard","Archer","Archer"]
King_lst = ["King"] # daha krallar ve bufları oyuna eklenmedi 
def loginScreen():
    print(Panel.fit("_"*70 +    "\n                         [1] #OYNA" +
                                "\n                         [2] #AYARLAR" +
                                "\n                         [3] #ÇIKIŞ",
                                style="bold white"))

    firstPick = int(input("Seçim: "))

    if firstPick == 1:
        screen_clear()
        startScreen()
    elif firstPick == 2:
        screen_clear()
        settings()
    elif firstPick == 3:
        screen_clear()
        print("Çıkış yapılıyor...")
        time.sleep(2)
        screen_clear()
    else:
        print("Geçerli bir seçenek seçin!!")
        time.sleep(2)
        screen_clear()
        loginScreen()           

def settings():
    print(Panel.fit("Burası şuanlık boş" + "\n [1] Geri",style=red))
    secondPick = int(input("Seçim: "))
    if secondPick == 1:
        screen_clear()
        loginScreen()
    else:
        print("Geçerli bir seçenek seçin!!")
        time.sleep(2)
        screen_clear()
        settings()

def startScreen():
    print("Last War Başlıyor...")
    time.sleep(1)
    start_screen = input("Karakter seçimi için Enter'a Basınız.")
    if start_screen == "":
        screen_clear()
        CharacterPickScreen()
    else:
        print("Tekrar deneyiniz!")
        time.sleep(2)
        screen_clear()
        start_screen()

def CharacterPickScreen():
    Pick_Character_lst.clear()
    EnemyPick_Character_lst.clear()
    for k,ClassName in enumerate(Character_lst):
        attemp = 3
        selected = False
        SelectCharacter = [char for char in Character_pool[ClassName] if char not in Pick_Character_lst]
        print(Panel.fit(f"--- {ClassName.upper()} Listesi --- [{k}/{len(Character_lst)}] Seçim --- {Pick_Character_lst}" ,style=blue))
        for i,char in enumerate(SelectCharacter):
            print(f"{[i+1]} {char.Name} \n❤️Can:{char.Health} | ⚔️Güç:{char.Power} | 🔄 Seri Vuruş: {char.Repetitive}")
            print("\n\n")
        while attemp > 0:          
            try: 
                PickNumber = int(input("Karakter seçiniz: "))
                if 1 <= PickNumber <= len(SelectCharacter):
                    SelectedCharacter = SelectCharacter[PickNumber-1]
                    Pick_Character_lst.append(SelectedCharacter)
                    selected = True
                    print(f"✅ {SelectedCharacter} Seçildi!!")
                    break
                else:
                    attemp -= 1
                    print(f"❌ Lütfen geçerli bir Karekter numarısı seçiniz. Kalan deneme hakkınız '{attemp}'")
            except:
                attemp -= 1
                print(f"❌ Lütfen sadece rakam giriniz. Kalan deneme hakkınız '{attemp}'")
        if attemp == 0 or selected == False:
            SelectedCharacter = random.choice(SelectCharacter)
            Pick_Character_lst.append(SelectedCharacter)
            selected = True
            print("⚠️ Karakter rastgele seçildi!")
            time.sleep(1)
            
        screen_clear()
    screen_clear()
    print(Panel.fit(f"{Pick_Character_lst}",title="Seçilen Karakterler",style=white))
    print("\n\n")
    print(Panel.fit("               [(1)Enter] Onayla   ",style=white))
    print(Panel.fit("               [2] Tekrar Oluştur  ",style=white))
    print(Panel.fit("               [3] Çıkış           ",style=white))
    start_screen2 = input("Seçim: ")
    if start_screen2 == "" or start_screen2 == "1":
        screen_clear()
        print("Karşı takım kuruluyor...")
        time.sleep(1)
        screen_clear()

        for ClassName in Character_lst:
            enemy_names = [c.Name for c in EnemyPick_Character_lst]
            Select_character = [char for char in Character_pool[ClassName] if char.Name not in enemy_names] # Random Enemy picked
            original_select = random.choice(Select_character)
            selected_clone = copy.deepcopy(original_select)
            EnemyPick_Character_lst.append(selected_clone)
        print(f"✅ Karşı takım oluşturuldu!")
        time.sleep(1)
        screen_clear()
        print(Panel.fit(f"{Pick_Character_lst}",title="Senin Takımın",style=white))
        print(Panel.fit(f"{EnemyPick_Character_lst}",title="Karşı Takım",style=white))
        start_screen3 = input("Başlamak için Enter'a basınız!")
        time.sleep(1)
        screen_clear()
        BattleScreen() # battle screen e gider

    elif start_screen2 == "2":
        screen_clear()
        print(Panel.fit("Tekrar oluşturulmak üzere geri gidiliyor",style=white))
        time.sleep(1)
        screen_clear()
        CharacterPickScreen()
    
    elif start_screen2 ==  "3":
        print("Çıkış yapılıyor...")
        time.sleep(1)
        screen_clear()
        loginScreen()
        
    else:
        screen_clear()
        print(Panel.fit("Tekrar oluşturulmak üzere geri gidiliyor",style=white))
        time.sleep(1)
        screen_clear()
        CharacterPickScreen()

def BattleScreen():
    Round = 1 # tur sayısı
    
    while len(Pick_Character_lst) > 0 and len(EnemyPick_Character_lst) > 0:
        screen_clear()
        print(Panel.fit(f"<============================Tur:{Round}============================>")) 
        for i,char in enumerate(Pick_Character_lst):            
            healthbar = char.indexHealth()
            armorbar = char.indexArmor()
            print(Panel.fit(f"[{i+1}]{char.Name}: {char.HealthBar[healthbar]} [{char.Health}]  {char.ArmorBar[armorbar]} [{char.Armor}]"))
        for k in range(10):
            print("\n")
        
        for x,enemychar in enumerate(EnemyPick_Character_lst):
            if x <=5:
                Enemyhealthbar = enemychar.indexHealth()
                Enemyarmorbar = enemychar.indexArmor()
                print(Panel.fit(f"[{x+1}]{enemychar.Name}: {enemychar.HealthBar[Enemyhealthbar]} [{enemychar.Health}]  {enemychar.ArmorBar[Enemyarmorbar]} [{enemychar.Armor}]"))
        try:
            UpdateList = " ".join([f"[{i+1}]{name}" for i,name in enumerate(Pick_Character_lst)])
            print(Panel.fit(f"Hamle için karakterinizi Seçin! {UpdateList}"))
            Myindex = int(input(" ")) - 1
            if 0 <= Myindex < len(Pick_Character_lst):
                MyHero = Pick_Character_lst[Myindex]
            else:
                print("Geçerli bir sayı karakter sayısı seçiniz!")
                continue
            
            print(Panel.fit(f"Seçilen karakter için hamle seçiniz [1]Saldır [2]Savun"))
            MovePick = int(input(""))
            if MovePick == 1:
                UpdateListEnemy = " ".join([f"[{i+1}]{name}" for i,name in enumerate(EnemyPick_Character_lst)])
                print(Panel.fit(f"Saldırmak için bir rakip seçiniz {UpdateListEnemy}"))
                TargetIndex = int(input(" ")) - 1
                if 0 <= TargetIndex < len(EnemyPick_Character_lst):
                    TargetEnemy = EnemyPick_Character_lst[TargetIndex]
                    line = random.choice(MyHero.BattleCries)
                    slow_write(f"{MyHero.Name}: {line} ",style=cyan)
                    MyHero.attack(TargetEnemy)

                    if TargetEnemy.Health <= 0:
                        line1 = random.choice(MyHero.KillLines)
                        slow_write(f"{MyHero.Name}: {line1}",style=cyan)
                        time.sleep(1)
                        line2 = random.choice(TargetEnemy.DieLines)
                        slow_write(f"{TargetEnemy.Name}: {line2}",style=cyan)
                        EnemyPick_Character_lst.remove(TargetEnemy)
                        time.sleep(1)
                
                else:
                    print("Geçersiz hedef hakkınızı kaybettiniz!!")
            elif MovePick == 2:
                result = MyHero.defender()
                if result == False:
                    print("Tekrar deneyiniz")
                    time.sleep(1)
                    continue
            else:
                print("Geçersiz hamle!")
                continue
            
            time.sleep(2)
              

        except ValueError:
            print("Lütfen sadece sayı giriniz!")
        
        # Rakip Saldırısı
        print(Panel.fit("Sıra Rakipte"))
        time.sleep(1)
        EnemyHero = random.choice(EnemyPick_Character_lst)
        EnemyMovePick = random.randint(1,100)
        if EnemyMovePick <= 20:
            EnemyHero.defender()
        elif EnemyMovePick > 20:
            Enemyline = random.choice(EnemyHero.BattleCries)
            slow_write(f"{EnemyHero.Name}: {Enemyline}",style=cyan)
            EnemyTarget = random.choice(Pick_Character_lst)
            EnemyHero.attack(EnemyTarget)
            if EnemyTarget.Health <= 0:
                Enemyline1 = random.choice(EnemyHero.KillLines)
                slow_write(f"{EnemyHero.Name}: {Enemyline1}",style=cyan)
                time.sleep(1)
                Enemyline2 = random.choice(EnemyTarget.DieLines)
                slow_write(f"{EnemyTarget.Name}: {Enemyline2}")
                time.sleep(1)
                Pick_Character_lst.remove(EnemyTarget)

        time.sleep(2)
        Round += 1
    
    screen_clear()
    if len(Pick_Character_lst) > 0:
        slow_write("                         _    _  _____ _   _",0.01,style="yellow blink")
        slow_write("                        | |  | ||  _  | \ | |",0.01,style="yellow blink")
        slow_write("                        | |  | || | | |  \| |",0.01,style="yellow blink")
        slow_write("                        | |/\| || | | | . ` |",0.01,style="yellow blink")
        slow_write("                        \  /\  /\ \_/ / |\  |",0.01,style="yellow blink")
        slow_write("                         \/  \/  \___/\_| \_/",0.01,style="yellow blink")
        time.sleep(3)
        print("Ana menüye dönülüyor")
        time.sleep(1)
        loginScreen()
    
    elif len(Pick_Character_lst) <= 0:
        slow_write("                         _     _____ _____ _____ ",0.01,style="bold red blink")
        slow_write("                        | |   |  _  /  ___|  ___|",0.01,style="bold red blink")
        slow_write("                        | |   | | | \ `--.| |__  ",0.01,style="bold red blink")
        slow_write("                        | |   | | | |`--. \  __|",0.01,style="bold red blink")
        slow_write("                        | |___\ \_/ /\__/ / |___ ",0.01,style="bold red blink")
        slow_write("                        \_____/\___/\____/\____/ ",0.01,style="bold red blink")
        time.sleep(3)
        print("Ana menüye dönülüyor")
        time.sleep(1)
        loginScreen()

game_intro()