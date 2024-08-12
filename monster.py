from typing import Any

from duration import Duration
from settings import get_settings


class Monster:
    def __init__(self,
                 monster_name: str,
                 kill_value: float | None = None) -> None:
        self.monster_name: str = monster_name
        self.kill_value: float | None = kill_value

    def __str__(self) -> str:
        string: str = str(self.__dict__)
        return string

    def export_to_file(self) -> None:
        file_name: str = get_settings('monster_file_name', 'str')
        with open(file_name, 'a') as file:
            file.writelines(f"{self.monster_name},{self.kill_value}\n")

    @staticmethod
    def import_from_file() -> dict[str, Any]:
        file_name: str = get_settings('monster_file_name', 'str')
        monster_dictionary: dict[str, Any] = {}
        with open(file_name, 'r') as file:
            data: list[str] = file.read().splitlines()
        for datum in data:
            split_string: list[str] = datum.split(',')
            monster_dictionary.update({split_string[0]: split_string[1:]})
        return monster_dictionary

    @staticmethod
    def monster_names() -> list[str]:
        monster_dictionary: dict[str, Any] = Monster.import_from_file()
        monster_names: list[str] = [*monster_dictionary.keys()]
        return monster_names

    def damage_per_second(self, time_to_kill: Duration) -> float:
        pass

    def kills_per_hour(self, time_to_kill: Duration, idle_time: Duration) -> float:
        pass

    def theoretical_kills_per_hour(self, time_to_kill: Duration) -> float:
        pass

    def hourly_profit(self, time_to_kill: Duration) -> float:
        pass
