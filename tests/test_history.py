from services.history_service import HistoryService


def test_save():

    HistoryService.save("2+2",4)

    history = HistoryService.get_all()

    assert len(history) >= 1