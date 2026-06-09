from abc import ABC, abstractmethod


class ScoreUpdaterObserver(ABC):

    @abstractmethod
    def update(self, ball_details) -> None:
        pass
