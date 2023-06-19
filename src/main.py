import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_token = os.environ.get("MEDIUM_API_TOKEN")


# Get medium user info from api
def get_user_info():
    """
    Get user details from Medium API

    Returns:
         user_detail
    """
    my_details = requests.get(
        url=f"https://api.medium.com/v1/me?accessToken={api_token}",
        timeout=10
    ).json()

    return my_details

def post_article(contents, state="draft"):
    """
    Post article on Medium API

    Args:
        contents: Markdown formatted content to be published onto medium.
        state: The state of the article, defaults to draft.

    Returns:
        True if successful
    """
    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    article_metadata = {
        "title": "Hello World",
        "contentFormat": "markdown",
        "content": "# Hello World\nSome example text",
        "tags": ["helloworld", "testing"],
        "publishStatus": state
    }

    response = requests.post(
        url=f'https://api.medium.com/v1/users/{get_user_info()["data"]["id"]}/posts',
        headers=headers,
        timeout=10,
        data=article_metadata
    )

    print(response.json())

    return True

post_article(article_contents)