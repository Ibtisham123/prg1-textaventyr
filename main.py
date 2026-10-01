# Här skriver du ditt textäventyr

print("=== IbtishamAdventure ===")
namn = input("Skriv ditt namn, pilot: ").strip()

print(f"\nLarmet tjuter! Ditt rymdskepp har kraschat på en främmande planet.")
print("Rök fyller kabinen och du måste gör någonting snabbt.")

# Val 1
print("\nVad gör du?")
print("1. Undersöker kontrollpanelen")
print("2. Öppnar nödutgången och går ut")

val1 = input("Ditt val (1 eller 2): ").strip()

if val1 == "1":
    print(f"\n{namn} sätter sig vid den rykande kontrollpanelen.")
    print("1. Skicka ut en nödsignal")
    print("2. Dra ut alla strömkablar")

    val2 = input("Ditt val (1 eller 2): ").strip()


if val1 == "1":
    if val2 == "1":
        print(f"\n VINST! Nödsignalen gick fram. Ett närliggande skepp räddade {namn}!")
    elif val2 == "2":
        print("\n GAME OVER! En gnista antände bränslet och skeppet exploderade.")
    else:
        print("\nDu kunde inte bestämma dig och blev kvar i den rykande kabinen.")
else:
    print("\nFelaktigt val. Du panikade och äventyret tog slut.")