import requests
import sys
import os

os.system('clear')

print ('▉▉▉   ▉▉▉  ▉   ▉  ▉  ▉▉▌')
print ('▉┆┆   ▉┆▉   ▉ ▉   ▉  ▉  ▌')
print ('▉▉▉   ▉▉▉    ▉    ▉  ▉▉▌ ●[]●<based login>')
print ('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
print ('PRHATIAN . TIDAK SEMUA PHISING BISA DI SPAM MENGGUNAKAN TOOL INI')
print ('____________________________')
print ('INFO LEBIH LANJUT KUNJUNGI AKUN CHANNEL')
print ('________________________________')
print ('________________________________')
print ('YOUTUBE   :  ANT CYBER SULBAR')
print ('____________________________')
print ('FACEBOOK  :  KHAN AMIR      ')
print ('____________________________')
print ('                            ')
print ('                            ')
print ('                            ')

amirkan = input('LINK/URL TARGET   : ')

nay = input('DATA EMAIL        : ')
naisa = input('DATA PASSWORD     : ')

def login(id,pw):
   data = {nay:id, naisa:pw,}
   r = requests.post(amirkan,data=data)
   if '!.ph.l?' in r.url:
       print (f'[×] error = {pw} ')
       sys.exit()
   else:
       print (f'[∆] berhasil = {pw} ')
       login(id,pw)

if __name__=='__main__':
   id = input('USER              : ')
   pw = input('PASSWORD          : ')
   login(id,pw)
