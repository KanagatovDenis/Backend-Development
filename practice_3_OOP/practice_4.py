import random


class SpaceShip:
    FUEL_PER_UNIT_OF_DISTANCE = 0.5
    MAX_SPEED = 1000

    def __init__(self, name, fuel=100, hull=100):
        self.name = name
        self._fuel = fuel
        self._hull = hull
        self._speed = 0

    @property
    def fuel(self):
        return self._fuel

    def refuel(self, amount):
        self._fuel += amount

    @property
    def hull(self):
        return self._hull

    def take_damage(self, amount):
        self._hull = max(0, self._hull - amount)

    def repair(self, amount):
        self._hull = min(100, self._hull + amount)

    @property
    def speed(self):
        return self._speed

    def set_speed(self, value):
        self._speed = max(0, min(value, self.MAX_SPEED))

    def is_operational(self):
        return self._hull > 0

    def fly(self, distance):
        needed = distance * self.FUEL_PER_UNIT_OF_DISTANCE

        if needed > self._fuel:
            return False

        self._fuel -= needed

        return True

    def __str__(self):
        return (f"Корабль {self.name}, в баке {self._fuel:.1f} топлива, корпус  имеет {self._hull}% прочности, "
                f"скорость {self._speed} км/с")


class CrewMember:
    def __init__(self, name, role, skills=None, health=100):
        self.name = name
        self.role = role
        self.skills = skills or {}
        self._health = health

    @property
    def health(self):
        return self._health

    @property
    def is_alive(self):
        return self._health > 0

    def take_damage(self, amount):
        self._health = max(0, self._health - amount)

    def heal(self, amount):
        if self.is_alive:
            self._health = min(100, self._health + amount)

    def skill(self, name):
        return self.skills.get(name, 0)

    def __str__(self):
        status = f"Здоровье составляет {self._health}" if self.is_alive else "Погиб"

        return f"{self.name} ({self.role}): {status}"


class Mission:
    def __init__(self, goal, distance, fuel_required, legs=4, seed=None):
        self.goal = goal
        self.distance = distance
        self.fuel_required = fuel_required
        self.legs = legs
        self.events = [self._asteroid_field, self._engine_failure, None]
        self.log = []
        self.random = random.Random(seed)

    def _asteroid_field(self, ship, crew):
        pilots = [c for c in crew if c.role == "pilot" and c.is_alive]
        dodge = max((p.skill("piloting") for p in pilots), default=0)
        damage = max(5, 40 - dodge * 4)
        ship.take_damage(damage)
        self.log.append(f"Астероидное поле! Урон корпусу {damage}%")

    def _engine_failure(self, ship, crew):
        engineers = [c for c in crew if c.role == "engineer" and c.is_alive]

        if engineers:
            repair = max(e.skill("repair") for e in engineers) * 3
            ship.take_damage(10)
            ship.repair(repair)
            self.log.append(f"Авария двигателя, инженер починил: корпус починен на {repair}%")
        else:
            ship.take_damage(25)
            self.log.append("Авария двигателя, инженера нет! Урон корпусу 25%")

    def run(self, ship, crew):
        if ship.fuel < self.fuel_required:
            self.log.append("Недостаточно топлива для старта")

            return False

        if not any(c.role == "pilot" and c.is_alive for c in crew):
            self.log.append("Нет живого пилота")

            return False

        leg_distance = self.distance / self.legs
        ship.set_speed(500)

        for leg in range(1, self.legs + 1):
            if not ship.fly(leg_distance):
                self.log.append(f"Этап {leg}: закончилось топливо")

                return False

            event = self.random.choice(self.events)

            if event:
                event(ship, crew)
            else:
                self.log.append(f"Этап {leg}: полёт без происшествий")

            if not ship.is_operational():
                self.log.append("Корабль разрушен")

                return False

        ship.set_speed(0)
        self.log.append(f"Миссия «{self.goal}» выполнена!")

        return True


if __name__ == "__main__":
    ship = SpaceShip("Орион", fuel=120)
    crew = [
        CrewMember("Алексей", "pilot", {"piloting": 8}),
        CrewMember("Мария", "engineer", {"repair": 7}),
        CrewMember("Иван", "medic", {"medicine": 6}),
    ]
    mission = Mission("Полёт к Марсу", distance=100, fuel_required=50, seed=3)

    print(ship)
    for member in crew:
        print(member)

    success = mission.run(ship, crew)

    print("\nЖурнал миссии:")
    for entry in mission.log:
        print(" -", entry)
    print("\nУспех:", success)
    print(ship)
