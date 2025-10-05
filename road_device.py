class RoadDevice:
    def __init__(self, road_name, speed_limit, start=0, end=100):
        self.road_name = road_name
        self.speed_limit = speed_limit
        self.start = start
        self.end = end

    def communicate_speed(self, vehicle):
        if self.start <= vehicle.position <= self.end:
            vehicle.set_road_speed(self.speed_limit)