## [Datum] – [Kort titel på problemet]

**Vad gick fel:**
syntaxfel på grund av ett tomt elif , dubbla else-block och en oavslutad textsträng

**Varför:**
elif saknade ett vilkor, och indateringen gjorde att det sista else-blocket hamnade utanför sin logiska kedja.

**Hur jag löste det:**
Ändrade elif: till else:, stängde strängen och strukturerade om under en yttre if- sats

**Vad jag skulle göra annorlunda:**
Använda en kodeditor med syntaksmarkering som varnar för felaktig indatering och öppna strängar direkt.

**AI-granskning (om tillämpligt):**
[Vad AI föreslog / vad du ändrade / vad AI missade]