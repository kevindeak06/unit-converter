def menu():
    # Kiírja a választási lehetőségeket a konzolra
    print("\n-- MÉRNÖKI ÁTVÁLTÓ --")
    print("1. Inch -> Milliméter (mm)")
    print("2. Milliméter (mm) -> Inch")
    print("3. Pound (font) -> Kilogramm (kg)")
    print("4. Kilogramm (kg) -> Pound (font)")
    print("5. Kilépés")


def start_program():
    # A program fő ciklusa
    fut = True
    while fut:
        menu()

        # Szövegként olvassuk be a választást, hogy ne omoljon össze hiba esetén
        valasztas = input("Válassz egy menüpontot (1-5): ")

        if valasztas == "1":
            try:
                # 1 inch = 25.4 mm
                ertek = float(input("Add meg az értéket inchben: "))
                eredmeny = ertek * 25.4
                print(f" {ertek} inch = {eredmeny:.2f} mm")
            except ValueError:
                # Hibakezelés, ha a felhasználó nem számot ad meg
                print("Kérlek számot adj meg!")

        elif valasztas == "2":
            try:
                # 1 mm = 1 / 25.4 inch
                ertek = float(input("Add meg az értéket milliméterben: "))
                eredmeny = ertek / 25.4
                print(f"{ertek} milliméter = {eredmeny:.2f} inch")
            except ValueError:
                print("Kérlek számot adj meg!")

        elif valasztas == "3":
            try:
                # Átváltás: font -> kg
                ertek = float(input("Add meg az értéket fontban: "))
                eredmeny = ertek * 0.45359237
                print(f"{ertek} font = {eredmeny:.2f} kilogramm")
            except ValueError:
                print("Kérlek számot adj meg!")

        elif valasztas == "4":
            try:
                # Átváltás: kg -> font
                ertek = float(input("Add meg az értéket kilogrammban: "))
                eredmeny = ertek / 0.45359237
                print(f"{ertek} kilogramm = {eredmeny:.2f} font")
            except ValueError:
                print("Kérlek számot adj meg!")

        elif valasztas == "5":
            # Kilépés a ciklusból
            print("Kilépés...")
            fut = False
        else:
            print("Érvénytelen választás! Próbáld újra!")


# A program indítása
if __name__ == "__main__":
    start_program()