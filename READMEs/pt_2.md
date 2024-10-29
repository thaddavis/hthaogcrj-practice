PART 2 - Deploy a simple Job to Google Cloud Run

Let’s now take at Google Cloud Run. As we are starting from scratch, let’s first create a project in GCP. You can do this in multiple ways but let’s use the web console for now…

Click this dropdown and you should see a button that says “Create Project”

I’ll create a project called `hthtogcrj`

All of the GCP related work we will implement will be done in this project for organizational purposes. After we’ve finished with this walkthrough we’ll delete this GCP project to release whatever resources we provision inside of it.

After we have our project created in the GCP console let’s come over the the Cloud Run page that you can access by search in the search bar or by locating in the side menu…

So Google Cloud Run is a managed platform for running containerized services and jobs in Google’s cloud.

You can 2 tabs on the Google Cloud Run page that say “Services” & “Jobs”

In this context, “Services” means long-running applications like HTTP APIs that need to be responsive to incoming requests from the internet

while “Jobs” on the other hand are used for triggering scripts that release the computational resources needed to run them immediately upon script completion or failure.

As we are learning how Cloud Run Jobs work, let’s deploy a simple Job to get our feet wet…

https://cloud.google.com/run/docs/quickstarts/jobs/build-create-python

First let’s authenticate our Dev container with GCP by typing…

- `gcloud init` command
- `gcloud services list --enabled`
- `gcloud services enable run.googleapis.com cloudbuild.googleapis.com`
- `gcloud services list --enabled`
- Find your project’s “project number” - ie: 148827868659
    - https://console.cloud.google.com/home/dashboard?project=hthaogcrj-practice
- `gcloud projects add-iam-policy-binding 148827868659 --member=serviceAccount:148827868659-compute@developer.gserviceaccount.com --role=roles/cloudbuild.builds.builder`

This command enables Cloud Run to use Cloud Build as needed in our project…

Cloud Build is a product for implementing CICD solutions in GCP’s ecosystem. By CICD, we mean the process of shipping the code we write on our personal computer to the Cloud in an automated manner.

The reason why we need to do this will make sense shortly

And now let’s add 7 more files to our project folder in VSCode…

- `touch main.py`
- `mkdir helpers`
- `touch helpers/say_hello.py`
- `touch requirements.txt`
- `touch .gitignore`
- `touch Procfile`
- `touch Dockerfile.prod`
- `touch cloudbuild.yaml`

- Let’s populate the main.py file
- Let’s populate the say_hello.py file
- Let’s populate the requirements.txt
- Let’s populate the .gitignore
    - https://github.com/github/gitignore/blob/main/Python.gitignore
- Let’s populate the Procfile file
- Let’s populate the Dockerfile file

This application is quite stupid but it shows all the fundamental building blocks that we can expand upon to build whatever application we like

LET’S TEST THIS EXAMPLE PROJECT OUT IN THE DEV CONTAINER LIKE SO…

- pip install -r requirements.txt
- python main.py

PRO TIP: Sometimes you gotta restart the language server (SHIFT + COMMAND + P) “Python: Restart Language Server” when you fix errors and they still are not going away in VSCode’s UI

OK! So things work as expected. For clarity, what’s going to happen each time we trigger this job in Google Cloud Run is the instructions in the `main.py` file will be executed

OK! So now let’s ship this job to Cloud Run

Before we do that though let’s pause for a few seconds to look at this diagram - https://learn.microsoft.com/en-us/dotnet/architecture/microservices/container-docker-introduction/docker-containers-images-registries

After we deploy our job, we’ll take another look at this diagram and it’ll make even more sense…

- gcloud artifacts locations list
- PROJECT_ID=hthaogcrj-practice


```
gcloud artifacts locations list
PROJECT_ID=hthaogcrj-practice
gcloud artifacts repositories list
gcloud artifacts repositories create repo-for-job-1 --repository-format=docker --location=us-east1 --description="Repository for Job 1’s Docker images" --project $PROJECT_ID
gcloud artifacts repositories list
gcloud artifacts repositories describe repo-for-job-1 --location=us-east1
gcloud builds submit --config=cloudbuild.yaml
```

Now let’s deploy a job to Cloud Run

```
gcloud run jobs deploy job-1 --image us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1/job-1-image:latest --region us-east1 --project $PROJECT_ID
gcloud run jobs execute job-1 --region us-east1
```

VERIFY: https://console.cloud.google.com/run/jobs?project=hthaogcrj-practice
LOOK AT THE LOGS: https://console.cloud.google.com/run/jobs/details/us-east1/job-1/logs?project=hthaogcrj-practice

FOR COMPLETENESS (AND FOR FUN) LET ME SHOW YOU ANOTHER QUICK WAY TO BUILD & DEPLOY YOUR CODE TO CLOUD RUN JOBS

```
docker build --platform linux/amd64 -t  -f Dockerfile.prod .
gcloud auth print-access-token
docker login -u oauth2accesstoken https://us-east1-docker.pkg.dev # And then paste in the access token
gcloud auth configure-docker us-east1-docker.pkg.dev
docker build --platform linux/amd64 -t us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1/job-1-image:latest -f Dockerfile.prod .
docker push us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1/job-1-image:latest # for storing the image into "Artifact Registry"
gcloud run jobs deploy job-1 --image us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1/job-1-image:latest --region us-east1 --project $PROJECT_ID # deploy 
gcloud run jobs execute job-1 --region us-east1
gcloud run jobs execute job-1 --tasks 2 --region us-east1
```