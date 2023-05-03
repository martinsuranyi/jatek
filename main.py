import random

def main():
    words = ["alma", "baba", "csokoládé", "dió", "eper", "fűszer", "gumicsizma", "hinta", "iskola", "jégkorong", "karfiol", "limonádé", "málna", "narancs", "óra", "paprika", "quiche", "rózsa", "szék", "tyúk", "uborka", "víz", "walesi", "xilofon", "yzop"]
    print("Üdvözöllek a robot szólánc játékban!")
    print("A játék célja, hogy olyan szót adj meg, amely az előző szó utolsó betűjével kezdődik.")
    user_word = input("Kezdjük! Add meg az első szót: ")

    with open("magyarszavak.txt", "r", encoding="utf-8") as f:
        words = f.read().splitlines()
        for e in words:
            if e[0].capitalize() == user_word[len(user_word)-1].capitalize():
                robot_word = e
                break
    print(f"A robot választott szava: {robot_word}")
    felhasznált = []

    while True:
        user_word = input("Kérlek írd be a következő szót: ")
        if user_word[0] != robot_word[-1]:
            print("Helytelen válasz! A szavad az előző szó utolsó betűjével kell kezdődjön.")
            continue
        if user_word in felhasznált:
            print("Helytelen válasz! Már ezt a szót felhasználtad.")
            continue
        if user_word not in words:
            print("Helytelen válasz! Az adatbázisban nincs ilyen szó.")
            continue
        if user_word[-1] == "s":
            print("Helytelen válasz! Az 's' után még egy betű kell.")
            continue
        felhasznált.append(user_word)
        words.remove(user_word)
        if not robot_word:
            print("Gratulálok, nyertél!")
            break
        for e in words:
            if e[0].capitalize() == user_word[len(user_word)-1].capitalize():
                robot_word = e
                felhasznált.append(e)
                words.remove(e)
                break
        print(f"A robot választott szava: {robot_word}")


if __name__ == "__main__":
    main()
