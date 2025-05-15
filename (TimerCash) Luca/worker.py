class Worker():
    
    def __init__(self, nome, cognome, email, paga_oraria):
        
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.paga_oraria = paga_oraria
        
        self.lista = [self.nome, self.cognome, self.email, self.paga_oraria]