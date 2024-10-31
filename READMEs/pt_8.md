# PART 8 - Adding AgentOps

The process of integrating with AgentOps is very similar to the process of integrating with OpenAI’s platform

First come over to https://app.agentops.ai/ and sign up if we haven’t already

Then find the page for provisioning API keys

I found it by opening the “Profile” dropdown and selecting the “API keys” option

And you should see a default API key that you can copy

Let’s add it to our project by adding a new line in our .env file that reads in all caps `AGENTOPS_API_KEY=`

Then we have to install the “agentops===0.3.14” package from pypi.org

And then initialize the agentops tracker in the main.py like so…

```
import agentops
agentops.init(os.getenv("AGENTOPS_API_KEY"))
```

Make sure to add it at the top of the main.py file so tracking is setup before our Agents get to work

If we now run our application script, we should start to see some info in the AgentOps console…

- Showcase the AgentOps dashboard

Now let’s set up AgentOps in GCP aka in our Production Environment.

This process will be very similar to how we setup the 

We have to add the AGENTOPS_API_KEY as secret in “Secret Manager”

```
echo "YOUR_NEW_SECRET_VALUE" | gcloud secrets create AGENTOPS_API_KEY --data-file=-
```

And give our Defaul Compute Service Account permissions to access it

```
gcloud secrets add-iam-policy-binding AGENTOPS_API_KEY \
  --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

And then reference in the “—set-secrets” flag of our CICD script like so…

--set-secrets “AGENTOPS_API_KEY=projects/${{ env.PROJECT_NUMBER }}/secrets/AGENTOPS_API_KEY:latest” \

When we trigger our job in GCP we should still be seeing data being fed in from our Agents running in GCP…

gcloud run jobs execute first-job-ever --region us-east1

NOTE TO SELF: After AgentOps is showing the session running in GCP

After confirming that’s working, let’s move on to the final section!
