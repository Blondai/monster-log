def get_settings(setting_name: str, return_type: str) -> int | float | str:
    settings: dict[str, int | float | str] = import_file()
    for setting in settings:
        if setting == setting_name:
            return convert(settings[setting], return_type)
    else:
        raise ValueError(f"Setting {setting_name} not found in 'settings.ini'.")


# Probably add more return_types
def convert(setting_name: str, return_type: str) -> int | float | str:
    if return_type == 'int':
        return int(setting_name)
    elif return_type == 'float':
        return float(setting_name)
    elif return_type == 'str':
        return str(setting_name)
    else:
        raise NotImplementedError(f"Can't convert string to type '{return_type}'.")


def import_file() -> dict[str, str]:
    settings: dict[str, str] = {}
    with open('settings.ini', 'r') as file:
        data: list[str] = file.read().splitlines()
    for element in data:
        strings: list[str] = element.split('=')
        settings.update({strings[0]: strings[1]})
    return settings
