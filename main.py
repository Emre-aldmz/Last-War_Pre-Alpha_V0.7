#  //==========================================================================\\
# ((----------------------------------Libraries---------------------------------))
#  \\==========================================================================//

import random
import time 

#  //==========================================================================\\
# ((--------------------------------Interface-----------------------------------))
#  \\==========================================================================//

Character_pool = {                                                  
    "Gladyator" : ["Alonzo","Erok","Proxgaint","Rockby"],
    "Wizard" : ["Gloria","Adam","Kun","Samuel"],                             # Statları eklenecek v1.3
    "Archer" : ["Emrey","Ahu","Elegante","Eriksen"],
    "King" : ["Mr. Salvo","Kin","T.U.R.X"]
}

Pick_Character_lst = []
Character_lst = ["Gladyator","Wizard","Archer","King"]



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
            print(f"Mevcut karakterler: {character_now}")                          # çünkü character_number 0 dan başlıyor 1 den +1 ine kadar
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
print(EnemyPick_Character_lst)



#  //==========================================================================\\
# ((------------------------------------OOP-------------------------------------))
#  \\==========================================================================//    

class Character():
    def __init__(self,name,power,health,attack_repetitive,battle_cries):
        self.Name = name
        self.Power = power
        self.Health = health
        self.Repetitive = attack_repetitive
        self.BattleCries = battle_cries
    def defender(self):
        defender_line = random.choice(defender_lines)
        print(f"Defans yapıldı: {defender_line}")  # burdayız
    def attack(self,enemy):
        toplam = 0
        for i in range(self.Repetitive):
            attack_line = random.choice(attack_lines)
            print("Atak yapıldı: {ata}")
            RandomBattleCries = random.choice(self.BattleCries)
            print(f"{self.Name}: {RandomBattleCries}")
            time.sleep(2)
            print(f"{self.Name} {self.Power} Gücünde {i+1}.atağını yapıyor")
            enemy.Health -= self.Power
            time.sleep(2)
            print(f"{enemy.Name} in {enemy.Health} canı kaldı")
            toplam += self.Power
            time.sleep(2)
        
        print(f"{enemy.Name} Toplam:{toplam} Gücünden darbe aldı!! {enemy.Health} Canı kaldı ")

class King(Character):
    def __init__(self,name,health,special_power,battle_cries):
        super().__init__(name,0,health,0,battle_cries)
        self.SpecialPower = special_power

    def buff(self):
        print(f"{self.Name} Kızdı 🔱 {self.SpecialPower} Gücünü aktif ediyor!!!")
        time.sleep(2)
        print("İşler Karıştı!!!")
        

#  //=========================================================================\\
# ||-------------------------------Characters---------------------------------||
# ||-----------------------Name/Power/Healeth/Repetitive----------------------||
# \\==========================================================================//

gladyator0 = Character("Alonzo",50,200,1,[
    "Kılıcım gücünü halkımdan alır",
    "Atımın altında ezileceksin!!",
    "Korkma belki devlet affeder"
])
gladyator1 = Character("Erok",20,200,1,[
    "Sen ben hadi savaş",
    "Hrrr...",
    "Kılıç ve kan"
])
gladyator2 = Character("Proxgaint",30,250,1,[
    "Baltam en son babamı kestiğinde bu kadar mutluydu",
    "Bir balta iki balta aaa balta kafanda",
    "Balta balta batalarrrr"
])
gladyator3 = Character("Rockby",1,1000,5,[
    "SELAM KAYA GİBİ",
    "Taş taşa demiş biz taşız",
    "Al bu kayayı başına çal"
])
gladyator4 = Character("Man",25,100,4,[
    "Ne çirkinsin ölmek sana mübah",
    "Seni öldürmek için can atıyorum",
    "Kellen için geliyorumm"
])

wizard0 = Character("Gloria",100,50,2,[
    "Selam birazdan her yer alev alıcak",
    "Güzeliğim alevlerimin yanında bir hiç",
    "Seni sevmedim YAN!"
])
wizard1 = Character("Adam",50,100,2,[
    "Soğuk soğuk soğuk  pffff",
    "Seni buzdan heykele dönüştürücem",
    "Donmak için can atıyorum"
])
wizard2 = Character("Kun",20,250,5,[
    "Toprağın üstünde güvende değilsin",
    "Kafanı toprağa gömücem",
    "Ordaki dağları ben yarattım"
])
wizard3 = Character("Samuel",50,200,1,[
    "Seni Boğucam",
    "Yüzme biliyo musun? umarım bilmiyosundur",
    "Yağmurdan korkmalısın"
])

archer0 = Character("Emrey",20,250,6,[
    "Odak kafada",
    "Sevgilim için GELİYORUM",
    "Bonjour"
])
archer1 = Character("Ahu",25,100,4,[
    "Oklarım kusursuzdur ama sen onlara layık değilsin",
    "Seni öldürmek için yay kulanmama gerek yok",
    "Zaten ölüsün"
])
archer2 = Character("Elegante",10,100,10,[
        "Hey hey gördün mü tam kafadan",
        "Kral mı aynı senin gibi ölmeli",
        "Benim adım Elegante senin ise ölü"
])
archer3 = Character("Eriksen",40,150,4,[
    "Sanırım savaşıcaz",
    "Biliyor musun al şu oku ve kendini öldür",
    "Yapmasak zaten ölüceksin"
])

#  //==========================================================================\\
#  ||----------------------------------Kins------------------------------------||
#  ||----------------------KingName/Healeth/SpecialPower-----------------------||
#  \\==========================================================================//

king0 = King("Mr. Salvo",10000,"empty",[
    "Cehennem'den bir parça",
    "Yaklaşan ölüm",
    "Kokusu burnumda"
])
king1 = King("Kin",10000,"empty",[
    "Devletine bağlı askerlerin her zaman kazandığı bir savaş",
    "Kazanmak için tek çare SAVAŞ",
    "AYAKLANIN ASKERLİM"
])
king2 = King("T.U.R.X",9999,"empty",[
    "JD2&%^'ASF^FFS'^H4)",
    "EF3.5622'FASF++&S&ASF&^+!'",
    "..."
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












# gladyator2.attack(gladyator3)




