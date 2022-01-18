a_initial = 123
f_reverse = 0

f_reverse = (a_initial % 10)*100 + (a_initial % 100) // 10 * 10 + a_initial // 100
print(a_initial)
print(f_reverse)