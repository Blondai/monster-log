from monster import Monster


class Text:
    def __init__(self, raw_text: str):
        self.text: list[str] = Text.convert(raw_text)

    @staticmethod
    def convert(raw_text: str) -> list[str]:
        split_text: list[str] = raw_text.split('\n')
        text: list[str] = Text.delete_empty(split_text)
        return text

    @staticmethod
    def delete_empty(split_text: list[str]) -> list[str]:
        text: list[str] = []
        for string in split_text:
            if string != '':
                text.append(string)
        return text

    def search_for_hitpoints(self) -> tuple[int, int]:
        try:
            for string in self.text:
                if '/' in string:
                    split_string: list[str] = string.split('/')
                    break
            assert len(split_string) == 2, f"Can't convert string '{split_string}' to hitpoints."
            current_hitpoints: int = int(split_string[0])
            max_hitpoints: int = int(split_string[1])
            return current_hitpoints, max_hitpoints
        except:
            return [None, None]

    def get_current_hitpoints(self) -> int:
        current_hitpoints, _ = self.search_for_hitpoints()
        return current_hitpoints

    def get_max_hitpoints(self) -> int:
        _, max_hitpoints = self.search_for_hitpoints()
        return max_hitpoints

    def search_for_name(self) -> str:
        # TODO: Implement correctly
        # monster_list: list[str] = Monster.monster_names()
        # for string in self.text:
        #     if string in monster_list:
        #         name: str = string
        #         break
        # return name
        try:
            return self.text[0]
        except:
            return None
