#  //==========================================================================\\
# ((----------------------------------Libraries---------------------------------))
#  \\==========================================================================//

import random
import time 
import os
import sys
from rich.console import Console

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
        

    def defender(self):
        print(" ")
        
        
    
    def attack(self,enemy):  
        print(" ")
        
class King(Character):
    def __init__(self,name,health,special_power,battle_cries,health_bar):
        super().__init__(name,0,health,0,0,0,battle_cries,0,0,health_bar,0,0)     
        self.SpecialPower = special_power

    def buff(self,self_military):
        if kingResult == "Kanlı İmza": 
            self.self_military += int(self.Health*(5/100))
            self.Health -= int(self.Health*(5/100))
            slow_write(f"{self.Name}: Kanlı imzayı attı. Tüm takım + can kazandı!",0.02,style=green)
        if kingResult == "Sıkıyönetim":
            print(" ")