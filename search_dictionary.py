"""
Implementarea unui dictionar roman englez si a functionalitatii de cautare in
aceste, pe baza unui cuvant
In cazul in care nu ete gasit cuvantul in dictionar se va ridica o eroare
definita de utilizator WordNotFoundError

"""


class Error(Exception):
    """Clasa pe baza pentru exceptii definite de utilizator"""
    pass


class WordNotFoundError(Error):
    """Clasa pentru exceptii la cautare fara succes in dictionar"""


class Dict:
    """Clasa pentru instante de tip dictionar, perechi cuvand: traducere
    Atribute:
        name(str):      numele dictionarului
        word (dict):    dictionarul de cuvinte, perechi de stringuri
                        word: translation
        tota_(init):    numarul total de definitii (cuvinte)
    Metode:
        __init__(self, name, initial_words)
            - constructorul pe baza nume si dictionar de start
        add(self, word, translation)
            - adauga un cuvant word cu traducerea translation la dictionar
        display(self)
            - afiseaza perechi cuvant: traducere (valorile din dictionar)
        search(self, word)
            - cauta cuvantul word in dictionar
                - afiseaza traducerea daca este gasit
                - astfel, ridica exceptia WordNotFoundError
        count():
            - afiseaza numarul de cuvinte din dictonar (total)

    """
    total = 0

    def __init__(self, name='Dictionar Ro-En', initial_words=None):
        self.name = name
        if initial_words is None:
            self.words = {}
        else:
            self.words = initial_words.copy()
            Dict.total = Dict.total + len(initial_words)

    def add(self, word, translation):
        self.words[word] = translation
        Dict.total += 1

    def display(self):
        for word, translation in self.words.items():
            print(f'{word} = {translation}')

    def search(self, word):
        try:
            translation = self.words.get(word)
            if translation is None:
                raise WordNotFoundError(
                    f'Cuvantul {word} nu este un dictionar')
        except WordNotFoundError as e:
            return f'>>>{e.__class__.__name__}: {e}'
        else:
            return f'Rezultat cautat: {word} = {translation}'

    @staticmethod
    def count():
        return (f'Dictionarul are {Dict.total} cuvinte')


def main():
    d = Dict('Dictionar Roman Englez',
             {'mare': 'sea', 'calculator': 'computer'})
    d.add('zi', 'day')
    d.add('ora', 'hour')
    d.add('soare', 'sun')
    d.add('apa', 'water')
    d.display()
    print(d.search('zi'))
    print(d.search('eveniment'))  # ridica o exceptie wordNotFoundError
    print(d.search('soare'))

    print(Dict.count())


if __name__ == '__main__':
    main()
