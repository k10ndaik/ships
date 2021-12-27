from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey
from datetime import datetime

import random


def create_shipsTB(bd):
    metadata = MetaData()

    weapons = Table('weapons', metadata,
                 Column('weapon', Text(), primary_key=True),
                 Column('reload_speed', Integer()),
                 Column('rotation_speed', Integer()),
                 Column('diameter', Integer()),
                 Column('power_volley', Integer()),
                 Column('count', Integer()),
                 )

    hulls = Table('hulls', metadata,
                    Column('hull', Text(), primary_key=True),
                    Column('armor', Integer()),
                    Column('type', Integer()),
                    Column('capacity', Integer()),
                    )

    engines = Table('engines', metadata,
                    Column('engine', Text(), primary_key=True),
                    Column('power', Integer()),
                    Column('type', Integer()),
                    )

    ship = Table('ship', metadata,
                 Column('ship', Text(), primary_key=True),
                 Column('weapon', ForeignKey("weapons.weapon")),
                 Column('hull', ForeignKey("hulls.hull")),
                 Column('engine', ForeignKey("engines.engine")),
                 )

    metadata.create_all(bd)
    class Ships():
        def __init__(self):
            self.ship = ship
            self.weapons = weapons
            self.hulls = hulls
            self.engines = engines

        def auto_weapons(self, number):
            for i in range(number):
                ins = self.weapons.insert().values(
                    weapon=f'weapon-{i+1}',
                    reload_speed=random.randint(1,20),
                    rotation_speed=random.randint(1,20),
                    diameter=random.randint(1,20),
                    power_volley=random.randint(1,20),
                    count=random.randint(1,20)
                )
                bd.execute(ins)

        def auto_hulls(self, number):
            for i in range(number):
                ins = self.hulls.insert().values(
                    hull=f'hull-{i+1}',
                    armor=random.randint(1,20),
                    type=random.randint(1,20),
                    capacity=random.randint(1,20),
                )
                bd.execute(ins)

        def auto_engines(self, number):
            for i in range(number):
                ins = self.engines.insert().values(
                    engine=f'engine-{i+1}',
                    power=random.randint(1,20),
                    type=random.randint(1,20)
                )
                bd.execute(ins)

        def auto_ship(self, number):
            from sqlalchemy import select
            from itertools import chain
            import random

            weapon = bd.execute(select([weapons.c.weapon])).fetchall()
            hull = bd.execute(select([hulls.c.hull])).fetchall()
            engine = bd.execute(select([engines.c.engine])).fetchall()

            for i in range(number):
                ins = self.ship.insert().values(
                    ship=f'ship-{i+1}',
                    weapon=str(*chain(*random.sample(weapon, 1))),
                    hull=str(*chain(*random.sample(hull, 1))),
                    engine=str(*chain(*random.sample(engine, 1))),
                )
                bd.execute(ins)

        def auto_all(self):
            self.auto_engines(6)
            self.auto_weapons(20)
            self.auto_hulls(5)
    return Ships()
