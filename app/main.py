class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        count = 0
        for car in cars:
            count += self.wash_single_car(car)

        return count

    def calculate_washing_price(self, car: Car) -> float:
        cost_wash = round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center, 2
        )
        return cost_wash

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            cost_wash_single_car = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return cost_wash_single_car
        return 0

    def rate_service(self, rating: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
