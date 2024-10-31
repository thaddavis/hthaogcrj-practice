# BONUS SECTION: As promised, here’s how you can easily tear down the GCP project and avoid incurring charges.

First undo what we’ve built up till this point…

ie:

- Delete the cron-job - `gcloud scheduler jobs delete cron-job-1 --location=us-east1`
- Delete the crj -`gcloud run jobs delete job-1 --region=us-east1 --project=$PROJECT_ID`
- Delete the Artifact Repository - `gcloud artifacts repositories delete repo-for-job-1 --location=us-east1 --project=$PROJECT_ID`
- & Delete the Secrets
```
gcloud secrets delete AGENTOPS_API_KEY --project=$PROJECT_ID
gcloud secrets delete AI_NEWS_RECIPIENTS --project=$PROJECT_ID
gcloud secrets delete MAILGUN_API_KEY --project=$PROJECT_ID
gcloud secrets delete OPENAI_API_KEY --project=$PROJECT_ID
```

After then deleting the resources we’ve provisioned, shut down the project on the Project Dashboard > Project Settings page to mark any stray resources for deletion after 30 days.

I recommend tearing down the project, unless you plan on continuing to develop this application further at which point you’re on your own. PEACE.