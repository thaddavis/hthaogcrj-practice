# PART 3 - CICD with GitHub Actions

Let’s now automate the deployment for our application with GitHub actions…

- Add the .github/workflows/cicd.yaml script

```
mkdir .github/workflows
touch .github/workflows/cicd.yaml
```

And we’ll populate this cicd.yaml file with this content…

Placing a .yaml file at this location of our project tree will automatically trigger the code outlined within it each time we push code to the `main` branch

If we look closely, this cicd.yaml script, we will see it requires us to setup up some “variables” as well as a “secret” in GitHub

So let’s do that…

If we come over to the Settings section of our GitHub repo…

Let’s add the following “Repository variables”…

PROJECT_ID
PROJECT_NUMBER
JOB_NAME
CLOUD_RUN_REGION
DOCKER_IMAGE_URL
ARTIFACTORY_URL

And here is how we generate the value for the “secret”…

Come over to the “IAM & ADMIN” page on GCP’s Console and select the `Service Accounts` sub-page…

A “Service Account” is fancy name for a username/password that we give to an application so it has permissions to do what we need it to do

And to the keen eye, notice how of GCP comes with a number of IAM users already created called the Default Compute Service Account. This is a Service Account that GCP gives to several API’s within our project so they have the permissions to do what they need to do

Let’s create a service account called…

Name: “hthaogcrj-cicd-sa”
Description: “hthaogcrj - Service Account for CICD with GitHub Actions”

PRO TIP: Add descriptions where possible to your GCP resources so you know what they’re for after revisiting them after long periods of time

And after we create the Service Account, let’s select it from the list of Service Accounts in our project > Come over to the keys tab > And generate a JSON key

This will download a JSON file to our computer and the contents of this JSON file are what we need

Let’s copy the contents of this file and add it as a secret in our GitHub repository…

And that takes care of all the variables and secrets our CICD script needs

SIDENOTE: Now we can see the difference between a GitHub “variable” & “secret”. The values we provide for secrets are NOT able to be viewed after we create them whereas the values we provide for variables are… 

1 - Let’s test our CICD script by pushing our latest code to the GitHub repository

2 - ERROR: denied: Permission "artifactregistry.repositories.uploadArtifacts" denied on resource "projects/hthaogcrj-practice/locations/us-east1/repositories/repo-for-job-1" (or it may not exist)

3 - gcloud iam service-accounts list --project $PROJECT_ID

4 - gcloud projects get-iam-policy $PROJECT_ID

5 - gcloud projects get-iam-policy $PROJECT_ID --flatten="bindings[].members" --format="table(bindings.role)" --filter="bindings.members:serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com"

WE NEED TO ADD PERMISSIONS FOR UPLOADING IMAGES TO ARTIFACT REGISTRY TO THE CICD SERVICE ACCOUNT…

6 - GRANT THE `roles/artifactregistry.writer` role to the “CICD Service Account”

7 - gcloud projects add-ism-policy-binding hthaogcrj-practice --member="serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com" --role="roles/artifactregistry.writer"

8 - gcloud projects get-iam-policy $PROJECT_ID --flatten="bindings[].members" --format="table(bindings.role)" --filter="bindings.members:serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com"

9 - RETRIGGER THE GITHUB ACTION IN THE GITHUB CONSOLE

10 - ERROR: (gcloud.run.jobs.deploy) PERMISSION_DENIED: Permission 'run.jobs.get' denied on resource 'namespaces/hthaogcrj-practice/jobs/job-1' (or resource may not exist). This command is authenticated as hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com using the credentials in /home/runner/work/hthaogcrj-practice/hthaogcrj-practice/gha-creds-dde669d04d533f26.json, specified by the [auth/credential_file_override] property.

11 - gcloud projects add-iam-policy-binding hthaogcrj-practice --member="serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com" --role="roles/run.admin"

WE NEED TO ADD PERMISSIONS FOR UPDATING CLOUD RUN JOBS TO THE CICD SERVICE ACCOUNT…

12 - gcloud projects get-iam-policy $PROJECT_ID --flatten="bindings[].members" --format="table(bindings.role)" --filter="bindings.members:serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com"

13 - RETRIGGER THE GITHUB ACTION IN THE GITHUB CONSOLE

14 - ERROR: (gcloud.run.jobs.deploy) PERMISSION_DENIED: Permission 'iam.serviceaccounts.actAs' denied on service account 148827868659-compute@developer.gserviceaccount.com (or it may not exist). This command is authenticated as hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com using the credentials in /home/runner/work/hthaogcrj-practice/hthaogcrj-practice/gha-creds-3c3a9156b6f4ce02.json, specified by the [auth/credential_file_override] property.

15 - gcloud iam service-accounts add-iam-policy-binding 148827868659-compute@developer.gserviceaccount.com --member="serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com" --role="roles/iam.serviceAccountUser"

MY UNDERSTANDING OF THIS PERMISSION ISSUE IS WE NEED TO ADD A PERMISSION FOR ALLOWING OUR CICD SERVICE ACCOUNT TO TRIGGER ACTIONS THAT WILL BE PERFORMED BY THE “DEFAULT COMPUTE SERVICE ACCOUNT”

16 - gcloud iam service-accounts get-iam-policy 148827868659-compute@developer.gserviceaccount.com

17 - RETRIGGER THE GITHUB ACTION IN THE GITHUB CONSOLE

18 - And it should work √

- LET’S TRIGGER THE JOB AGAIN AND TAKE A LOOK AT THE LOGS
    - gcloud run jobs execute first-crj-ever --region us-east1
- MAKE A CHANGE TO OUR SCRIPT
- PUSH THE CHANGE TO GITHUB
- WAIT FOR THE CICD SCRIPT TO COMPLETE
- AND TRIGGER THE JOB AGAIN AND TAKE A LOOK AT THE LOGS
    - gcloud run jobs execute first-crj-ever --region us-east1

AND IT’S WORKING! Fantastic. Now we can start to move faster…

In PART 4, we will learn how to trigger our job on a regular schedule using a GCP product called “Cloud Scheduler” 