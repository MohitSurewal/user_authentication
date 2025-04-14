import getpass        #getpass is used to hiding password not shows characters.

def user_authentication():
    #users id and password and the hints of the passwords:

    users = {
        "admin": {"password": "greatpin123", "role": "Administrator","hint": "start with G and endwith 123"},
        "mohit": {"password": "muskan123", "role": "guest", "hint": "friendship is password"},
        "muskan": {"password": "stands4466", "role": "staff", "hint": "start with s and with 4466"}
    }

    superuser_password = "RootAccess"
    attempts = 3 

    while (attempts > 0):
        print("\n----login------")
        username = input("Enter Your Username: ").strip()

        if username not in users:
            forgot = input("Username not found in users. forgot username (yes/no)?: ").strip().lower()

            if forgot == "yes":
                print("Available Username", ", ".join(users.keys()))
            attempts -=1
            continue

        is_superuser = input("Are You a Superuser? (YES/NO); ").strip().lower() == "yes"

        if is_superuser :
                su_pass = getpass.getpass("Enter Superuser Password: ").strip()
                if su_pass == superuser_password:
                    print(f"✅ Superuser '{username}' Logged in Successfully!")
                    print("🔓 Full Super Access granted ")
                    with open ("Superuser_log.txt", "a") as log_file:
                        log_file.write(f"Superuser '{username}' accessed the system.\n")
                    break
                else:
                    print("❌ Wrong Superuser Password.")

        else:
                password = getpass.getpass("Enter your Password: ")
                
                if users[username]["password"] == password:
                    print(f"✅{users[username]['role'].capitalize()}'{username}'logged successfully!")
                    print(f"🔏Access Level: {users[username]['role']}")
                    break
                else: 
                    forgot = input("wrong passwords. Forgot password? (YES/NO): ").strip().lower()
                    if forgot == "yes":
                        print(f"🔎password hint for '{username}': {users[username]['hint']}")

        attempts -= 1 
        if attempts > 0:
                print(f"☢️ You have {attempts}. attemps left.")
        else:
                print("🚫Too many failed attempts. Access Denied: ")


user_authentication()



