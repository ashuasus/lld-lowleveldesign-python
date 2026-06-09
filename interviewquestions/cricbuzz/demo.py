from collections import deque
from .Team.Player.person import Person
from .Team.Player.player_details import PlayerDetails
from .Team.Player.player_type import PlayerType
from .Team.team import Team
from .match import Match
from .t20_match import T20Match


class Demo:

    def main(self):
        team_a = self._add_team("India")
        team_b = self._add_team("SriLanka")

        match_type = T20Match()
        match = Match(team_a, team_b, None, "SMS STADIUM", match_type)
        match.start_match()

    def _add_team(self, name: str) -> Team:
        player_details_queue = deque()

        p1 = self._add_player(name + "1", PlayerType.ALLROUNDER)
        p2 = self._add_player(name + "2", PlayerType.ALLROUNDER)
        p3 = self._add_player(name + "3", PlayerType.ALLROUNDER)
        p4 = self._add_player(name + "4", PlayerType.ALLROUNDER)
        p5 = self._add_player(name + "5", PlayerType.ALLROUNDER)
        p6 = self._add_player(name + "6", PlayerType.ALLROUNDER)
        p7 = self._add_player(name + "7", PlayerType.ALLROUNDER)
        p8 = self._add_player(name + "8", PlayerType.ALLROUNDER)
        p9 = self._add_player(name + "9", PlayerType.ALLROUNDER)
        p10 = self._add_player(name + "10", PlayerType.ALLROUNDER)
        p11 = self._add_player(name + "11", PlayerType.ALLROUNDER)

        player_details_queue.append(p1)
        player_details_queue.append(p2)
        player_details_queue.append(p3)
        player_details_queue.append(p4)
        player_details_queue.append(p5)
        player_details_queue.append(p6)
        player_details_queue.append(p7)
        player_details_queue.append(p8)
        player_details_queue.append(p9)
        player_details_queue.append(p10)
        player_details_queue.append(p11)

        bowlers = [p8, p9, p10, p11]

        team = Team(name, player_details_queue, [], bowlers)
        return team

    def _add_player(self, name: str, player_type: PlayerType) -> PlayerDetails:
        person = Person()
        person.name = name
        player_details = PlayerDetails(person, player_type)
        return player_details


if __name__ == "__main__":
    demo_obj = Demo()
    demo_obj.main()
