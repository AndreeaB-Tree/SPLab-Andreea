# Lab2

Cateva remarci, de jos in sus: 
- la subchapter sa faci metode de addImage(url), addParagraph(text), addTable(text), iar in aceste metode creezi obiectele respective si le pui intr-o lista de elemente
- la chapter ar trebui sa ai o lista de subchapters. Ar trebui o metoda de addSubchapter(subTitle), unde creezi un subchapter, il pui in lista si returnezi indexul unde l-ai pus in lista
- la chapter ar trebui o metoda de getSubchapter(index) care returneaza subcapitolul din lista ta de la indexul respectiv
- la Book acelasi mecanism, adica ai o lista de capitole, si metoda addChapter(title) si getChapter(index)
- toate clasele sa aiba metode de print(), iar cand apelezi print() de la Book, acolo printezi titlul, autorul, si printezi si toate capitolele care le ai in lista
- cand printezi un capitol, printezi titlul si toate subcapitolele
- cand printezi un subcapitol, printezi subtitlul si apelezi metoda de print de la toate obiectele (paragrafe, tabele, imagini) pe care le ai in lista de elemente

# lab3

- ai in plus pana la linia 60 definitii de clase care le poti sterge
- in clasa Book, addContent nu face altceva decat sa apeleze super.add din section (book mosteneste section si astfel are tot managmentul de elemente de acolo)
- in metoda de print de la Book, trebuie doar sa printezi autorii si sa apelezi super.print() din section
- metoda printBook este chiar printElement() suprascris din Element (care e mostenit de section, care e suprascris de Book)

In general, la commit sa pui mesaje cu ce ai contine. Ar trebui sa ai doar codul sursa curent, si sa lucrezi cu branch-uri. Urmatorul lab care il butonezi sa faci asa:
- <git status> ar trebui sa iti afiseze ca esti pe branch-ul main
- <git checkout -b lab4> o sa iti creeze local branch-ul de lab3
- creezi fisiere .py pentru fiecare clasa si faci import de ele unde ai nevoie si stergi folder-ele de lab2 si lab3
- <git add *> sau poate mai trebuie sa faci add manual la ceva chestii
- <git commit -m "refactoring and add proxy for image">
- <git push>
astfel vei avea pe branch continutul labului, si din web de pe github faci pull request ca sa iti aduci modificarile de pe branch pe main.

Sa imi zici sa facem eventual impreuna la lab tot acest mecanism
