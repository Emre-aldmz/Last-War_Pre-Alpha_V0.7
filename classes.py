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
# ((------------------------------------OOP-------------------------------------))
#  \\==========================================================================//    

class Character():
    def __init__(self,name,power,health,attack_repetitive,defender_health,critical_hit,battle_cries,kill_lines,die_lines,health_bar,armor_bar,armor):
        self.Name = name
        self.Power = power
        self.Health = health
        self.MaxHealth = health       
        self.Repetitive = attack_repetitive
        self.DefenderHealth = defender_health
        self.CriticalHit = critical_hit
        self.BattleCries = battle_cries
        self.KillLines = kill_lines
        self.DieLines = die_lines
        self.HealthBar = health_bar
        self.ArmorBar = armor_bar
        self.MaxArmor = 100
        self.Armor = 100                
    
    def indexHealth(self):
        if self.Health >= self.MaxHealth:
            return 0
        if self.Health <= 0:
            return 10 
        ratio = self.Health / self.MaxHealth
        reverse_x = int(10 * ratio)
        x = 10 - reverse_x
        return x
    
    def indexArmor(self):
        if self.Armor >= self.MaxArmor:
            return 0
        if self.Armor <=0:
            return 10
        ratio1 = self.Armor / self.MaxArmor
        reverse_y = int(10 * ratio1)
        y = 10 - reverse_y
        return y
        
    def defender(self):
        if self.Health < self.MaxHealth:
            self.Health = min(self.Health+self.DefenderHealth, self.MaxHealth)
            barindex = self.indexHealth()
            print(f"{self.Name}: Defans yapıyor. Can basıldı! Can:[{self.Health}]/{self.HealthBar[barindex]}")
            time.sleep(1.5)
            return True # Main e bilgi gönderiyoruz
        else:
            print(f"{self.Name}: Canı zaten ful❤️")
            time.sleep(1)
            return False # False ise BattleScreen() continue ile while döngüsünün başına dönücek
            
    def attack(self,enemy):
        if enemy.Armor > 0:
            possibility = random.randint(1,100)
            if possibility < self.CriticalHit:
                enemy.Armor -= self.Power*2
                if enemy.Armor <= 0:
                    enemy.Armor = 0
                    print(f"{self.Name}: 💥💥Kritik Vuruş💥💥 Saldırıyor ==> {enemy.Name}")
                    time.sleep(1)
                    print(f"{enemy.Name}: Zırhı Krıldı💥")
                    time.sleep(1.5)
                else:  
                    print(f"{self.Name}: 💥💥Kritik Vuruş💥💥 Saldırıyor ==> {enemy.Name}")
                    time.sleep(1)
                    barindex = enemy.indexArmor()
                    print(f"{enemy.Name}: Kalan Kalkanı🛡️ ==> [{enemy.Armor}]/{enemy.ArmorBar[barindex]}")
                    time.sleep(1.5)
            else:
                enemy.Armor -= self.Power
                if enemy.Armor <= 0:
                    enemy.Armor = 0
                    print(f"{self.Name}: Saldırıyor⚔️ ==> {enemy.Name}")
                    time.sleep(1.5) 
                    print(f"{enemy.Name}: Zırh Kırıldı💥")
                    time.sleep(1.5)
                else:  
                    print(f"{self.Name}: Saldırıyor⚔️ ==> {enemy.Name}")
                    time.sleep(1.5)
                    barindex = enemy.indexArmor()
                    print(f"{enemy.Name}: Kalan Kalkanı🛡️ ==> [{enemy.Armor}]/{enemy.ArmorBar[barindex]}")
                    time.sleep(1.5)                
        else:
            possibility = random.randint(1,100)
            if possibility < self.CriticalHit:
                enemy.Health -= self.Power*2
                if enemy.Health <= 0:
                    enemy.Health = 0
                    print(f"{self.Name}: 💥💥Kritik Vuruş💥💥 Saldırıyor ==> {enemy.Name}")
                    time.sleep(1.5)
                    print(f"{enemy.Name}: Öldü💀")
                    time.sleep(1.5)
                else:
                    print(f"{self.Name}: 💥💥Kritik Vuruş💥💥 Saldırıyor ==> {enemy.Name}")
                    time.sleep(1.5)
                    barindex = enemy.indexHealth()
                    print(f"{enemy.Name}: Kalan Can❤️ ==> [{enemy.Health}]/{enemy.HealthBar[barindex]}")
                    time.sleep(1.5)
            else:
                enemy.Health -= self.Power  
                if enemy.Health <= 0:
                    enemy.Health = 0
                    print(f"{self.Name}: Saldırıyor⚔️ ==> {enemy.Name}")
                    time.sleep(1.5)
                    print(f"{enemy.Name}: Öldü💀")
                    time.sleep(1.5)
                else:
                    print(f"{self.Name}: Saldırıyor⚔️ ==> {enemy.Name}")
                    time.sleep(1.5)
                    barindex = enemy.indexHealth()
                    print(f"{enemy.Name}: Kalan Can❤️ ==> [{enemy.Health}]/{enemy.HealthBar[barindex]}")
                    time.sleep(1.5)

    def __repr__(self): # Önemli bir fonksiyon (İsimlerin alınıp kullanılmasını sağlıyor)
        return self.Name
            
class King(Character): # Krallar ve özellikleri daha eklenmedi
    def __init__(self,name,health,special_power,battle_cries,health_bar,armor_bar):
        super().__init__(name,0,health,0,0,0,battle_cries,0,0,health_bar,armor_bar,0)     
        self.SpecialPower = special_power

    def buff(self,self_military):
        if kingResult == "Kanlı İmza": 
            self.self_military += int(self.Health*(5/100))
            self.Health -= int(self.Health*(5/100))
            slow_write(f"{self.Name}: Kanlı imzayı attı. Tüm takım + can kazandı!",0.02,style=green)
        if kingResult == "Sıkıyönetim":
            print(" ")