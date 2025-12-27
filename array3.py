
 #از کاربر پنج عدد رو بگیر و داخل یه لیست ذخیره کن و بعد چاپ کن

numbers=int(input("enter 5 numbers:"))
i=numbers.split("_")
i=[int(n)for n in i]
print(i)