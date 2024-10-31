# PART 6 - Add Mailgun

Next up we’ll integrate email into our application…

There are many email providers we could use but for demonstration purpose we will go with Mailgun…

- https://signup.mailgun.com/new/signup
- And after signing up you’ll have to verify your account via an Authorization Code that you’ll receive in either your inbox or on your phone…
- After you complete this account verification process, you can then provision an API key
    - This API key is what will authenticate our application with Mailgun’s Email API
- We can store this API key in the .env file by adding an entry that reads MAILGUN_API_KEY=<API_KEY_HERE>
- And now let’s add some code for testing that we can indeed send emails from our application
- If we come over to the domains page of the Mailgun console (https://app.mailgun.com/mg/sending/domains), we can see that Mailgun provides us with a free domain for testing…
- We will be able to send emails FROM this domain TO any email we list as an authorized recipient here…
- To authorize a recipient, we enter and submit an email address using this form AND will need the owner of the address to accept an invitation they’ll receive in their INBOX
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
- Out of courtesy of time tho let’s comment out most of our code and just test that emailing with Mailgun works…
- python main.py
- If you don’t mind finishing this walkthrough with emails being delivered to SPAM then skip ahead to PART 7
- BUT if you’d like the emails to be delivered to people’s INBOX as expected, here are the steps you’ll need to take…
    - Come over to the https://app.mailgun.com/mg/sending/domains page again and click “Add new domain”
    - Then specify the subdomain of some domain you own for example I used the name mail.wishbliss.link (where my domain is wishbliss.link)
    - After you add your domain you’ll be presented with a list of records that you’ll need to add to your domain’s DNS settings through your DNS provider
    - Here is what adding these Mailgun records to my DNS settings in AWS Route 53 looks like for reference
    - And after these records are added to our DNS we can click `Verify` to have Mailgun confirm that we’re indeed the owner of this domain
    - And now, when we send emails from our verified domain with Mailgun, the emails should land in our INBOX as expected
        - ie: noreply@wishbliss.link

If you have issues purchasing a domain or verifying it with your email provider, leave a comment or paste detailed descriptions of your issues into either Google or ChatGPT. If you’ve gotten this far, don’t be discouraged. Setting up emailing for a custom domain is not too difficult but can be a little bit tricky depending on the details of your setup. If someone in the audience knows of a simpler way to implement email integrations please leave a comment and I’ll pin it to the top of the comments.

Let’s move on to PART 7
