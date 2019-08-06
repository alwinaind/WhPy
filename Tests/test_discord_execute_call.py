from dotenv import load_dotenv
import os
import pytest
from WhPy import discord

# Load Environment Variables
load_dotenv("./env/.env")

# Test Variables
channel_id = os.getenv("WEBHOOK_CHANNEL_ID")
token = os.getenv("WEBHOOK_TOKEN")
url = os.getenv("WEBHOOK_URL")

# Specific Variables
content = "This is a test message"
username = "MichaelCduBois"
avatar_url = "https://www.python.org/static/community_logos/"\
    "python-powered-h-140x182.png"


def test_wait():
    """
    Scenario: Webhook.execute() is called with wait=True
        When Webhook.execute() is called with wait=True
        Then WhPy should get JSON data by adding query parameter 'wait=true'
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message(content=content)

    response = hook.execute(wait=True)

    assert response.status_code == 200
    assert response.json()


def test_message_not_called():
    """
    Scenario: Webhook.execute() is called without calling Webhook.message()
        When Webhook.execute() is called without calling Webhook.message()
        Then WhPy should alert the developer to a missing required argument
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    with pytest.raises(TypeError) as exception_info:

        hook.execute()

    assert "Missing required arguments:" in str(exception_info.value)


def test_message_call_empty():
    """
    Scenario: Webhook.execute() is called with a blank Webhook.message() call
        When Webhook.execute() is called with a blank Webhook.message() call
        Then WhPy should alert the developer to a missing required argument
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message()

    with pytest.raises(TypeError) as exception_info:

        hook.execute()

    assert "Missing required arguments:" in str(exception_info.value)


def test_message_data():
    """
    Scenario: Webhook.execute() is called with Webhook.message() populated
        When Webhook.execute() is called with Webhook.message() populated
        Then WhPy should execute the message with stored values
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message(
        content=content,
        username=username,
        avatar_url=avatar_url,
        tts=True
    )

    response = hook.execute(wait=True)

    print(response.json())

    assert response.json()["content"] == content
    assert response.json()["author"]["username"] == username
    assert response.json()["author"]["avatar"] is not None
    assert response.json()["tts"] is True
