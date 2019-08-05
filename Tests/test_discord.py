from dotenv import load_dotenv
import os
import pytest
from WhPy import discord

load_dotenv("./env/.env")

url = os.getenv("WEBHOOK_URL")
channel_id = os.getenv("WEBHOOK_CHANNEL_ID")
token = os.getenv("WEBHOOK_TOKEN")

bad_channel_id = 404
bad_token = "BADTOKEN"

str_msg = "Test Message"
int_msg = 12345

str_username = "MichaelCduBois"
int_username = 208

str_avatar_url = "https://www.python.org/static/community_logos/"\
    "python-powered-h-140x182.png"
int_avatar_url = 67890


def test_import():
    """
    Tests the import of the discord class
    """
    assert discord, "discord not imported"
    assert discord.Webhook, "Webhook not imported"


def test_blank_arguments():
    """
    Tests blank webhook arguments raises TypeError
    """
    with pytest.raises(TypeError) as exception_info:

        d = discord.Webhook()

    assert "Missing required arguments" in str(exception_info.value)


def test_blank_channel_id():
    """
    Tests blank webhook channel_id argument raises TypeError
    """
    with pytest.raises(TypeError) as exception_info:

        d = discord.Webhook(token=token)

    assert "Missing required arguments" in str(exception_info.value)


def test_blank_token():
    """
    Tests blank webhook channel_id argument raises TypeError
    """
    with pytest.raises(TypeError) as exception_info:

        d = discord.Webhook(channel_id=channel_id)

    assert "Missing required arguments" in str(exception_info.value)


def test_invalid_channel_id():
    """
    Tests an invalid webhook token raises ValueError
    """
    with pytest.raises(ValueError) as exception_info:

        d = discord.Webhook(channel_id=bad_channel_id, token=token)

    assert "Unknown Webhook" in str(exception_info.value)


def test_invalid_webhook_token():
    """
    Tests an invalid webhook token raises ValueError
    """
    with pytest.raises(ValueError) as exception_info:

        d = discord.Webhook(channel_id=channel_id, token=bad_token)

    assert "Invalid Webhook Token" in str(exception_info.value)


def test_webhook_arguments():
    """
    Tests webhook arguments
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    # Argument channel_id Testing
    assert d.channel_id is not None, "The argument channel_id should be set"
    assert type(d.channel_id) is str, "The argument channel_id should be str"
    assert d.channel_id == str(channel_id),\
        "The argument channel_id should be { channel_id }"

    # Argument token Testing
    assert d.token is not None, "The argument token should be set"
    assert type(d.token) is str, "The argument token should be str"
    assert d.token == str(token), "The argument token should be { token }"


def test_webhook_url():
    """
    Tests url argument is correctly decoded to channel_id and token
    """
    d = discord.Webhook(url=url)

    # Argument channel_id Testing
    assert d.channel_id is not None, "The argument channel_id should be set"
    assert type(d.channel_id) is str, "The argument channel_id should be str"
    assert d.channel_id == str(channel_id),\
        "The argument channel_id should be { channel_id }"

    # Argument token Testing
    assert d.token is not None, "The argument token should be set"
    assert type(d.token) is str, "The argument token should be str"
    assert d.token == str(token), "The argument token should be { token }"


def test_empty_message():
    """
    Ensures Discord message is not set on empty message call
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message()
    assert not d.content, "The argument content should be None"


def test_string_message_content():
    """
    Tests Discord message content sent as string
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(
        content=str_msg
    )
    assert d.content is not None, "The arument content should be set"
    assert type(d.content) is str, "The argument content should be str"


def test_integer_message_content():
    """
    Tests Discord message content sent as integer is converted to a string
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(
        content=int_msg
    )
    assert d.content is not None, "The arument content should be set"
    assert type(d.content) is str, "The argument content should be str"


def test_empty_username():
    """
    Ensures Discord username is not set on empty message call
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message()
    assert not d.content, "The argument content should be None"


def test_string_username():
    """
    Tests Discord username sent as string
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(
        username=str_username
    )
    assert d.username is not None, "The arument username should be set"
    assert type(d.username) is str, "The argument username should be str"


def test_integer_username():
    """
    Tests Discord username sent as integer is converted to a string
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(
        username=int_username
    )
    assert d.username is not None, "The arument username should be set"
    assert type(d.username) is str, "The argument username should be str"


def test_empty_avatar_url():
    """
    Ensures Discord avatar_url is not set on empty message call
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message()
    assert not d.avatar_url, "The argument avatar_url should be None"


def test_string_avatar_url():
    """
    Tests Discord avatar_url sent as string
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(
        avatar_url=str_avatar_url
    )
    assert d.avatar_url is not None, "The arument avatar_url should be set"
    assert type(d.avatar_url) is str, "The argument avatar_url should be str"


def test_integer_avatar_url():
    """
    Tests Discord avatar_url sent as integer is converted to a string
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(
        avatar_url=int_avatar_url
    )
    assert d.avatar_url is not None, "The arument avatar_url should be set"
    assert type(d.avatar_url) is str, "The argument avatar_url should be str"


def test_message_tts():
    """
    Tests Discord TTS option
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(content=str_msg, tts=True)

    hook = d.execute(wait=True)

    assert hook.status_code == 200
    assert hook.json()["tts"] is True


def test_empty_execute_before_message():
    """
    Tests an empty execute call before message call returns TypeError
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    with pytest.raises(TypeError) as exception_info:

        d.execute()

    assert "Missing required argument: 'content'" in str(exception_info.value)


def test_empty_execute_and_message():
    """
    Tests an empty execute cann with an empty message call returns TypeError
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message()

    with pytest.raises(TypeError) as exception_info:

        d.execute()

    assert "Missing required argument: 'content'" in str(exception_info.value)


def test_execute_content():
    """
    Test that execute works with content flag
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(content=str_msg)

    assert d.execute().status_code == 204


def test_execute_wait():
    """
    Test that execute(wait=True) returns JSON
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(content=str_msg)

    hook = d.execute(wait=True)

    assert hook.status_code == 200
    assert hook.json()["content"] == str_msg


def test_execute_username():
    """
    Test that execute overrides username
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(content=str_msg, username=str_username)

    assert d.execute().status_code == 204


def test_execute_avatar_url():
    """
    Test that execute overrides avatar_url
    """
    d = discord.Webhook(channel_id=channel_id, token=token)

    d.message(content=str_msg, avatar_url=str_avatar_url)

    assert d.execute().status_code == 204
