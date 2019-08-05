import pytest
from WhPy import discord


def test_import():
    """
    Ensures discord module is imported
    """
    assert discord.Webhook, "Could not import discord.webhook"
