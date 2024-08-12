from duration import Duration
from utils import get_current_time


class Enemy:
    def __init__(self,
                 name: str,
                 max_health: int,
                 can_heal: bool = False):
        self.name: str = name
        self.max_health: int = max_health
        self.current_health: int = max_health
        self.can_heal: bool = can_heal
        self.start_combat_time: float = get_current_time()
        self.end_combat_time: float | None = None

    def progress(self, new_health: int):
        if new_health == 0:
            end_combat_time: float = get_current_time()
            self.end_combat_time: float = end_combat_time

        if new_health >= self.current_health or self.can_heal:
            print("Problem...")

    def combat_duration(self) -> Duration:
        if self.end_combat_time is None:
            raise ValueError("Could not calculate combat duration.")
        combat_duration: Duration = Duration.from_seconds(self.end_combat_time - self.start_combat_time)
        return combat_duration

    def save_encounter(self) -> None:
        combat_duration: Duration = self.combat_duration()
        encounter: dict[str, str | Duration] = {'name': self.name,
                                                'combat_duration': combat_duration}
        # TODO: Dump to file
