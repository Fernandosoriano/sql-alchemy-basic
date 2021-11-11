import db
from models import Producto

def run():
    arroz = Producto('Arroz', 1.25)
    db.session.add(arroz)
    print(arroz.id)
    agua = Producto('Agua', 0.3)
    db.session.add(agua)
    db.session.commit()
    print(arroz.id)

# Lo importante en este punto es la línea db.Base.metadata.create_all(db.engine).
# En ella estamos indicando a SQLAlchemy que cree, si no existen,
# las tablas de todos los modelos que encuentre en la aplicación

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()