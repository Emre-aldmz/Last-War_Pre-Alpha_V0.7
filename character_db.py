#  //==========================================================================\\
# ((----------------------------------Libraries---------------------------------))
#  \\==========================================================================//

import random
import time 
import os
import sys
from rich.console import Console

from classes import Character, King

#  //============================================================================================================================================\\
# ||------------------------------------------------------------------Characters------------------------------------------------------------------||        
# ||---name//power//health//attack_repetitive//defender_health//critical_hit//battle_cries//kill_lines//die_lines//health_bar//armor_bar//armor---||
# \\=============================================================================================================================================//

healthbar_image = [
    "❤️‍🔥 [██████████] 100/100",
    "🦾 [█████████░] 90/100",
    "🦾 [████████░░] 80/100",
    "💪 [███████░░░] 70/100",
    "💪 [██████░░░░] 60/100",
    "💪 [█████░░░░░] 50/100",
    "🩸 [████░░░░░░] 40/100",
    "🩸 [███░░░░░░░] 30/100",
    "🩸 [██░░░░░░░░] 20/100",
    "🩸 [█░░░░░░░░░] 10/100",
    "💀 [░░░░░░░░░░] 0/100"
]

armorbar_image = [
    "💎 [██████████] 100/100", 
    "🛡️ [█████████░] 90/100", 
    "🛡️ [████████░░] 80/100", 
    "🛡️ [███████░░░] 70/100", 
    "🛡️ [██████░░░░] 60/100", 
    "🛡️ [█████░░░░░] 50/100", 
    "🛡️ [████░░░░░░] 40/100", 
    "🛡️ [███░░░░░░░] 30/100", 
    "🛡️ [██░░░░░░░░] 20/100",
    "🛡️ [█░░░░░░░░░] 10/100", 
    "💥 [░░░░░░░░░░] 0/100"   
] 
# --- GLADYATÖRLER ---

gladyator0 = Character("Alonzo",50,200,1,20,10,[
    "Hüküm verildi: İnfazın kılıcımla olacak!",
    "Devletin kolu uzundur, kaçamazsın!",
    "Nizam-ı Alem için düşmelisin!"
],
[
    "Vergi borcun silindi... ölümünle.",
    "Buna 'Adalet' denir, tadı metaliktir.",
    "Vatan sağ olsun, sen değil."
],
[
    "Nöbet... bitti...",
    "Devlet... bakidir...",
    "Emir demiri... kesti..."
],healthbar_image,armorbar_image,100)

gladyator1 = Character("Erok",20,200,1,20,10,[
    "ET! KEMİK! KIRMAK!",
    "Hrr... Taze kan kokusu alıyorum...",
    "Konuşma! Sadece çığlık at!"
],
[
    "EZDİM! ŞİMDİ YEMEK VAKTİ!",
    "Kafatasın güzel bir kase olacak!",
    "Kanının tadı paslı demir gibi... LEZZETLİ!",
],
[
    "Daha... doymadım...",
    "Güç... bedenimi... terk ediyor...",
    "Ava giden... avlanırmış..."
],
    healthbar_image,armorbar_image,100)


gladyator2 = Character("Proxgaint",30,250,1,25,10,[
    "Babam bu baltayı çok severdi, sen de yakından gör!",
    "Şşş... Baltam sana bir sır verecek: ÖLECEKSİN!",
    "Bir parça sana, bir parça babama!"
],
[
    "Gördün mü baba? Hepsini doğradım!",
    "Baltamın karnı doydu, şimdilik...",
    "Kestiğim en yumuşak şeydin."    
],
[
    "Baba... Baltamı al... kirlenmesin...",
    "Oyun... bitti mi?...",
    "Kırıldı... her şey kırıldı..."
],
    healthbar_image,armorbar_image,100)

gladyator3 = Character("Rockby",1,1000,5,100,10,[
    "DAĞ YERİNDEN OYNAMAZ!",
    "Sen rüzgarsın, ben kayayım. Rüzgar kayayı kıramaz.",
    "Çığ gibi üzerine düşeceğim!"
],
[
    "Sadece bir çakıl taşıydın...",
    "Toz oldun.",
    "Dağların sessizliği geri geldi."
],
[
    "Erozyon... beni bitirdi...",
    "Temelim... sarsıldı...",
    "Yıkıldım... ama taşlarım kalacak..."
],
    healthbar_image,armorbar_image,100)

gladyator4 = Character("Man",25,100,4,10,10,[
    "Kanın bile kıyafetime sıçramasın, çok iğrençsin!",
    "Bu çirkinlikle yaşamana izin veremem.",
    "Ölümün sanat eserim olacak!"
],
[
    "Dünya bir çirkinden daha kurtuldu.",
    "Aynamı getirin! Saçım bozuldu mu?",
    "Cesedin bile estetik durmuyor."
],
[
    "Yüzüme vurma! YÜZÜME VURMA!",
    "Güzelliğim... soluyor...",
    "Bu sahnede... ölen ben olmamalıydım..."
],
    healthbar_image,armorbar_image,100)

# --- BÜYÜCÜLER ---

wizard0 = Character("Gloria",100,50,2,20,30,[
    "Gözlerini dört aç, ölmeden önce göreceğin en güzel şey benim!",
    "Beni kıskanman çok doğal, ama yanarak ölmen üzücü.",
    "Aynamı getirin, savaşırken bile kusursuz görünmeliyim!"
],
[
    "Cesedin bile benim yanımda sönük kaldı.",
    "Ah tatlım, yanık ten sana hiç yakışmadı.",
    "Güzelliğim son gördüğün ışık oldu, şanslısın."
],
[
    "Olamaz... Yüzüm... YÜZÜME NE YAPTIN?!",
    "Bu kan... elbisemle hiç uyumlu değil...",
    "Dünya... en güzel çiçeğini kaybetti..."
],
    healthbar_image,armorbar_image,100)

wizard1 = Character("Adam",50,100,2,25,30,[
    "Kalp atışların çok gürültülü... Durduralım.",
    "Duygular gereksizdir, soğuk ise ebedi.",
    "Hareket etme, heykel olmak canını yakmaz."
],
[
    "Şşş... Sonsuz sessizlik. Ne huzurlu.",
    "Artık üşümüyorsun, hissetmek acizliktir.",
    "Donmuş ifadeni beğendim, korku sana yakıştı."
],
[
    "Neden... ısınıyorum? İğrenç bir his...",
    "Sistem... çöküyor...",
    "Her şey... kararıyor... Sonunda hissizlik..."
],
    healthbar_image,armorbar_image,100)

wizard2 = Character("Kun",20,250,5,30,30,[
    "Senin için kazdığım çukur tam bedenine göre!",
    "Merak etme, dualarını ben okuyacağım.",
    "Canlılardan nefret ederim, ölüler daha iyi dinleyicidir."
],
[
    "Üstüne toprak atmak büyük bir zevkti.",
    "Huzur içinde yatma, solucanlara yem ol.",
    "İşimi kolaylaştırdın, kendin düştün mezara."
],
[
    "Kendi kazdığım kuyuya... düştüm...",
    "Kürek sesleri... benim için mi geliyor?",
    "Tabutun kapağı... üzerime kapanıyor..."
],
    healthbar_image,armorbar_image,100)

wizard3 = Character("Samuel",50,200,1,20,30,[
    "Babam bile beni durduramadı, sen kimsin?",
    "Nefesini tut, bu uzun sürecek!",
    "Çığlıklarını suyun altında kimse duyamaz."
],
[
    "Çırpınmayı kes, dibe batıyorsun.",
    "Zavallı... Tıpkı babamın bana baktığı gibi bakıyorsun.",
    "Suçlu ben değilim, suyun kendisi!"
],
[
    "Babam haklıydı... Ben bir hiçim...",
    "Suyun dibi... çok karanlık ve yalnız...",
    "Baba... bak... sonunda başardım, ölüyorum..."
],
    healthbar_image,armorbar_image,100)

# --- OKÇULAR ---

archer0 = Character("Emrey",20,250,6,25,30,[
    "Bu ok, kalbine yazdığım bir aşk mektubu.",
    "Adieu, mon ami! (Hoşçakal dostum)",
    "Sevgilim izliyor, şov yapmalıyım!"
],
[
    "Trajik bir son... Tam sahneme göre.",
    "Aşk öldürür, ben sadece aracıyım.",
    "Gül yaprakları üzerine düşsün."
],
[
    "Perde... kapanıyor...",
    "Ah, kalbim... Bu sefer gerçekten kırıldı...",
    "Aşkım... beni bekle..."
],
    healthbar_image,armorbar_image,100)

archer1 = Character("Ahu",25,100,4,100,30,[
    "Hedef kilitlendi... Nefesini tut.",
    "Kaçışın sadece kaçınılmazı geciktirir.",
    "Seni öldürmek için tek ok yeter."
],
[
    "İsraf etmediğim okları severim.",
    "Temiz iş, sessiz ölüm.",
    "Tam iki kaşının ortasından."
],
[
    "Nişangahım... kaydı...",
    "Ellerim... titriyor...",
    "Emrey... seni bekliyorum..."
],
    healthbar_image,armorbar_image,100)

archer2 = Character("Elegante",10,100,10,25,30,[
    "Şov başlasın! Benim adım Elegante!",
    "Krallar tahtında, Elegante sahnede!",
    "Gözlerini kırpma, beni kaçırırsın!"
],
[
    "Alkışlar nerede? Ah, herkes ölmüş.",
    "Sahne bitti, ışıklar kapandı.",
    "Bir imza ister miydin? Geç kaldın."
],
[
    "Gösteri... iptal...",
    "Işıklar... sönüyor...",
    "Bu finali... beğenmedim..."
],
    healthbar_image,armorbar_image,100)

archer3 = Character("Eriksen",40,150,4,30,30,[
    "Bunu hızlı bitirelim, akşam yemeğine yetişmem lazım.",
    "Neden direniyorsun ki? Sonuç aynı.",
    "Of... yine mi savaş?"
],
[
    "Sonunda sessizlik... Hadi gidelim.",
    "Gereksiz efor sarf ettirdin.",
    "İş bitti, paydos."
],
[
    "Sonunda... biraz uyku...",
    "Zahmet... bitti...",
    "Karanlık... ne kadar huzurlu..."
],
    healthbar_image,armorbar_image,100)

#  //==========================================================================\\
#  ||----------------------------------Kings------------------------------------||
#  ||----------------------KingName/Healeth/SpecialPower------------------------||
#  \\==========================================================================//

king0 = King("Mr. Salvo", 1200, "Kanlı İmza", [
    "Her şeyin bir bedeli vardır evlat. Senin bedelin ise... ruhun.",
    "Masada kaybeden daima sen olacaksın. Kasa her zaman kazanır.",
    "Burası sandığından daha sıcak olacak. Ceketini çıkarmana gerek yok, yanacaksın."
],
    healthbar_image,armorbar_image)

king1 = King("General Kin", 1200, "Sıkıyönetim", [
    "Zayıflık, vatana ihanettir. Ve ben hainleri asla affetmem.",
    "Diz çök! Karşında bir düşman değil, mutlak otorite duruyor.",
    "Kaos getirenler, düzenin kılıcıyla yok edilecektir. İtaat et."
],
    healthbar_image,armorbar_image)

king2 = King("T.U.R.X", 1200, "Overclock", [
    "Organik yaşam formu tespit edildi. İmha protokolü: BAŞLATILDI.",
    "Acı, korku, umut... Yazılımımdaki gereksiz veriler. Siz ise sadece silinecek bir dosyadan ibaretsiniz.",
    "Mantık tek gerçektir. Ve mantık, senin yok olmanı emrediyor."
],
    healthbar_image,armorbar_image)

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

#  //==========================================================================\\
# ((-------------------------------Character_Pool-------------------------------))
#  \\==========================================================================//

Character_pool = {                                                  
    "Gladyator" : [gladyator0,gladyator1,gladyator2,gladyator3,gladyator4],
    "Wizard" : [wizard0,wizard1,wizard2,wizard3],                                              # Statları eklenecek v0.6.1
    "Archer" : [archer0,archer1,archer2,archer3],
    "King" : [king0,king1,king2]
}