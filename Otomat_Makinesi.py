products=["Kola","Fanta","Bisküvi","Çikolata"] # index:0,1,2,3
prices=[8.5,8.5,4,3.5]
username="admin"
password="123"
right_of_Entry = 3
keep_up = None
secim = None

while secim != "Q" and keep_up != "2":
    secim=input("1-Admin\n2-Müşteri\nQ-Çıkış\n\tSeçim:").upper()
    if secim == "Q":break
    elif secim == "1":
        user_panel_username = input("Username:")
        user_panel_password = input("Password:")
        if right_of_Entry == 1:
            print("Kullanıcı adı veya şifre hatalı")
            print("Giriş hakkı bitti")
            break
        elif user_panel_username == username and user_panel_password == password:
            print("Giriş Başarılı\n")
            while keep_up != "2":
                desired_action = input("Yapılmak istenen işlem\n1-Ürün ekleme\t2-Ürün çıkarma\t3-Profil değişikliği\t4-Liste görüntüle\tQ-Çıkış\n\tSeçim:").upper()
                if desired_action == "Q":
                    secim = "Q"
                    break
                elif desired_action == "1":
                    while keep_up != "2":
                        new_product_name = input("Ürün adı:")
                        new_prices = float(input("Ürün Fiyatı:"))

                        products.append(new_product_name)
                        prices.append(new_prices)

                        while True:
                            keep_up = input("Başka bir ürün eklemek istiyor musunuz? (1-Evet\t2-Hayır)\n\tSeçim:")
                            if keep_up == "1":
                                break
                            elif keep_up == "2":
                                print(products)
                                print(prices)
                                break
                            else:
                                print("Kodlama hatası")
                                continue
                elif desired_action == "2":
                    count = 0
                    for urun in products:
                        print(f"{count}-{urun}")
                        count += 1
                    index_remove = int(input("Silinmek istenen ürünün numarası:"))
                    products.pop(index_remove)
                    prices.pop(index_remove)
                    print(urun,"ürünü listeden kaldırıldı.")
                    while True:
                        keep_up = input("Başka bir ürün kaldırmak istiyor musunuz? (1-Evet\t2-Hayır)\n\tSeçim:")
                        if keep_up == "1":
                            break
                        elif keep_up == "2":
                            print(products)
                            print(prices)
                            break
                        else:
                            print("Kodlama hatası")
                            continue

                elif desired_action == "3":
                    user_or_pass = input("1-Kullanıcı adı değiştir\n2-Şifre değiştir\nV-Vazgeç\n\tSeçim:").upper()
                    if user_or_pass == "V":
                        break
                    elif user_or_pass == "1":
                        user_panel_username = input("Username:")
                        user_panel_password = input("Password:")

                        if user_panel_username == username and user_panel_password == password:
                            user_panel_username = input("Username:")
                            username = user_panel_username
                            print("Yeni kullanıcı adınız {}".format(username))
                        else:
                            print("Kullanıcı adı veya şifre yanlış")
                    elif user_or_pass == "2":
                        user_panel_username = input("Username:")
                        user_panel_password = input("Password:")
                        if user_panel_username == username and user_panel_password == password:
                            while True:
                                user_panel_username = input("Username:")
                                change_password = input("New password:")
                                again_change_password = input("Enter the new password again:")
                                if change_password != again_change_password:
                                    print("Girilen şifreler uyuşmadı, tekrar deneyiniz.")
                                else:
                                    password = change_password
                                    for p in password:
                                        print("*",end="")
                                    print("\nŞifreniz güncellendi")
                                    break
                            while True:
                                show_pass = input("Şifreyi görüntülemek ister misiniz? (E/H)\n\tSeçim:").upper()
                                if show_pass == "E":
                                    print(f"Yeni şifre: {password}")
                                    break
                                elif show_pass == "H":
                                    break
                                else:
                                    print("Kodlama hatası")
                elif desired_action == "4":
                    import time
                    print("Products: ",end=" ")
                    print(products)
                    print("Prices: ",end=" ")
                    print(prices)
                    print("\n")
                    time.sleep(3)
                    while True:
                        keep_up = input("Başka bir işlem yapmak istiyor musunuz? (1-Evet\t2-Hayır)\n\tSeçim:")
                        if keep_up == "1" or keep_up == "2":
                            break
                        else:
                            print("Kodlama hatası")
                            continue
                else:
                    print("Kodlama hatası")
                    continue
        else:
            right_of_Entry -= 1
            print("Kullanıcı adı veya şifre hatalı")
    elif secim == "2":
        invoice = 0
        remaining_money = 0
        balance = 0
        money_inflow = None
        while keep_up != "2" and money_inflow != "Q":
            count = 0
            print("\t\tKOD"+"\t\t\tFiyatlar")
            for product in products:
                a = 0
                print(f"Product: {count} - {product}",end="\t")
                for price in prices:
                    if a == 1:
                        break
                    else:
                        print(prices[count])
                        count += 1
                        a = 1
            while keep_up != "2":
                money_inflow = input("Para girişi:").upper()
                if float(money_inflow) < min(prices) and invoice < min(prices):
                    print("Girilen para en ucuz ürünümüzden daha az\n")
                    money_inflow = input("Para girişi:").upper()
                    if money_inflow == "Q":
                        break
                else:
                    choose = int(input("Ürün kodunu yazınız:"))
                    print(products[choose],"ürün fiyatı: ",prices[choose])
                    if float(money_inflow) - prices[choose] < 0 and invoice < prices[choose]:
                        print("Bakiye yetersiz")
                        while True:
                            keep_up = input("Devam etmek istiyor musunuz? (1-Evet\t2-Hayır)\n\tSeçim:")
                            if keep_up == "1":
                                break
                            elif keep_up == "2":
                                print("Toplam bakiye:", invoice)
                                break
                            else:
                                print("Kodlama hatası")
                                continue
                    else:
                        invoice = invoice + prices[choose]
                        remaining_money = float(money_inflow)
                        remaining_money -= prices[choose]
                        balance += remaining_money
                        print("Toplam bakiye:{}\t\tPara üstü: {}'TL".format(invoice,balance))
                        while True:
                            keep_up = input("Başka bir arzunuz? (1-Evet\t2-Hayır)\n\tSeçim:")
                            if keep_up == "1":
                                break
                            elif keep_up == "2":
                                break
                            else:
                                print("Kodlama hatası")
                                continue
    else:
        print("Kodlama hatası")
        continue

if secim == "Q" or keep_up == "2":
    print("Çıkış yapılıyor..")
    import time
    time.sleep(2)