from src.settings.extensions import db

class Pizza(db.Model):
    
    __tablename__="pizzas"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    
    itens_pedidos = db.relationship(
        'Item_Pedido',
        backref='pizzas',
        lazy=True,
        cascade='all, delete-orphan'
    )
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def __repr__(self):
        return f"Pizza: {self.nome} - {self.preco}"
    
    def __to_dict_(self):
        ...