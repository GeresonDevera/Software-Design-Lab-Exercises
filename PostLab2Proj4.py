print("""
ATM Machine at your service
----------------------
""")
password = 1434
PIN = ""
password_attempt = 1
is_password_lock = False

while PIN != password and not (is_password_lock):

    if password_attempt <= 3:
        PIN = int(input("Please enter your 4 digit PIN CODE\n"))

    else:
        is_password_lock = True
    password_attempt = password_attempt + 1

if is_password_lock:
    print("""
    -------------------------------------------
    LOGIN DISABLED
    Dear customer, we've noticed that you have attempted to log in many times. 
    Due to exceeding attempts, we have
    made the decision to contact police about this incident.
    -------------------------------------------
    """)
else:
    print("Accepted, Thankyou!")