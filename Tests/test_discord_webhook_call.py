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

# Invalid Test Variables
bad_channel_id = "1234"
bad_token = "567890"


def test_blank_call():
    """
    Scenario: discord.Webhook() is called without arguments
        When discord.Webhook() is called without arguments
        Then WhPy should alert the developer to missing required arguments
    """
    with pytest.raises(TypeError) as exception_info:

        hook = discord.Webhook()

    assert "Missing required arguments" in str(exception_info.value)


def test_channel_id_blank():
    """
    Scenario: discord.Webhook() is called without channel_id assigned
        When discord.Webhook() is called without the channel_id assigned
        Then WhPy should alert the developer to missing required arguments
    """
    with pytest.raises(TypeError) as exception_info:

        hook = discord.Webhook(token=token)

    assert "Missing required arguments" in str(exception_info.value)


def test_channel_id_invalid():
    """
    Scenario: discord.Webhook() is called with an invalid channel_id
        When discord.Webhook() is called with an invalid channel_id
        Then why should alert the developer to an unknown webhook
    """
    with pytest.raises(ValueError) as exception_info:

        hook = discord.Webhook(channel_id=bad_channel_id, token=token)

    assert "Unknown Webhook" in str(exception_info.value)


def test_channel_id_stored_as_string():
    """
    Scenario: discord.Webhook() is successfully called with channel_id & token
        When discord.Webhook() is successfully called with channel_id and token
        Then discord.Webhook() should store channel_id as a string
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    assert hook.channel_id is not None
    assert type(hook.channel_id) is str
    assert hook.channel_id == str(channel_id)


def test_token_blank():
    """
    Scenario: discord.Webhook() is called without token assigned
        When discord.Webhook() is called without the token assigned
        Then WhPy should alert the developer to missing required arguments
    """
    with pytest.raises(TypeError) as exception_info:

        hook = discord.Webhook(channel_id=channel_id)

    assert "Missing required arguments" in str(exception_info.value)


def test_token_invalid():
    """
    Scenario: discord.Webhook() is called with an invalid token
        When discord.Webhook() is called with an invalid token
        Then WhPy should alert the developer to an Invalid Webhook Token
    """
    with pytest.raises(ValueError) as exception_info:

        hook = discord.Webhook(channel_id=channel_id, token=bad_token)

    assert "Invalid Webhook Token" in str(exception_info.value)


def test_token_stored_as_string():
    """
    Scenario: discord.Webhook() is successfully called with channel_id & token
        When discord.Webhook() is successfully called with channel_id and token
        Then discord.Webhook() should store token as a string
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    assert hook.token is not None
    assert type(hook.token) is str
    assert hook.token == str(token)


def test_url_decodes():
    """
    Scenario: discord.Webhook() is successfully called with url
        When discord.Webhook() is successfully called with url
        Then discord.Webhook() will decode the url into channel_id and token
    """
    hook = discord.Webhook(url=url)

    assert hook.channel_id is not None
    assert hook.channel_id == url.split("/")[5]
    assert hook.token == url.split("/")[6]
