from pathlib import Path
import sys
sys.path.append(f"{Path(__file__).parent.parent.resolve()}/src")

from nbz2.core import Core
from nbz2.engine import Engine


class TestNBZ2():

    def test_go_to_google(self) -> None:
        GECKODRIVER_PATH: str = f"{Path(__file__).parent.parent.resolve()}/drivers/geckodriver"
        nbz2: Core = Core(Engine.firefox, GECKODRIVER_PATH)
        nbz2.go_to_url("https://google.es")
        assert nbz2.get_url_title() == "Google"
        nbz2.close()
