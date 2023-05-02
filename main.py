import random


def main():
    print("Üdvözöllek a Robot szólánc játékban!")
    print("A játék lényege, hogy a megadott szó utolsó betűjével kell kezdened a következő szót.")
    print("Ha nem tudsz szót mondani, vesztettél.")
    print("Kezdjük!")

def main():
    words = ["alma", "baba", "csokoládé", "dió", "eper", "fűszer", "gumicsizma", "hinta", "iskola", "jégkorong", "karfiol", "limonádé", "málna", "narancs", "óra", "paprika", "quiche", "rózsa", "szék", "tyúk", "uborka", "víz", "walesi", "xilofon", "yzop"]
    print("Üdvözöllek a robot szólánc játékban!")
    print("A játék célja, hogy olyan szót adj meg, amely az előző szó utolsó betűjével kezdődik.")
    user_word = input("Kezdjük! Add meg az első szót: ")
    while user_word:
        robot_word = [word for word in words if word[0] == user_word[-1] if len(user_word) > 0]
        if not robot_word:
            print("Sajnálom, nem találtam olyan szót, amely az utolsó betűvel kezdődik.")
            break
        robot_choice = robot_word[0]
        print("Az én szavam:", robot_choice)
        user_word = input("Add meg a következő szót: ")
    print("Köszönöm, hogy játszottál!")

    # Betöltjük a szavakat tartalmazó fájlt.
    with open("magyarszavak.txt", "r", encoding="utf-8") as f:
        words = f.read().splitlines()

    # Robot választ egy véletlen szót.
    robot_word = random.choice(words)
    print(f"A robot választott szava: {robot_word}")

    # Felhasználó választ egy szót, amely az előző szó utolsó betűjével kezdődik.
