from src.settings.extensions import db

class Item_Pedido(db.Model):
    
    __tablename__ = "itens_pedidos"
    
    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text, default=None, nullable=True)
    
    pedidos = db.relationship(
        "Pedido",
        backref="itens_pedidos",
        lazy=True,
        cascade="all, delete-orphan"
    )
    
    def __init__(self, pizza_id, quantidade, descricao=None):
        self.pizza_id = pizza_id
        self.quantidade = quantidade
        self.descricao = descricao

    def __repr__(self):
        return f"Item_Pedido: {self.pizza_id} - {self.quantidade}"
    
    def __to_dict_(self):
       ...