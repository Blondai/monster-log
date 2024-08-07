from duration import Duration


class Monster:
    def __init__(self,
                 monster_name: str,
                 hitpoints: int,
                 kill_value: float) -> None:
        self.monster_name: str = monster_name
        self.hitpoints: int = hitpoints
        self.kill_value: float = kill_value

    def __str__(self) -> str:
        string: str = str(self.__dict__)
        return string

    def export_to_file(self, file_name: str) -> None:
        pass

    @staticmethod
    def import_from_file(file_name: str, monster_name: str) -> Monster:
        pass

    def damage_per_second(self, time_to_kill: Duration) -> float:
        pass

    def kills_per_hour(self, time_to_kill: Duration, idle_time: Duration) -> float:
        pass

    def theoretical_kills_per_hour(self, time_to_kill: Duration) -> float:
        pass

    def hourly_profit(self, time_to_kill: Duration) -> float:
        pass
