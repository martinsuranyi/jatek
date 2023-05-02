
    # Felhasználó választ egy szót, amely az előző szó utolsó betűjével kezdődik.
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
        #[word for word in words if word[0] == user_word[-1] if len(user_word)>0]
        if not robot_word:
            print("Gratulálok, nyertél!")
            break
        for e in words:
            if e[0].capitalize() == user_word[len(user_word)-1].capitalize():
                robot_word = e
                break
        print(f"A robot választott szava: {robot_word}")


if __name__ == "__main__":
    main()
