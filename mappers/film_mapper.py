import json
from pathlib import Path
from typing import List
from models.film import Film
      
def load_films_from_json(json_path: str) -> List[Film]:
    data = json.loads(Path(json_path).read_text(encoding="utf-8"))
    return [Film(name=item["name"], genre=item["genre"], year=int(item["year"])) for item in data]