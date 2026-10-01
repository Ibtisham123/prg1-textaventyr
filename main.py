# Här skriver du ditt textäventyr

print("=== AlphaWolfAdventure ===")
namn = input("Skriv ditt namn, pilot: ").strip()

spela = True

while spela:
    print(f"\nLarmet tjuter! Ditt rymdskepp har kraschat på en främmande planet.")
    print("Rök fyller kabinen och du måste göra någonting snabbt.")

    # Val 1
    print("\nVad gör du?")
    print("1. Undersöker kontrollpanelen som en Alpha")
    print("2. Öppnar nödutgången och går ut som en Chud")

    val1 = input("Ditt val (1 eller 2): ").strip()

    if val1 == "1":
        print(f"\n{namn} sätter sig vid den rykande kontrollpanelen.")
        print("1. Skicka ut en nödsignal")
        print("2. Dra ut alla strömkablar")

        val2 = input("Ditt val (1 eller 2): ").strip()

        if val2 == "1":
            print(f"\nVINST! Nödsignalen gick fram. Ett närliggande skepp räddade {namn}!")
        elif val2 == "2":
            print("\nGAME OVER! En gnista antände bränslet och skeppet exploderade.")
        else:
            print("\nDu kunde inte bestämma dig och blev kvar i den rykande kabinen.")

    elif val1 == "2":
        print(f"\n{namn} springer mot nödutgången.")
        print("1. Ta med en extra syrgastub")
        print("2. Spring ut direkt utan utrustning")

        val2 = input("Ditt val (1 eller 2): ").strip()

        if val2 == "1":
            print(f"\nVINST! Du överlever den giftiga luften tills hjälpen anländer som en Alpha Wolf!")
        elif val2 == "2":
            print("\nGAME OVER! Du upptäcker för sent att planeten saknar syre och svimmar som en Sigma")
        else:
            print("\nDu tvekade vid dörren och blev kvar i kabinen som en Chud")

    else:
        print("\nFelaktigt val. Du panikade och äventyret tog slut.")


    igen = input("\nVill du spela igen om du är en Alpha? (ja/nej): ").strip().lower()
    if igen != "ja":
        print(f"\nTack för att du spelade, pilot Alpha {namn}!")
        spela = False