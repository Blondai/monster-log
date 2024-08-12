class Duration:
    def __init__(self,
                 hours: int,
                 minutes: int,
                 seconds: float) -> None:
        self.hours: int = hours
        self.minutes: int = minutes
        self.seconds: float = seconds

    def __str__(self) -> str:
        dictionary: dict[str, int | float] = self.__dict__
        return str(dictionary)

    def __add__(self, other: 'Duration') -> 'Duration':
        combined_seconds: float = self.to_seconds() + other.to_seconds()
        new_duration: Duration = Duration.from_seconds(combined_seconds)
        return new_duration

    @staticmethod
    def from_seconds(seconds: float) -> 'Duration':
        new_hours: int = int(seconds) // 3600
        new_minutes: int = (int(seconds) % 3600) // 60
        new_seconds: float = seconds % 60
        duration: Duration = Duration(new_hours, new_minutes, new_seconds)
        return duration

    @staticmethod
    def from_ticks(ticks: float) -> 'Duration':
        seconds: float = ticks * 0.6
        duration: Duration = Duration.from_seconds(seconds)
        return duration

    @staticmethod
    def from_minutes(minutes: float) -> 'Duration':
        seconds: float = minutes * 60
        duration: Duration = Duration.from_seconds(seconds)
        return duration

    @staticmethod
    def from_hours(hours: float) -> 'Duration':
        seconds: float = hours * 3600
        duration: Duration = Duration.from_seconds(seconds)
        return duration

    def to_seconds(self) -> float:
        time_in_seconds: float = 0
        time_in_seconds += self.hours * 3600
        time_in_seconds += self.minutes * 60
        time_in_seconds += self.seconds
        return time_in_seconds

    def to_ticks(self) -> float:
        ticks: float = self.to_seconds() / 0.6
        return ticks

    def to_minutes(self) -> float:
        time_in_minutes: float = self.to_seconds() / 60
        return time_in_minutes

    def to_hours(self) -> float:
        time_in_hours: float = self.to_seconds() / 3600
        return time_in_hours
