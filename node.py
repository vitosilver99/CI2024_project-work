import operator 
import numpy as np

class Node:
    def __init__(self, value, children=None):
        # controlla che children sia una lista di Node o None
        if children is not None:
            assert all(isinstance(s, Node) for s in children), "Panic: Children must be `Node`"
        self.value = value
        self.children = children if children else []

    def __len__(self):
        return 1 + sum(len(c) for c in self.children)

    #Mi restituisce il valore della funzione trovata
    def evaluate(self, variables):
        """Valuta il nodo basandosi sul tipo di valore."""
        if callable(self.value):  # Se è un'operazione
            children_values = [child.evaluate(variables) for child in self.children]

            # Controllo per divisione per zero
            if self.value == operator.truediv:
                if abs(children_values[1]) < 1e-8:  # Evita divisori prossimi a zero
                    return 1e6  # Penalità per divisione per zero
            
            try:
                # Prova a calcolare il risultato
                result = self.value(*children_values)

                # Controlla per valori complessi
                if isinstance(result, complex):
                    return 1e6  # Penalità per numeri complessi
                
                # Controlla per NaN o valori infiniti
                if not np.isfinite(result):
                    return 1e6  # Penalità per valori non finiti
                
                return result
            except (OverflowError, ValueError, ZeroDivisionError):
                # Gestisce errori di overflow, dominio non valido, ecc.
                return 1e6  # Penalità generica per errori numerici
        elif isinstance(self.value, str):  # Se è una variabile
            return variables.get(self.value, 0)  # Usa 0 se la variabile non esiste
        else:  # Se è un valore numerico
            return self.value


    def __str__(self):
        return self.long_name

    @property
    def subtree(self):
        result = set()
        self._get_subtree(result)
        return result

    def _get_subtree(self, bunch: set):
        bunch.add(self)
        for c in self.children:
            c._get_subtree(bunch)

    @property
    def short_name(self):
        # questo necessario per ottenere ad esempio "add" e non tutto il <operator.add> etc..
        if callable(self.value):            
            return self.value.__name__
        return str(self.value)

    @property
    def is_leaf(self):
        return len(self.children) == 0

    @property
    def long_name(self):
        if self.is_leaf:
            return self.short_name
        return f'{self.short_name}(' + ', '.join(c.long_name for c in self.children) + ')'

    def copy(self):
        """
        Crea una copia profonda del nodo e di tutti i suoi figli.
        """
        # Copia il nodo corrente
        copied_children = [child.copy() for child in self.children]  # Ricorsivamente copia i figli
        return Node(self.value, copied_children)