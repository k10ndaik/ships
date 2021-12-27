from bd import create_db, create_shipsTB

ships = create_db('ships')

bd = ships.connect()

shipsTB = create_shipsTB(ships)

shipsTB.auto_all()

shipsTB.auto_ship(200)





