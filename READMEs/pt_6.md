# Next up we’ll integrate email into our application…

There are many email providers we could use but for demonstration purpose we will go with Mailgun…

- https://signup.mailgun.com/new/signup
- After signing up you’ll have to verify your email and/or phone number with Mailgun via an Authorization Code that you’ll receive in either your inbox or on your phone…
- After you complete this account verification process, you can then provision an API key
    - This API key is what will authenticate our application with Mailgun’s Email API
- We can store this API key in the .env file
    - Let’s add an entry that reads MAILGUN_API_KEY=<API_KEY_HERE>
- And now let’s add some code for testing that we can send emails from our application
- If we come over to https://app.mailgun.com/mg/sending/domains, we can see that Mailgun provides us with a free domain to test with…
- We will be able to send emails FROM this domain TO any email we list as authorized recipients here…
- To authorize a recipient, we enter and submit its address with this form AND have the owner accept the invitation that they’ll receive via email
- After we authorize some email we own (by own I mean we have access to its inbox), let’s add the following code to our application…

	
    - touch helpers/send_email.py
```
import requests
import os

def send_email():
    print("Sending email...")
    requests.post(
      "https://api.mailgun.net/v3/sandboxd7c358e02f26415dbb7329dd994a8334.mailgun.org/messages",
      auth=("api", os.getenv("MAILGUN_API_KEY")),
      data={"from": "Wishbliss Mailing List <mailgun@sandboxd7c358e02f26415dbb7329dd994a8334.mailgun.org>",
        "to": ["tad@cmdlabs.io"],
        "subject": "Hello",
        "text": "Testing !!! some !!! weirdness"})
```

    - main.py
```
send_email()
```

- After adding this code, we can test our script again and we should receive an email in our SPAM folder
- Out of courtesy of the time let’s comment out and just test that the email API works…
- python main.py
- If you don’t mind finishing this walkthrough with emails being delivered to SPAM then skip ahead to PART 7
- BUT if you’d like the emails to be delivered to INBOX proper, here are the steps you’ll need to take…
    - Come over to the https://app.mailgun.com/mg/sending/domains page again and click “Add new domain”
    - Then specify the subdomain of some domain you own for example I used the name mail.wishbliss.link (where my domain is wishbliss.link)
    - After you add you domain you’ll be presented with a list of records that you’ll need to add to your domain’s DNS settings through your DNS provider
    - Here is what adding these records to my DNS settings in AWS Route 53 looks like for me reference
    - And after this records are added to our DNS we can click `Verify` to have Mailgun confirm that we are indeed the owner of this domain
    - And now when we send email with an email from our verified domain as the send the emails should land in our INBOX proper
        - noreply@wishbliss.link

If you have issues purchasing a domain or verifying it with your email provider, leave a comment or paste detailed descriptions of your issues into either Google or ChatGPT. If you’ve gotten this far, don’t be discouraged. Setting up emailing from a custom domain is not too difficult but can be tricky if you do something slightly off.

SIDENOTE: If someone in the audience knows of a simpler way to implement email integrations please leave a comment and I’ll pin it to the top of the comments