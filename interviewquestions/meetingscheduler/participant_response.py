from enum import Enum


class ParticipantResponse(Enum):
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    TENTATIVE = "TENTATIVE"
    NOT_RESPONDED = "NOT_RESPONDED"
