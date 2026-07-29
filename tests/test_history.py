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

def test_reset_clears_history():
    history = ConversationHistory()

    history.add_user_message("Hello")
    history.add_assistant_message("Hi")

    history.clear()

    assert history.size() == 0
    assert history.is_empty()

def test_formatted_history():
    history = ConversationHistory()

    history.add_user_message("Hello")
    history.add_assistant_message("Hi!")

    output = history.formatted_history()

    assert "Hello" in output
    assert "Hi!" in output

def test_context_window():

    history = ConversationHistory()

    for i in range(30):

        history.add_user_message(f"Question {i}")

        history.add_assistant_message(f"Answer {i}")

    context = history.context()

    assert len(context) == 20

    assert context[0]["content"][0]["text"] == "Question 20"