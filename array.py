
#پیدا کردن بزرگترین و کوچکترین عدد

numbers=[12,1,5,78,98,95,45,34,23]
max_num=numbers[0]
min_num=numbers[0]
for n in numbers:
      if n > max_num:
           max_num = n
      if n < min_num:
            min_num = n
      print("max",max_num)
      print("min",min_num)