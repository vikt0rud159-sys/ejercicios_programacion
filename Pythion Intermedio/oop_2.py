class Bus:
	max_passengers = 3
	persons_in_bus = []
	def add_passenger(self, person):
		if len(self.persons_in_bus) >= self.max_passengers:
			print("\nAutobús lleno")
			return
		self.persons_in_bus.append(person)
	def subtract_person(self):
		self.persons_in_bus.pop(0)


bus1 = Bus()
bus1.add_passenger("Jose")
bus1.add_passenger("Pablo")
bus1.subtract_person()
bus1.add_passenger("Lola")


print(f"\n{bus1.persons_in_bus}\n")