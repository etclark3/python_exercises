MC = 3
LM = 3
BB = 5
H = 1
print(MC*(LM + BB + H))

#
gpay = 400
fbpay = 350
amzpay = 380

gwork = 6
fbwork = 10
amzwork = 4

weekly_pay = (gpay * gwork) + (amzpay * amzwork) + (fbpay * fbwork)
print(f'My paycheck this week will be ${weekly_pay}')
#

p_member = True
two_or_more_items = False
offer = True

#
username = 'codeup'
password = 'notastrongpassword'

if len(password) < 5:
    print('False')
if len(password) > 5:
    print('True')

if len(username) > 20:
    print('the username must be no more than 20 characters')
if len(username) < 20:
    print('Username meets requirements')

if password == username:
    print('the password must not be the same as the username')
if password != username:
    print('True')

if password {0 = ' '} or {-1 = ' '}:
    print('password cannot start or end with a space')

#

username = 'codeup'
password = 'codeup'

