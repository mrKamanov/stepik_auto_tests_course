import os
import json
import pytest

@pytest.fixture(scope="session")
def load_config():
    # Определяем путь к config.json относительно conftest.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, 'config.json')

    # Проверяем существование файла
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")

    # Загружаем данные из config.json
    with open(config_path, 'r') as config_file:
        config_data = json.load(config_file)
    return config_data