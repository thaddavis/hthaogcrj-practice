PART 3 - CICD with GitHub Actions

- Add the .github/workflows/cicd.yaml script

```
mkdir .github/workflows
touch .github/workflows/cicd.yaml
```

And Populate the cicd.yaml with this content…

Let’s commit these changes and push our project to GitHub to test out this CICD automation.

Placing a .yaml file in this location of our project will automatically trigger this cicd.yaml script each time we push code to the `main` branch

This cicd.yaml script requires us to setup up some GitHub Action “variables” as well as a GitHub “secret”

So let’s do that…

Let’s add the following Repository “variables”…

PROJECT_ID
PROJECT_NUMBER
JOB_NAME
CLOUD_RUN_REGION
DOCKER_IMAGE_URL
ARTIFACTORY_URL

And let’s add the following Repository “secret”

GCP_SA_KEY

Here is how we generate the value for this secret…

We come over to the “IAM & ADMIN” page on the GCP Console and select the `Service Accounts` sub-page…

A “Service Account” btw is a fancy name for a username and password we give to an application so it has the permissions to do what we need it to do

And let’s create a service account called…

Name: “hthaogcrj”
Description: “hthaogcrj - Service Account for CICD with GitHub Actions”

And after we create the Service Account, let’s select it in the list of Service Accounts in our project > Come over to the keys tab > And generate a JSON key

This will download a JSON file to our computer and its contents are what we need

Next we’ll copy/paste the contents of this JSON file into the value field of the GitHub secret we were in the middle of creating…

And that takes care of all the variables and secrets our CICD script needs

We can see now that the difference between a GitHub Repository “variable” & “secret” is that the values we provide for secrets are NOT able to be viewed after we create them whereas the values we provide for variables are… 

1 - Let’s trigger the CICD script again

2 - ERROR: denied: Permission "artifactregistry.repositories.uploadArtifacts" denied on resource "projects/hthaogcrj-practice/locations/us-east1/repositories/repo-for-job-1" (or it may not exist)

3 - gcloud iam service-accounts list --project $PROJECT_ID

4 - gcloud projects get-iam-policy $PROJECT_ID

5 - gcloud projects get-iam-policy $PROJECT_ID --flatten="bindings[].members" --format="table(bindings.role)" --filter="bindings.members:serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com"

6 - GRANT THE `roles/artifactregistry.writer` role to the “Service Account”

7 - gcloud projects add-ism-policy-binding hthaogcrj-practice --member="serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com" --role="roles/artifactregistry.writer"

8 - gcloud projects get-iam-policy $PROJECT_ID --flatten="bindings[].members" --format="table(bindings.role)" --filter="bindings.members:serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com"

9 - TRIGGER THE GITHUB ACTION

10 - ERROR: (gcloud.run.jobs.deploy) PERMISSION_DENIED: Permission 'run.jobs.get' denied on resource 'namespaces/hthaogcrj-practice/jobs/job-1' (or resource may not exist). This command is authenticated as hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com using the credentials in /home/runner/work/hthaogcrj-practice/hthaogcrj-practice/gha-creds-dde669d04d533f26.json, specified by the [auth/credential_file_override] property.

11 - gcloud projects add-iam-policy-binding hthaogcrj-practice --member="serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com" --role="roles/run.admin"

12 - gcloud projects get-iam-policy $PROJECT_ID --flatten="bindings[].members" --format="table(bindings.role)" --filter="bindings.members:serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com"

13 - TRIGGER THE GITHUB ACTION

14 - ERROR: (gcloud.run.jobs.deploy) PERMISSION_DENIED: Permission 'iam.serviceaccounts.actAs' denied on service account 148827868659-compute@developer.gserviceaccount.com (or it may not exist). This command is authenticated as hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com using the credentials in /home/runner/work/hthaogcrj-practice/hthaogcrj-practice/gha-creds-3c3a9156b6f4ce02.json, specified by the [auth/credential_file_override] property.

15 - gcloud iam service-accounts add-iam-policy-binding 148827868659-compute@developer.gserviceaccount.com --member="serviceAccount:hthaogcrj@hthaogcrj-practice.iam.gserviceaccount.com" --role="roles/iam.serviceAccountUser"

16 - gcloud iam service-accounts get-iam-policy 148827868659-compute@developer.gserviceaccount.com

17 - TRIGGER THE GITHUB ACTION

18 - And it should work √

- LET TRIGGER THE JOB AGAIN AND TAKE A LOOK AT THE LOGS
    - gcloud run jobs execute job-1 --region us-east1
- MAKE A CHANGE TO OUR SCRIPT
- PUSH THE CHANGE TO GITHUB
- WAIT FOR THE CICD SCRIPT TO COMPLETE
- AND TRIGGER THE JOB AGAIN AND TAKE A LOOK AT THE LOGS
    - gcloud run jobs execute job-1 --region us-east1

AND IT’S WORKING! Fantastic. Now we can start to move faster…

OK! In PART 4, we will learn how to trigger our job on a regular schedule using a GCP product called “Cloud Scheduler” 