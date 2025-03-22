from src.utils.base_prompt import BasePrompt


class UkrainianInstructionTemplate(BasePrompt):
    template: str = """Виправте наступний текст, зробивши його граматично правильним. Якщо помилок немає, повторіть текст без змін.

{original_text}"""
    input_variables: list[str] = ["original_text"]


class ItalianInstructionTemplate(BasePrompt):
    template: str = """Correggere tutti gli errori ortografici, di punteggiatura, stilistici, grammaticali, lessicali e sintattici nel testo seguente. 
Se non ci sono errori, è sufficiente ripetere il testo. 
Nella risposta, fornite solo il testo corretto senza ulteriori spiegazioni o commenti.

{original_text}"""
    input_variables: list[str] = ["original_text"]


class GermanInstructionTemplate(BasePrompt):
    template: str = """Korrigieren Sie alle Rechtschreib-, Interpunktions-, Stil-, Grammatik-, lexikalischen und syntaktischen Fehler in dem folgenden Text. 
Wenn keine Fehler vorhanden sind, wiederholen Sie den Text einfach. 
Geben Sie in Ihrer Antwort nur den korrigierten Text ohne weitere Erläuterungen oder Kommentare wieder.

{original_text}"""
    input_variables: list[str] = ["original_text"]


class CzechInstructionTemplate(BasePrompt):
    template: str = """Opravte všechny pravopisné, interpunkční, stylistické, gramatické, lexikální a syntaktické chyby v následujícím textu. 
Pokud v něm nejsou žádné chyby, text jednoduše zopakujte. 
V odpovědi uveďte pouze opravený text bez dalších vysvětlivek a komentářů.

{original_text}"""
    input_variables: list[str] = ["original_text"]


class EnglishInstructionTemplate(BasePrompt):
    template: str = """Correct all errors in the following text: spelling, punctuation, stylistic, grammatical, lexical, and syntax. 
If there are no errors, simply repeat the original text. 
In your answer, provide only the corrected text without any additional explanations or comments.

{original_text}"""
    input_variables: list[str] = ["original_text"]


class SloveneInstructionTemplate(BasePrompt):
    template: str = """Popravite vse napake v naslednjih besedilih: pravopisne, interpunkcijske, slogovne, slovnične, leksikalne in skladenjske. 
Če napak ni, preprosto ponovite izvirno besedilo. 
V odgovoru navedite samo popravljeno besedilo brez dodatnih pojasnil ali komentarjev.

{original_text}"""
    input_variables: list[str] = ["original_text"]


class GreekInstructionTemplate(BasePrompt):
    template: str = """Διορθώστε όλα τα λάθη στο ακόλουθο κείμενο: ορθογραφία, στίξη, υφολογικά, γραμματικά, λεξιλογικά και συντακτικά. 
Εάν δεν υπάρχουν λάθη, απλώς επαναλάβετε το αρχικό κείμενο. 
Στην απάντησή σας, δώστε μόνο το διορθωμένο κείμενο χωρίς πρόσθετες εξηγήσεις ή σχόλια.

{original_text}"""
    input_variables: list[str] = ["original_text"]


class EstonianInstructionTemplate(BasePrompt):
    template: str = """Parandage kõik vead järgmises tekstis: õigekirja-, kirjavahemärgistus-, stiili-, grammatika-, leksika- ja süntaksivigad. 
Kui vigu ei ole, korrake lihtsalt originaalteksti. 
Esitage oma vastuses ainult parandatud tekst ilma täiendavate selgituste või kommentaarideta.

{original_text}"""
    input_variables: list[str] = ["original_text"]


class LatvianInstructionTemplate(BasePrompt):
    template: str = """Labojiet visas kļūdas šādā tekstā: pareizrakstības, interpunkcijas, stilistikas, gramatikas, leksikas un sintakses. 
Ja kļūdu nav, vienkārši atkārtojiet sākotnējo tekstu. 
Atbildē sniedziet tikai laboto tekstu bez papildu paskaidrojumiem vai komentāriem.

{original_text}"""
    input_variables: list[str] = ["original_text"]


class SwedishInstructionTemplate(BasePrompt):
    template: str = """Korrigera alla fel i följande text: stavning, skiljetecken, stilistiska, grammatiska, lexikala och syntaktiska fel. 
Om det inte finns några fel, upprepa helt enkelt originaltexten. 
I ditt svar ska du endast ange den korrigerade texten utan några ytterligare förklaringar eller kommentarer.

{original_text}"""
    input_variables: list[str] = ["original_text"]


class IcelandicInstructionTemplate(BasePrompt):
    template: str = """Leiðréttu allar villur í eftirfarandi texta: stafsetningu, greinarmerki, stílfræði, málfræði, orðafræði og setningafræði.
Ef það eru engar villur skaltu einfaldlega endurtaka upprunalega textann.
Í svarinu þínu skaltu aðeins gefa upp leiðréttan texta án frekari útskýringa eða athugasemda.

{original_text}"""
    input_variables: list[str] = ["original_text"]

