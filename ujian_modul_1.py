# nomor 1

# def create_phone_number() :
#     input_no = input('input your phone number:')
#     list_input = list(input_no)
#     list_kosong = []
#     for i in list_input:
#         if ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'):
#             print('invalid input must be alphabet')
#             break
#         elif ord('!') <= ord(i) <= ord('.'):
#             print('invalid input no symbol')
#             break
#         elif int(i) < 0:
#             print('input only positive number')
#             break
#         elif len(input_no) != 10:
#             print('Digits must in length of 10 no more no less.')
#             break
#         elif 0 <= int(i) <= 9:
#             list_kosong.append(i)
        
#         if len(list_kosong) == 10:
#             list_kosong.insert(0, '(')
#             list_kosong.insert(4, ') ')
#             list_kosong.insert(8, '-')
#             input_join = ''.join(list_kosong)
#             print(input_join)
    
# create_phone_number()



# nomor 2

# def movezeros(list):
#     list_ada = list
#     list_kosong = []
#     for i in list:
#         if i == 0:
#             list_ada.pop(list_ada.index(i))
#             list_kosong.append(i)
#     list3 = list_ada + list_kosong
#     print('result:', list3)

# movezeros(['a',True,False,4,0,7,0])



# nomor 3

# class St:
#     def mean(list_mean):
#         num_sum = sum(list_mean)
#         mean = num_sum / len(list_mean)
#         print(round(mean, 3))
          
#     def median(list_median):
#         list_median.sort()
#         if len(list_median) % 2 == 0:
#             first_median = list[len(list_median) // 2]
#             second_median = list[len(list_median) // 2 - 1]
#             median = (first_median + second_median) / 2
#         else:
#             median = list_median[len(list_median) // 2]
#         print(median)

#     def mode(list_mode):
#         if list_mode == []:
#             return None
#         else:
#             a = (max(set(list_mode), key=list_mode.count))
#             print(a)
    
#     def std(list_std):
#         n = len(list_std)
#         u = sum(list_std) / n
#         list_jumlah = []
#         for xi in list_std:
#             jumlah = (xi - u)**2
#             list_jumlah.append(jumlah)
#         std = (sum(list_jumlah) / n) ** (1/2)
#         print(std)
        

# St.mean([1,2,3])
# St.median([1,2,3])
# St.mode([1,2,3])
# St.std([1,2,4,5,6,7])

