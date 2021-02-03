# string, intiger, bool, float, double, char
# -------------Data types----------
skaicius = 0
zodis = "zodis"
flag = False
floatas = 0.00000222222

# -------------Data structures----------
phone_list = ["iphone 12", "samsung 20", "nokia 3310"]
tv_list = ["lg22222", "samsung22222", "silelis22"]
phone_list1 = ["stringas", "strings", 4, 5, False, False]
number_list = [1, 2, 3, 4, 5, 6, 7]
no_duplicate_set_from_list = set(phone_list1)

# galima keisti sukurtus irasus
nutable = ["iphone12", "samsung20"]
nutable[0] = "iphone13"

# negalima keisti
imnutable = ("iphone12", "samsung20")

dictionary = {"mobile_phones": phone_list, "tv": tv_list}

# ----------------printing------------
print(phone_list)

# --------------if logic states ----------------
if zodis == skaicius:
    print("zodis lygus skaiciui")
else:
    print("u suck sucker")

if len(phone_list) == len(imnutable):
    print("Sitie listai yra lygus")
elif phone_list == imnutable:
    print("lygus listai")
else:
    print("Neivyko funcionalumas")

# --------------loops-------------

for i in phone_list:
    print(i)

count = 0
while (flag == False):
    count += 1
    if count > 5:
        flag = True
        print("flag was changed")


# ----------------functions/methods------------------
def funcija(sarasas, sarasas1):
    print(phone_list)
    print(tv_list)


class user:
    def method(self, sarasas, sarasas1):
        print(sarasas)
        print(sarasas1)


# --------------------------function call/method call ------------------
funcija(phone_list, tv_list)


# --------------------Bubble sort ---------------
# def bubble_sort():
#     bubble_sort_list = [7, 3, 2, 8, 2, 1, 5, 3, 2, 1, 7, 3, 2]
#     is_sorting_finished = False
#     iteration_counter = 0
#     while is_sorting_finished == False:
#         did_sort_happen = False
#         for i in range(len(bubble_sort_list) - 1):
#             if bubble_sort_list[i] > bubble_sort_list[i + 1]:
#                 temp = bubble_sort_list[i]
#                 bubble_sort_list[i] = bubble_sort_list[i + 1]
#                 bubble_sort_list[i + 1] = temp
#                 did_sort_happen = True
#             iteration_counter += 1
#         if did_sort_happen == False:
#             is_sorting_finished = True
#
#     print(bubble_sort_list)
#     print(iteration_counter)
#
#
# bubble_sort()


# def fibonacci(fibonacci_index):
#     n1 = 0
#     n2 = 1
#     fibonacci_sequence = [n1, n2]
#     for i in range(fibonacci_index - 2):
#         n1 = fibonacci_sequence[-2]
#         n2 = fibonacci_sequence[-1]
#         new_number = n1 + n2
#         fibonacci_sequence.append(new_number)
#     print(fibonacci_sequence)

# def fibonacci_recursive(n):
#     if n <= 0:
#         print("Unable to return fibonacci")
#
#     elif n == 0:
#         return 0
#
#     elif n == 1 or n == 2:
#         return 1
#
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
#
#
# print(fibonacci_recursive(4))


# def carry_solver(n1, n2):
#
#     counter = 0
#     longer_number = max(len(str(n1)), len(str(n2)))
#     carry_in_mind = 0
#
#     for i in reversed(range(longer_number)):
#         carry_in_mind = n1 % 10 + n2 % 10 + carry_in_mind
#         if carry_in_mind >= 10:
#             carry_in_mind = 1
#         else:
#             carry_in_mind = 0
#             counter += carry_in_mind
#         n1 = n1 // 10
#         n2 = n2 // 10
# \
#
# print(carry_solver(80, 222))