from engine import state, handler


class GameState(state.State):
    def __init__(self):
        """Constructor for GameState"""
        super().__init__()
        self.set_handler(handler.Handler())

