# PART 4 - Set up a cron job using Cloud Scheduler

https://console.cloud.google.com/marketplace/product/google/cloudscheduler.googleapis.com?project=hthaogcrj-practice

To use Cloud Scheduler we have to enable it in our project by entering the following command…

```
gcloud services list --enabled
gcloud services enable cloudscheduler.googleapis.com --project=hthaogcrj-practice
gcloud services list --enabled
```

Now we can create a cron job 

A cron job, for those who have never heard the term, is a scheduled task that runs a regular interval

The way we define the interval on a cron job is with this expression format: 

Minute (0-59) <> Hour (0-23) <> Day of the month (1-31) <> Month (1-12) <> Day of the week (0-7) (0 or 7 = Sunday)

ie: * * * * * - once a minute
ie: 0 9 * * 1 - every Monday at 9:00am

And we can stretch this expression format to its limits like so…

0 14 1,15 * * - the 1st and 15th of each month at 2 PM
*/5 8-10 * * * - every 5 minutes between 8 AM and 10 AM

Here is the gcloud command that we use to create CRON jobs in GCP with Cloud Scheduler (which will in turn trigger our Cloud Run Job)

gcloud scheduler jobs create http $SCHEDULER_JOB_NAME --location $SCHEDULER_REGION --schedule=“$CRON_EXPRESSION” --uri=“https://REGION-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/$PROJECT_ID/jobs/$JOB_NAME:run” --http-method POST --oauth-service-account-email $SERVICE_ACCOUNT_EMAIL_WITH_PERMISSIONS

$SCHEDULER_JOB_NAME -> cron-job-1
$SCHEDULER_REGION -> us-east1
$CRON_EXPRESSION -> * * * * *
$SERVICE_ACCOUNT_EMAIL_WITH_PERMISSIONS -> aka the “Default compute service account”

gcloud scheduler jobs create http cron-job-1 --location us-east1 --schedule="* * * * *" --uri="https://us-east1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/hthaogcrj-practice/jobs/first-crj-ever:run" --http-method POST --oauth-service-account-email 148827868659-compute@developer.gserviceaccount.com

Notice how we are giving the CRON job the “Default compute service account”. We can create another service account for the CRON job if we want to be super restrictive on principle but this is ok as the CRON job is performing a limited task and is managed by Google.

https://console.cloud.google.com/run/jobs/details/us-east1/first-crj-ever/logs?project=hthaogcrj-practice

Here is how you pause the cron job…

gcloud scheduler jobs pause cron-job-1 --location=us-east1

And here is how you delete the cron job

gcloud scheduler jobs delete cron-job-1 --location=us-east1

Fabulous. Now we know how to run CRON Jobs in the Cloud…

***INTERMISSION***
