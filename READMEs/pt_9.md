# PART 9 - Wrapping things up

To wrap things up, let’s do 3 things

First let’s update our agents to focus on a different niche so you understand how to customize this application for your own purposes

Second, let’s re-enable the CRON job and adjust the CRON expression to trigger our Agents on a regular interval…

And Third let’s make the list of email recipients a secret so we don’t dox whoever is receiving these reports…

```
echo “tad@cmdlabs.io” | gcloud secrets create AI_NEWS_RECIPIENTS --data-file=-
gcloud secrets add-iam-policy-binding AI_NEWS_RECIPIENTS \
  --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

--set-secrets “AI_NEWS_RECIPIENTS=projects/${{ env.PROJECT_NUMBER }}/secrets/AI_NEWS_RECIPIENTS:latest” \

gcloud run jobs execute first-job-ever --region us-east1

And that’s all folks. We now have a team of A.I. News Reporters synthesizing information for us across a number of sources.

In conclusion, this entire video can be summed up in 3 words: Welcome to PRODUCTION!
