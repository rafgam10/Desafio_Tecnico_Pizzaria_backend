from src.settings.extensions import db

class Pedido(db.Model):
    
    __tablename__="pedidos"
    
    id=db.Column(db.Integer, primary_key=True)
    id_item_pedido=db.Column(db.Integer, db.ForeignKey('itens_pedidos.id'), nullable=False)
    # id_cliente=db.Column(db.Integer)
    total=db.Column(db.Float, nullable=False)
    
    def __init__(self, id_item_pedido, total):
        self.id_item_pedido = id_item_pedido
        self.total = total
        
    def __repr__(self):
        return f"Pedido: {self.id_item_pedido} - {self.total}"