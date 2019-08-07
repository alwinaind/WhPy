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


def test_after_init():
    """
    Scenario: Webhook.clear is called before Webhook.message
        When Webhook.clear is called before Webhook.message
        Then Webhook.clear should ignore channel_id & token Instance Variables
        Then Webhook.clear should set the tts Instance Variable to False
        Then Webhook.clear should set the embeds Instance Variable to []
        Then Webhook.clear should set all other Instance Variables to None
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.clear()

    assert hook.channel_id is not None
    assert hook.token is not None
    assert hook.tts is False
    assert hook.content is None
    assert hook.username is None
    assert hook.avatar_url is None
    assert len(hook.embeds) == 0


def test_after_message():
    """
    Scenario: Webhook.clear is called after Webhook.message
        When Webhook.clear is called after Webhook.message
        Then Webhook.clear should ignore channel_id & token Instance Variables
        Then Webhook.clear should set the tts Instance Variable to False
        Then Webhook.clear should set the embeds Instance Variable to []
        Then Webhook.clear should set all other Instance Variables to None
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.message(
        content=content,
        username=username,
        avatar_url=avatar_url,
        tts=True
    )

    hook.clear()

    assert hook.channel_id is not None
    assert hook.token is not None
    assert hook.tts is False
    assert hook.content is None
    assert hook.username is None
    assert hook.avatar_url is None
    assert len(hook.embeds) == 0


def test_after_one_embed():
    """
    Scenario: Webhook.clear is called after Webhook.embed
        When Webhook.clear is called after Webhook.embed
        Then Webhook.clear should ignore channel_id & token Instance Variables
        Then Webhook.clear should set the tts Instance Variable to False
        Then Webhook.clear should set the embeds Instance Variable to []
        Then Webhook.clear should set all other Instance Variables to None
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.embed(
        title="test_after_one_embed",
        description=content,
        url=avatar_url,
        color="ff8800"
    )

    hook.clear()

    assert hook.channel_id is not None
    assert hook.token is not None
    assert hook.tts is False
    assert hook.content is None
    assert hook.username is None
    assert hook.avatar_url is None
    assert len(hook.embeds) == 0


def test_after_multiple_embed():
    """
    Scenario: Webhook.clear is called after multiple Webhook.embed
        When Webhook.clear is called after multiple Webhook.embed
        Then Webhook.clear should ignore channel_id & token Instance Variables
        Then Webhook.clear should set the tts Instance Variable to False
        Then Webhook.clear should set the embeds Instance Variable to []
        Then Webhook.clear should set all other Instance Variables to None
    """
    hook = discord.Webhook(channel_id=channel_id, token=token)

    hook.embed(
        title="test_after_multiple_embed_1",
        description=content,
        url=avatar_url,
        color="ff8800"
    )

    hook.embed(
        title="test_after_multiple_embed_2",
        description=content,
        url=avatar_url,
        color="88ff00"
    )

    hook.clear()

    assert hook.channel_id is not None
    assert hook.token is not None
    assert hook.tts is False
    assert hook.content is None
    assert hook.username is None
    assert hook.avatar_url is None
    assert len(hook.embeds) == 0
