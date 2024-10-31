# PART 8 - Adding AgentOps

The process of integrating with AgentOps is very similar to the process of integrating with OpenAI’s platform

First we come over to https://app.agentops.ai/ and sign up if we haven’t already

Then we have to find the page where we can provision API keys

I found it by opening the “Profile” dropdown and selecting the “API keys” option

And you should see a default API key that you can copy

And let’s add it into our .env file by writing on a new line in all caps `AGENTOPS_API_KEY=

After we have that sorted out we have to install the “agentops===0.3.14” package from pypi.org

And then import initialize the agentops tracker like so…

```
import agentops
agentops.init(os.getenv("AGENTOPS_API_KEY"))
```

Make sure to add it to the top of the main.py file so tracking is setup before our Agents get to work

And if we run our script we should see some feedback from AgentOps in the console

- Showcase the AgentOps dashboard

So to enable AgentOps in GCP aka our Production Environment we have to add the API key as another secret in “Secret Manager”

```
echo "YOUR_NEW_SECRET_VALUE" | gcloud secrets create AGENTOPS_API_KEY --data-file=-
gcloud secrets add-iam-policy-binding AGENTOPS_API_KEY \
  --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

--set-secrets “AGENTOPS_API_KEY=projects/${{ env.PROJECT_NUMBER }}/secrets/AGENTOPS_API_KEY:latest” \

gcloud run jobs execute job-1 --region us-east1

NOTE TO SELF: After AgentOps is showing the session running in GCP

Alright! Now let’s move on to the final section!