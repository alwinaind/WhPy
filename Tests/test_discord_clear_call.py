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


def test_():
    """
    Scenario:
        When
        Then
    """
    pass
