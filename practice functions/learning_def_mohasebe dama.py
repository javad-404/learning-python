def celsius_to_fahrenheit (a):
    F = (a * (9.5)) + 32
    return F
user_select = float(input("dmaye snatigrad ro vared konid: "))
f = celsius_to_fahrenheit(user_select)
print (f"dmaye farnahayat is {f}")