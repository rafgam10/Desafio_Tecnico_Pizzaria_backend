from src.settings.extensions import db
from src import create_app
from src.models.pizza_model import Pizza
from src.models.item_pedido_model import Item_Pedido
from src.models.pedido_model import Pedido
import pytest


@pytest.mark.skip(reason="Passou")
def test_model_pizza():
    
    app = create_app()
    
    with app.app_context():
        db.create_all()
        pizza = Pizza("Calabresa", 6.0)
        db.session.add(pizza)
        db.session.commit()
      
@pytest.mark.skip(reason="Passou")  
def test_model_item_pedido():
    
    app = create_app()
    
    with app.app_context():
        db.create_all()
        item = Item_Pedido(1, 3)
        db.session.add(item)
        db.session.commit()

@pytest.mark.skip(reason="Passou")  
def test_model_pedido():
    
    app = create_app()
    
    with app.app_context():
        db.create_all()
        
        itens = Item_Pedido.query.all()
        
        total = sum(item.pizzas.preco * item.quantidade for item in itens)
        
        pedido = Pedido(id_item_pedido=1, total=total)
        db.session.add(pedido)
        db.session.commit()