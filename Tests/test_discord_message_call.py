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

content = [
    "This is a string message",
    12345
]

username = [
    "MichaelCduBois",
    123456
]

avatar_url = [
    "https://www.python.org/static/community_logos/"
    "python-powered-h-140x182.png",
    1234567
]


def test_content_empty():
    """
    Scenario: Webhook.message() is called without content argument set
        When Webhook.message() is called without content argument set
        Then WhPy should set content to None
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message()

    assert not hook.content


@pytest.mark.parametrize("content", content)
def test_content_stored_as_string(content):
    """
    Scenario: Webhook.message() is called with content argument set
        When Webhook.message() is called with content argument set
        Then Webhook.message() should store content as a string
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message(content=content)

    assert hook.content is not None
    assert type(hook.content) is str
    assert hook.content == str(content)


def test_username_empty():
    """
    Scenario: Webhook.message() is called without username argument set
    When Webhook.message() is called without username argument set
    Then WhPy should set username to None
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message()

    assert not hook.username


@pytest.mark.parametrize("username", username)
def test_username_stored_as_string(username):
    """
    Scenario: Webhook.message() is called with username argument set
        When Webhook.message() is called with username argument set
        Then Webhook.message() should store username as a string
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message(username=username)

    assert hook.username is not None
    assert type(hook.username) is str
    assert hook.username == str(username)


def test_avatar_url_empty():
    """
    Scenario: Webhook.message() is called without avatar_url argument set
    When Webhook.message() is called without avatar_url argument set
    Then WhPy should set username to None
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message()

    assert not hook.avatar_url


@pytest.mark.parametrize("avatar_url", avatar_url)
def test_avatar_url_stored_as_string(avatar_url):
    """
    Scenario: Webhook.message() is called with avatar_url argument set
        When Webhook.message() is called with avatar_url argument set
        Then Webhook.message() should store avatar_url as a string
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message(avatar_url=avatar_url)

    assert hook.avatar_url is not None
    assert type(hook.avatar_url) is str
    assert hook.avatar_url == str(avatar_url)


def test_message_tts():
    """
    Scenario: Webhook.message() is called with the tts argument set as True
        When Webhook.message() is called with the tts argument set as True
        Then WhPy should store the tts flag as True
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message(content=content[0], tts=True)

    assert hook.tts is True
