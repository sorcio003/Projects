class Worker():
    
    def __init__(self, nome, cognome, email, email_cliente, paga_oraria, descript):
        
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.email_cliente = email_cliente
        self.descript = descript
        
        self.paga_oraria = paga_oraria
        
        self.lista = [self.nome, self.cognome, self.email, self.email_cliente, self.paga_oraria, self.descript]