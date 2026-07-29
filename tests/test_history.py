from src.history import ConversationHistory


def test_history_starts_empty():
    history = ConversationHistory()

    assert history.size() == 0


def test_add_user_message():
    history = ConversationHistory()

    history.add_user_message("Hello")

    assert history.size() == 1


def test_clear_history():
    history = ConversationHistory()

    history.add_user_message("Hello")
    history.clear()

    assert history.size() == 0

def test_history_preserves_order():
    history = ConversationHistory()

    history.add_user_message("Hello")
    history.add_assistant_message("Hi!")

    messages = history.messages()

    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"