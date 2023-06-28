# 24intager
# Hafta kunlari agar 1 yanvar == yakshanba k berilgan raqamdagi kun qaysi hafta kuniga togri keladi degan savol ;)
weeks = ["shanba","yakshanba",
    "dushanba","seshanba",
    "chorshanba","payshanba","Juma"]

while 1:
    k = input("Kunni kiriting = ")
    if k == "exit":
        print("dastur ishlash to'xtatildi.")
        break
    try:
        k = int(k)
    except:
        print("Faqat butun son kiriting !")
        continue
    print(f"hafta kuni {weeks[k%7]}") # bu joyda k ni 7 ga bolgandagi qoldiqni olyapman va osha indexdagi hafta kunini qaytaryapman
