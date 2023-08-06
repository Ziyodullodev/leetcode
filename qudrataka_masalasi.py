# 24intager
# Hafta kunlari agar 1 yanvar == yakshanba k berilgan raqamdagi kun qaysi hafta kuniga togri keladi degan savol ;)
# weeks = ["shanba","yakshanba",
#     "dushanba","seshanba",
#     "chorshanba","payshanba","Juma"]

# while 1:
#     k = input("Kunni kiriting = ")
#     if k == "exit":
#         print("dastur ishlash to'xtatildi.")
#         break
#     try:
#         k = int(k)
#     except:
#         print("Faqat butun son kiriting !")
#         continue
#     print(f"hafta kuni {weeks[k%7]}") # bu joyda k ni 7 ga bolgandagi qoldiqni olyapman va osha indexdagi hafta kunini qaytaryapman


# onlik_raqamlar = {
#     '1' : "o'n",
#     '2' : "yigirma",
#     '3' : "o'ttiz",
#     '4' : "qirq",
#     '5' : "ellik",
#     '6' : "oltmish",
#     '7' : "yetmish",
#     '8' : "sakson",
#     '9' : "toqson",
#     '10' : "yuz",
# }
# birlik_raqamlar = {
#     '1' : "bir",
#     '2' : "ikki",
#     '3' : "uch",
#     '4' : "tort",
#     '5' : "besh",
#     '6' : "olti",
#     '7' : "yetti",
#     '8' : "sakkiz",
#     '9' : "toqqiz",
#     '10' : "on",
# }

# n = 88
# def onlik_raqam(raqam):
#     onlik = n // 10
#     birlik = n % 10
#     son = onlik_raqamlar[str(onlik)] + "-" + birlik_raqamlar[str(birlik)]
#     return son


# if n > 100:
#     onlik = n // 10
#     birlik = n % 10
#     print(onlik_raqamlar[str(onlik)] + "-" + birlik_raqamlar[str(birlik)])

# elif n > 10:
#     num = onlik_raqam(n)

# else:
#     print(birlik_raqamlar[str(n)])

# print(num)


# a = 5
# n = 3
# jami_raqam = 0
# operator = ["-", "+"]
# operator_index = 0

# for i in range(1, n+1):
#     darajali_a = a ** i
#     jami_raqam += ((-1) ** operator_index) * darajali_a
#     operator_index = (operator_index + 1) % 2

# print(jami_raqam)



# n = 5
# jami = 1

# def calculate_factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * calculate_factorial(n - 1)

# for i in range(1, n+1):
#     jami += calculate_factorial(i) // 1

# print(jami)

# n = 110
# jami = 1

# def calculate_factorial_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * calculate_factorial_recursive(n - 1)

# def calculate_sum_of_factorials(n, i=1):
#     if i > n:
#         return 0
#     else:
#         return calculate_factorial_recursive(i) + calculate_sum_of_factorials(n, i + 1)

# jami += calculate_sum_of_factorials(n)
# print(jami)