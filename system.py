class RoadIA_System:
    def __init__(self):
        self.vehicles = []
        self.road_devices = []
        self.intersections = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_road_device(self, device):
        self.road_devices.append(device)

    def add_intersection(self, intersection):
        self.intersections.append(intersection)

    def update_system(self):
        for vehicle in self.vehicles:
            for device in self.road_devices:
                device.communicate_speed(vehicle)
            vehicle.maintain_distance()
            for inter in self.intersections:
                inter.suggest_direction(vehicle)
            vehicle.move()