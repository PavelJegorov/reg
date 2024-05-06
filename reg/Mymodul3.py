login_password_list = [[], []]

def kirjuta_failisse(fail: str):
    with open(fail, "w", encoding="utf-8") as f:
        if login_password_list[0]:  # Check if there's at least one login
            f.write(",".join(login_password_list[0]))
        f.write("\n")
        if login_password_list[1]:  # Check if there's at least one password
            f.write(",".join(login_password_list[1]))

def lisamine_failisse(fail: str, login, parool: str):
    global login_password_list
    # Directly append the new login and password to the global list
    login_password_list[0].append(login)
    login_password_list[1].append(parool)
    # Now write the updated list back to the file
    kirjuta_failisse(fail)


def loe_failist(fail: str):
    global login_password_list
    try:
        with open(fail, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) >= 2:
                login_password_list[0] = lines[0].strip().split(",")
                login_password_list[1] = lines[1].strip().split(",")
            else:
                login_password_list = [[], []]  # Reset if file is empty or malformed
    except FileNotFoundError:
        login_password_list = [[], []]  # Reset if file does not exist
# Alusta tühjade listidega
login_password_list = [[], []]
loe_failist("login_parool.txt")
def andmete_uuendamine():
    login_password_list.clear()
    login_password_list.append(loe_failist("login_parool.txt"))

login_password_list = []
loe_failist("login_parool.txt")
def register(login: str, password: str):
    global login_password_list
    if login in login_password_list[0]:
        print("Kasutajanimi on juba olemas!")
        return None  # Or another appropriate response
    lisamine_failisse("login_parool.txt", login, password)
    print("Kasutaja registreeritud edukalt!")
    return login_password_list[0].index(login)


def authorize(kasutaja_nimi: str, parool: str) -> any:
    """
    see funktsioon autoriseerib kasutaja
    Args:
        login (str): kasutaja nimi
        password (str): kasutaja parool
    :rtype: any
    """
    # vaatame et nimi ei ole kasutatud
    if kasutaja_nimi not in login_password_list[0]:
        print("ei ole kasutajat selle nimega!")
        return False
    # Kasutaja sisselogimisnime indeksi hankimine loendis
    index = login_password_list[0].index(kasutaja_nimi)

    # vaaatame kas parool on õige
    if parool != login_password_list[1][index]:
        print("vale parool!")
        return False
    return index

def change_login(indeks: int, new_login: str) -> any:
    """
    see funktsioon muudab kasutaja nime
    Args:
        login (str): vana kasutaja nimi
        new_login (str): uus kasutaja nimi
    :rtype: any
    """
    # vaadame et kasutaja nimi ei ole kasutatud
    # vaaatame kas uus nimi on juba kasutusel
    if new_login in login_password_list[0]:
        print("see nimi on juba kasutusel!")
        return False
    # Kasutaja sisselogimisnime muutmine loendis
    login_password_list[0][indeks] = new_login
    # printime edukat nime muutmist
    print("kasutaja nimi muudetud edukalt!")
    kirjuta_failisse("login_parool.txt")


# funktsioon et muuta kasutaja parool
def change_password(login: str, new_password: str) -> any:
    """
    see funktsioon muudab kasutaja parooli
    Args:
        login (str): kasutaja nimi
        new_password (str): kasutaja uus parool
    :rtype: any
    """
    # vaadame et kasutaja nimi ei ole kasutatud

    index = login_password_list[0].index(login)
    # vahetame kasutaja parooli loendis
    login_password_list[1][index] = new_password
    # prindime edukat parooli muutmist
    print("kasutaja parool muudetud edukalt!")
    kirjuta_failisse("login_parool.txt")


# funktsioon et taastada kasutaja parool
def recover_password(indeks) -> any:
    """
    see funktsioon taastab kasutaja parooli
    Args:
        login (str): The user's login name.
    :rtype: any
    """
    import smtplib, ssl
    from email.message import EmailMessage

    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = "pavel.jegorov1232@gmail.com"
    to_email = input("sisesta teie emaili: ")
    password = "ejin jdpi iqzs tspp"

    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(login_password_list[1][indeks])
    msg["Subject"] = "Parooli tastamine "
    msg["From"] = "pael.jegorov1232@gmail.com"
    msg["To"] = to_email

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.send_message(msg)
    except Exception as e:
        print(e)
    finally:
        server.quit()

    return login_password_list[1][indeks]
