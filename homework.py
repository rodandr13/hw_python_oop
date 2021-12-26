class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance: float = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self, distance: float, time: float) -> float:
        """Получить среднюю скорость движения."""
        average_speed: float = self.get_distance() / self.duration
        return average_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return self


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        coeff_calorie_1: int = 18
        coeff_calorie_2: int = 20
        calories: float = ((coeff_calorie_1
                           * self.get_mean_speed - coeff_calorie_2)
                           * self.weight / self.M_IN_KM * self.duration)
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        coeff_calorie_1: int = 0.035
        coeff_calorie_2: int = 0.29
        calories: float = (coeff_calorie_1 * weight
                           + (self.get_mean_speed() ** 2 // height)
                           * coeff_calorie_2 * weight) * duration
        return calories


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
