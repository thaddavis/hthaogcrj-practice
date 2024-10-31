# PART 2 - Deploy a simple Job to Google Cloud Run

In part 2, we’ll learn how to deploy a simple job to Google Cloud Run in preparation for learning how to host our PRODUCTION application.

As we’re starting from scratch, let’s create a new project in GCP. You can do this in multiple ways but let’s use the web console for now…

Come over to https://console.cloud.google.com/welcome

And on the top navbar you should see a dropdown for viewing your account’s projects. And after opening the dropdown, you should see a button that says “Create Project”

Click it and let’s create a new project. I’ll call mine `hthtogcrj`

All of the GCP-related work we’ll implement will be done in this project for organizational purposes.

After our GCP project is created, let’s come over to the Cloud Run page by searching “Cloud Run” in the search bar OR by clicking the Cloud Run option in the sidenav…

Cloud Run is a managed platform for running Containers in GCP.

On the Cloud Run page you should see 2 tabs that say “Services” & “Jobs”

In this context, “Services” means long-running applications like HTTP APIs that need to be responsive to incoming requests from the internet while “Jobs” on the other hand are used for triggering scripts that release the resources needed to run them immediately upon completion or failure.

This video focuses on the use of Cloud Run Jobs so let’s deploy a simple Job to get our feet wet…

https://cloud.google.com/run/docs/quickstarts/jobs/build-create-python

First let’s authenticate our Dev container with GCP by typing…

- `gcloud init` command
- `gcloud config get-value project`

Next let’s set up this GCP project so we can create Cloud Run Jobs inside of it like so…

- `gcloud services list --enabled`
- `gcloud services enable run.googleapis.com cloudbuild.googleapis.com`
- `gcloud services list --enabled`

Moving on, we now have to enter a command that requires the PROJECT_NUMBER of our GCP project. Depending on the gcloud command we’d like to use, we have to reference our project by either its $PROJECT_ID or its $PROJECT_NUMBER. I know it’s confusing but welcome to GCP.

In this instance my PROJECT_NUMBER is 148827868659 and my PROJECT_ID is hthtogcrj.

- You can find these values in the console by coming over to the Dashboard OR by using the terminal…
    - https://console.cloud.google.com/home/dashboard?project=hthaogcrj-practice
    - gcloud config get-value project
    - gcloud projects describe $PROJECT_ID --format="value(projectNumber)"

After we’ve retrieved our $PROJECT_ID and PROJECT_NUMBER, let’s define them as variables in our terminal…

PRO TIP: Wherever possible, define your PROJECT_ID & PROJECT_NUMBER as variables in your terminal and avoid hardcoding them in your gcloud commands. This will save you time.

Finally let’s run this command…

gcloud projects add-iam-policy-binding $PROJECT_NUMBER --member=serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com --role=roles/cloudbuild.builds.builder

This command gives the Cloud Run API in our project permissions to talk to a handful of other APIs in GCP…

The reason why we need to do this will make sense shortly…

And next, let’s add 7 files to our project. You can do this with VSCode’s UI or with the terminal…

I’ll use the terminal…

- `touch main.py requirements.txt Procfile Dockerfile.prod cloudbuild.yaml`
- `mkdir helpers`
- `touch helpers/say_hello.py`

- And let’s populate the main.py file with this content
- the requirements.txt with this content
- the .gitignore file with this content <!— IMPORTANT —>
    - https://github.com/github/gitignore/blob/main/Python.gitignore
- the Procfile with this content
- the Dockerfile.prod with this content
- the cloudbuild.yaml file with this content
- And the say_hello.py file with this content

This little application we just put together doesn’t do anything special BUT it does show you how most Python programming techniques still apply when building Cloud Run Job projects

LET’S TEST THIS LITTLE APPLICATION OUT IN THE DEV CONTAINER LIKE SO…

- pip install -r requirements.txt (As hinted by this warning in our editor)
- python main.py

PRO TIP: Sometimes when you fix errors and they’re still not going away in editor’s UI you have to restart the language server for the language you’re programming in (SHIFT + COMMAND + P) “Python: Restart Language Server” - and that should do it

OK! We’ve built a little script, we’ve tested it works, now let’s ship it job to Cloud Run Jobs

The left part of this diagram shows what we’ve done so far and the right part shows what we’re about to do…

https://learn.microsoft.com/en-us/dotnet/architecture/microservices/container-docker-introduction/docker-containers-images-registries

EXPLAIN THE LEFT HALF AND BRIEFLY EXPLAIN THE RIGHT HALF

We’ll reference this diagram after the deployment process again at which point it’ll make more sense… 

- PROJECT_ID=hthaogcrj-practice

DEPLOYMENT STEP #1 will be to create a repository in Google Artifact Registry. Inside of this Artifact Registry we can create repositories that will hold “images”.

When we build a Dockerfile we are left with what is called an “Image”. An “ Image” in the context of Docker is a collection of files that define all of the code and operating system requirements needed to run a particular application.

If we rewind to when we built the “Dev Container”, we remember seeing that an image and a container was created in Docker Desktop UI after we selected the “Reopen In Container” option in the COMMAND PALETTE…

After the image defining our “Dev Container” was ran (or launched) it left us with a “mini-computer” that had all the software we needed to build a Python application inside of it

So in summary, when we build a Dockerfile, it leaves us with an “Image”. And when we run the code along with the operating system requirements defined in an “Image”, we are left with a “Container“

We will now create our “Production Container” by building the Dockerfile.prod into an “Image” that will contain all the software and OS requirements needed to run our application on Cloud Run.

Because our “Production Image” will be so similar to our “Dev Image” there’s an extremely high likelihood that our little application will work just as it did in the “Dev Container” when we ship run it to Cloud Run…

As we can see, the only difference between our Production Image and our Dev Image will be the removal of some of the software that was needed during during development such as gcloud, .git, and Docker. These tools are not needed when running our application (or job) in Cloud Run.

Now you understand the reason why Docker is so useful. When you send code on its own to different computer without defining all of the operating system requirements it needs to run successfully, you then increase the chances of it not working. Docker packages code along with its operating system requirements so it has a higher likely of working when it runs on other computers on the internet.

If you are still confused by what was just said, here’s an analogy…

Dockerfile : Image : Container :: Recipe : Frozen Meal : Meal :: Blueprint : Manufactured Good : Purchased Good

OK!

When we build Docker images, we can store them in what are called “Registries”. There are many registries on the internet for example Google has a Registry, Amazon has a registry, Microsoft has a registry, and many companies run their own private registries for storing images they don’t want to be hosted outside of their network.

Inside of a registry, we can create repositories for storing distinct groups of images

FOR CLARITY: An image repository is not a .git repository. There are similar in a general sense but they are two different things

An image repository stores Docker images. A .git repository stores the history of code changes we make to a code base and offer many collaboration features when working in TEAM settings

Let’s now create a repository for storing the image powering our “Production Container”

```
gcloud artifacts locations list
PROJECT_ID=hthaogcrj-practice
gcloud artifacts repositories list
gcloud artifacts repositories create repo-for-job-1 --repository-format=docker --location=us-east1 --description="Repository for Job 1’s Images" --project $PROJECT_ID
gcloud artifacts repositories list
gcloud artifacts repositories describe repo-for-job-1 --location=us-east1
gcloud artifacts docker images list us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1
```

Now that we have our repository set up, we can use it for storing our Production Images…

I’m going to show you how to do this 2 ways: 1) Using Cloud Build AND 2) using the Docker client in the Dev Container

First let’s walkthrough how to do this with Cloud Build, which we enabled in our GCP project earlier if you recall…

```
touch cloudbuild.yaml
```

In the cloudbuild.yaml we can see a script that will, no surprise here, build the Dockerfile.prod and store the resulting image into our repository…

The URLs for repositories in Google Cloud follow a very specific format based on the data center where they are hosted. Here's the general format…

[region]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]

The -t flag on the “docker build” command allows us to name our images whatever we like, but, in order for the subsequent “docker push” command to know where to store the resulting image, the name must follow this GCP naming format

AKA: As long as we name our image according to this format, things will “just work” when we issue the command to store it in our repository

So! Here’s how we use Cloud Build to store images into Artifact Registry…

```
gcloud builds submit --config=cloudbuild.yaml
gcloud artifacts repositories list
gcloud artifacts docker images list us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1
```

As there are often multiple ways to skin a cat, secondly, for completeness, let’s walkthrough how to build and store images into Artifact Registry using the docker client installed in our “Dev Container” as well…

```
docker build --platform linux/amd64 -t us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1/job-1-image:latest -f Dockerfile.prod .
gcloud auth print-access-token
docker login -u oauth2accesstoken https://us-east1-docker.pkg.dev # And then paste in the access token for authenticating with the Registry
gcloud auth configure-docker us-east1-docker.pkg.dev
docker push us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1/job-1-image:latest # for storing the image into "Artifact Registry"
```

Now that have our image stored in the Cloud, we can deploy our first job ever to Cloud Run…

```
gcloud run jobs deploy first-crj-ever --image us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1/job-1-image:latest --region us-east1 --project $PROJECT_ID
```

NOTE: Explain how tags work

And now that we have our job registered in Cloud Run we can trigger it like so…

```
gcloud run jobs execute first-crj-ever --region us-east1
gcloud run jobs execute first-crj-ever --tasks 2 --region us-east1 <!— GOOD TO KNOW —>
```

VERIFY: https://console.cloud.google.com/run/jobs?project=hthaogcrj-practice
LOOK AT THE LOGS: https://console.cloud.google.com/run/jobs/details/us-east1/job-1/logs?project=hthaogcrj-practice

Alright great! We now know how to manually deploy and execute containerized scripts using Cloud Run Jobs.

Next up, we’ll automate this manual deployment process using GitHub Actions