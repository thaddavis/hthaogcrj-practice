import requests
import os

def send_email():
    print("Sending email...")
    requests.post(
      "https://api.mailgun.net/v3/sandboxd7c358e02f26415dbb7329dd994a8334.mailgun.org/messages",
      auth=("api", os.getenv("MAILGUN_API_KEY")),
      data={"from": "Wishbliss A.I. News Reporter <noreply@mail.wishbliss.link>",
        "to": ["tad@cmdlabs.io"],
        "subject": "Hello",
        "text": "Testing !!! some !!! weirdness"}
    )
