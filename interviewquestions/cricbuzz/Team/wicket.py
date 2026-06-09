from .wicket_type import WicketType


class Wicket:

    def __init__(self, wicket_type: WicketType, taken_by, over_detail, ball_detail):
        self.wicket_type = wicket_type
        self.taken_by = taken_by
        self.over_detail = over_detail
        self.ball_detail = ball_detail
