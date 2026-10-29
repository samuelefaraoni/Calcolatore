class Operazione:
    def __init__(self, nome: str, *valori) -> None:
        self.nome = nome
        self.valori = list(valori)

    def esegui(self):
        raise NotImplementedError("Le classi figlie devono implementare esegui()")

    def __str__(self) -> str:
        return f"{self.nome}: {self.valori}"


class Somma(Operazione):
    def __init__(self, *valori) -> None:
        super().__init__("somma", *valori)

    def esegui(self):
        return sum(self.valori)

class Sottrazione(Operazione):
    def __init__(self, primo, secondo) -> None:
        super().__init__("sottrazione", primo, secondo)

    def esegui(self):
        return self.valori[0] - self.valori[1]


class Divisione(Operazione):
    def __init__(self, dividendo, divisore) -> None:
        super().__init__("divisione", dividendo, divisore)

    def esegui(self) -> float:
        if self.valori[1] == 0:
            raise ValueError("Non si puo dividere per zero")
        return self.valori[0] / self.valori[1]


class Moltiplicazione(Operazione):
    def __init__(self, *valori) -> None:
        super().__init__("moltiplicazione", *valori)

    def esegui(self):
        risultato = 1
        for valore in self.valori:
            risultato *= valore
        return risultato