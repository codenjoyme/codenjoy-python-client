## Mandatory steps

- copy and paste your game token (browserUrl)
```python

def main():
    ...    
    url = "http://localhost:8080/codenjoy-contest/board/player/0?code=000000000000"
    ...
```

- define the desirable type of game
```python
def main():
    ...
    game = "bomberman"
    ...
```

- implement your invincible solver algorithm
```python
class BombermanSolver:
    ...
    def next_step(self):
        # make your action
        return Direction('ACT').to_string()
```
