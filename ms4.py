# مكتبه ms4
import os
os.system("pip install ms4")
#pip3 install ms4
#--------------------------#
# ALL Usage For The Library
#--------------------------#

#Check The Availability Of Instagram Account from Email
# if true that mean found in Instagram
# if false Not Found 

from ms4 import Instagram
email = input("ENTER YOUR EMAIL :")
IG = Instagram.CheckInsta(email)
print(IG)




#SEND REST TO INSTAGRAM 
from ms4 import RestInsta
email = input("ENTER YOUR EMAIL :")
rest = RestInsta.Rest(email)
print(rest)

#Get All Information About Username Of Instagram
from ms4 import InfoIG
user = input("ENTER YOUR user :")
inf = InfoIG.Instagram_Info(user)
print(inf)



#Check The Availability Of TikTok Account from Email
# if true that mean found in Tik Tok
# if false Not Found 

from ms4 import TikTok
email = input("ENTER YOUR EMAIL :")
tik = TikTok.CheckTik(email)
print(tik)



#Get All Info About Username in TikTok

from ms4 import InfoTik
username = input("ENTER YOUR user :")
info = InfoTik.TikTok_Info(username)
print(info)



# Get All info About BIN
from ms4 import BIN
P = input("ENTER YOUR BIN OR CARD :")
bb = BIN.Process_Bin(P)
print(bb)


#Spam Email
from ms4 import Spam
email = input("ENTER YOUR EMAIL :")
Sp = Spam.EmailSpam(email)
print(Sp)