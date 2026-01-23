#  //==========================================================================\\
# ((----------------------------------Libraries---------------------------------))
#  \\==========================================================================//

import random
import time 
import os
import sys
from rich.console import Console

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

#  //==========================================================================\\
# ((------------------------------------OOP-------------------------------------))
#  \\==========================================================================//    
# ||-----Name/Power/Health/Repetitive/DefenderHealth/BattleCry/HealthBar------||
class Character():
    def __init__(self,name,power,health,attack_repetitive,defender_health,battle_cries,health_bar):
        self.Name = name
        self.Power = power
        self.Health = health
        self.MaxHealth = health
        self.Repetitive = attack_repetitive
        self.BattleCries = battle_cries
        self.HealthBar = health_bar
        self.DefenderHealth = defender_health
    
    def index(self):
        if self.Health >= self.MaxHealth:
            return 0
        if self.Health <= 0:
            return 10 
        ratio = self.Health / self.MaxHealth
        reverse_x = int(10 * ratio)
        x = 10 - reverse_x
        return x

    def defender(self):
        if self.Health <= 0: 
            return 
        if self.Health < self.MaxHealth:
            self.Health += self.DefenderHealth
            if self.Health > self.MaxHealth:
                self.Health = self.MaxHealth
                slow_write(f"{self.Name}: +{self.DefenderHealth} Canı Fullendi! {self.HealthBar[self.index()]}",0.02,style="bold green")
            else:
                slow_write(f"{self.Name}: +{self.DefenderHealth} Can aldı {self.HealthBar[self.index()]} ")
        else:
            slow_write(f"{self.Name}: Canı ful {self.HealthBar[0]}",0.02,style="bold green")
        
    
    def attack(self,enemy):  
        for i in range(self.Repetitive):            
            if enemy.Health <= 0:
                slow_write(f"{enemy.Name} Öldü {enemy.HealthBar[10]}",0.02,style="bold red")     
                return                                                                           
            else:
                enemy.Health -= self.Power
                BattleCry = random.choice(self.BattleCries)
                slow_write(f"{self.Name}: {BattleCry}  {self.Name} ⚔️ {enemy.Name}",0.02)

class King(Character):
    def __init__(self,name,health,special_power,battle_cries,health_bar):
        super().__init__(name,0,health,0,0,battle_cries,health_bar)     # buf debuff kesinlikle gelmeli!!!!!!!!!!!
        self.SpecialPower = special_power

    def buff(self):
        print(f"{self.Name} Kızdı 🔱 {self.SpecialPower} Gücünü aktif ediyor!!!")
        time.sleep(2)
        print("İşler Karıştı!!!")
        

#  //========================================================================================\\
# ||---------------------------------------Characters-----------------------------------------||        
# ||---Name/Power/Health/Repetitive/DefenderHealth/BattleCry/Kill_lines/Die_lines/HealthBar---||      
# \\=========================================================================================//

gladyator0 = Character("Alonzo",50,200,1,20,[
    "Kılıcım gücünü halkımdan alır",
    "Atımın altında ezileceksin!!",
    "Korkma belki devlet affeder"
],
[
    "Kılıcım Tadı güzel miydi?!",
    "Yerin zaten orasıydı",
    "Devlet seni affetmedi"
],
[
    "Devletim uğruna...",
    "Kı-lıcı-m...",
    "Devlet en iyisini bilir"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
gladyator1 = Character("Erok",20,200,1,20,[
    "Sen ben hadi savaş",
    "Hrrr...",
    "Kılıç ve kan"
],
[
    "Öldü",
    "HAAAAAAAAAAAAAARRRRRRR",
    "Kanının tadı b*k gibi",
],
[
    "Uyumak istemiyorum...",
    "Öldüm mü?",
    "Öğk-öhk..."
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
gladyator2 = Character("Proxgaint",30,250,1,25,[
    "Baltam en son babamı kestiğinde bu kadar mutluydu",
    "Bir balta iki balta aaa balta kafanda",
    "Balta balta batalarrrr"
],
[
    "Baltam keskindir demiştim",
    "Babamı kestikten sonrada böyle olmuştu",
    "Sanırım öldün ha?!"    
],
[
    "Beni bekle baba geliyorum",
    "Bal-ba-balt...",
    "Beni iyi hakladın"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
gladyator3 = Character("Rockby",1,1000,5,100,[
    "SELAM KAYA GİBİ",
    "Taş taşa demiş biz taşız",
    "Al bu kayayı başına çal"
],
[
    "Genelde kimseyi öldürmem"
],
[
    "Yüce dağlar görevim bitti",
    "Dağ gibi adam devrildi...",
    "Yıkıldım..."
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
gladyator4 = Character("Man",25,100,4,10,[
    "Ne çirkinsin ölmek sana mübah",
    "Seni öldürmek için can atıyorum",
    "Kellen için geliyorumm"
],
[
    "Ölünce daha da çirkin oldun",
    "Seni öldürmek içi can atıyordum ama öldürdükten sonra zevk almadım",
    "Kellen beş para etmezmiş"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])

wizard0 = Character("Gloria",100,50,2,20,[
    "Selam birazdan her yer alev alıcak",
    "Güzeliğim alevlerimin yanında bir hiç",
    "Seni sevmedim YAN!"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
wizard1 = Character("Adam",50,100,2,25,[
    "Soğuk soğuk soğuk  pffff",
    "Seni buzdan heykele dönüştürücem",
    "Donmak için can atıyorum"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
wizard2 = Character("Kun",20,250,5,30,[
    "Toprağın üstünde güvende değilsin",
    "Kafanı toprağa gömücem",
    "Ordaki dağları ben yarattım"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
wizard3 = Character("Samuel",50,200,1,20,[
    "Seni Boğucam",
    "Yüzme biliyo musun? umarım bilmiyosundur",
    "Yağmurdan korkmalısın"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])

archer0 = Character("Emrey",20,250,6,25,[
    "Odak kafada",
    "Sevgilim için GELİYORUM",
    "Bonjour"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
archer1 = Character("Ahu",25,100,4,100,[
    "Oklarım kusursuzdur ama sen onlara layık değilsin",
    "Seni öldürmek için yay kulanmama gerek yok",
    "Zaten ölüsün"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
archer2 = Character("Elegante",10,100,10,25,[
        "Hey hey gördün mü tam kafadan",
        "Kral mı aynı senin gibi ölmeli",
        "Benim adım Elegante senin ise ölü"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
archer3 = Character("Eriksen",40,150,4,30,[
    "Sanırım savaşıcaz",
    "Biliyor musun al şu oku ve kendini öldür",
    "Yapmasak zaten ölüceksin"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])

#  //==========================================================================\\
#  ||----------------------------------Kins------------------------------------||
#  ||----------------------KingName/Healeth/SpecialPower-----------------------||
#  \\==========================================================================//

king0 = King("Mr. Salvo",10000,"empty",[
    "Cehennem'den bir parça",
    "Yaklaşan ölüm",
    "Kokusu burnumda"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
king1 = King("Kin",10000,"empty",[
    "Devletine bağlı askerlerin her zaman kazandığı bir savaş",
    "Kazanmak için tek çare SAVAŞ",
    "AYAKLANIN ASKERLİM"
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])
king2 = King("T.U.R.X",9999,"empty",[
    "JD2&%^'ASF^FFS'^H4)",
    "EF3.5622'FASF++&S&ASF&^+!'",
    "..."
],
[
    "[██████████] 100/100",
    "[█████████░] 90/100",
    "[████████░░] 80/100",
    "[███████░░░] 70/100",
    "[██████░░░░] 60/100",
    "[█████░░░░░] 50/100",
    "[████░░░░░░] 40/100",
    "[███░░░░░░░] 30/100",
    "[██░░░░░░░░] 20/100",
    "[█░░░░░░░░░] 10/100",
    "💀[░░░░░░░░░░] 0/100"

])

#  //==========================================================================\\
# ((---------------------------Defender/Attack-lines----------------------------))
#  \\==========================================================================//

defender_lines = [
    "Herkesin biraz dinlenmeye ihtiyacı vardır",
    "Şimdi defans zamanı!!!",
    "Takım güç topluyor"
    ]

attack_lines = [
    "Şimdi saldırı vakti!!!",
    "Saldırmak için koşuyorlar",
    "ŞUNLARA BAK! öldürmek için geliyorlar"
]












archer0.attack(gladyator0)
gladyator0.defender()



