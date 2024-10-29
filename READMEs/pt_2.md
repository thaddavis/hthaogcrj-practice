PART 2 - Deploy a simple Job to Google Cloud Run

Let’s now take a look at Google Cloud Run. As we’re starting from scratch, let’s create a new project in GCP. You can do this in multiple ways but let’s use the web console for now…

Come over to https://console.cloud.google.com/welcome

And on the top navbar you should see a dropdown for viewing your projects and after opening the dropdown, you should see a button that says “Create Project”

Click it and let’s create a new project. I’ll call mine `hthtogcrj`

All of the GCP-related work we will implement will be done in this project for organizational purposes and after we’ve finished with this walkthrough, we can release whatever resources we provision inside of it to keep our costs low.

And after our GCP project is created, come over to the Cloud Run page by either searching and selecting “Cloud Run” in the search bar OR by clicking the Cloud Run option in the sidebar…

Google Cloud Run is a managed platform for running “containerized” services and jobs in GCP.

Once your on the Cloud Run page you should see 2 tabs that say “Services” & “Jobs”

In this context, “Services” means long-running applications like HTTP APIs that need to be responsive to incoming requests from the internet

while “Jobs” on the other hand are used for triggering scripts that release the resources needed to run them immediately upon script completion or failure.

This video focuses on the use of Cloud Run Jobs so let’s deploy a simple Job to get our feet wet…

https://cloud.google.com/run/docs/quickstarts/jobs/build-create-python

First let’s authenticate our Dev container with GCP by typing…

- `gcloud init` command
- `gcloud config get-value project`

Next let’s set up our GCP project so we can create Cloud Run Jobs inside of it like so…

- `gcloud services list --enabled`
- `gcloud services enable run.googleapis.com cloudbuild.googleapis.com`
- `gcloud services list --enabled`

Moving on, we now have to enter a command that requires the PROJECT_NUMBER of our GCP project. Depending on the gcloud command we’d like to use, we have to reference our project by either its $PROJECT_ID or its $PROJECT_NUMBER. I know it’s confusing but welcome to GCP.

In this instance my PROJECT_NUMBER is 148827868659 and my PROJECT_ID is hthtogcrj.

- You can find these values in the console or by using the terminal…
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

- `touch main.py requirements.txt .gitignore Procfile Dockerfile.prod cloudbuild.yaml`
- `mkdir helpers`
- `touch helpers/say_hello.py`

- And let’s populate the main.py file with this content
- the requirements.txt with this content
- the .gitignore file with this content
    - https://github.com/github/gitignore/blob/main/Python.gitignore
- the Procfile with this content
- the Dockerfile.prod with this content
- the cloudbuild.yaml file with this content
- And the say_hello.py file with this content

This script we just created doesn’t do anything special BUT it does show you how most Python programming techniques still apply when building Cloud Run Job projects

LET’S TEST THIS LITTLE APPLICATION OUT IN THE DEV CONTAINER LIKE SO…

- pip install -r requirements.txt
- python main.py

PRO TIP: Sometimes when you fix errors and they’re still not going away in VSCode’s UI you gotta restart the language server (SHIFT + COMMAND + P) “Python: Restart Language Server”

OK! We’ve built a little script, we’ve tested it works, now let’s ship it job to Cloud Run Jobs

The left part of this diagram shows what we’ve done so far and the right part shows what we are about to do…

https://learn.microsoft.com/en-us/dotnet/architecture/microservices/container-docker-introduction/docker-containers-images-registries

EXPLAIN THE LEFT HALF AND BRIEFLY EXPLAIN THE RIGHT HALF

We’ll reference this diagram after the deployment process again at which point it’ll make a lot of sense… 

- PROJECT_ID=hthaogcrj-practice

DEPLOYMENT STEP #1 will be to create a repository in Google Artifact Registry. Inside of this Artifact Registry we can create repositories that will hold “images”.

When we build a Dockerfile we are left with what is called a “Docker Image”. A “Docker Image” is a collection of files that define all of the code and operating system requirements needed to run a particular application.

If we rewind to when we built the “Dev Container”, we remember seeing that an image and a container was created in Docker Desktop GUI after we selected the “Reopen In Container” option…

After the image defining our “Dev Container” was ran (or launched) it left us with a “mini-computer” that had all the software we needed to build an application inside of it

So in summary, when we build a Dockerfile, it leaves us with an “Image”. And when we run code along with the operating system requirements defined in its “Image”, we are left with a “Container“

We will now create our “Production Container” by building the Dockerfile.prod into an Image that will contain all the software and OS requirements needed to run our application on Cloud Run.

Because our “Production Image” will be so similar to our “Dev Image” there’s an extremely high likelihood that our script will work just as it did in the “Dev Container” when we ship run it to Cloud Run…

As we can see, the only difference between our Production Image and our Dev Image will be the removal of some of the software that was needed during during development such as gcloud, .git, and Docker. These tools are not needed when running our script (or job) in Cloud Run.

Now you understand the reason why Docker is so useful. When you send code on its own to different computer without defining all of the operating system requirements it needs to run successfully, you then increase the chances of it not working. Docker packages code along with its operating system requirements so it has a higher likely of working when it runs on other computers on the internet.

If you are still confused by what was just said, here’s an analogy I hope helps clarify…

Dockerfile : Image : Container :: Recipe : Frozen Meal : Meal :: Blueprint : Manufactured Good : Purchased Good

OK! Enough Rambling…

When we build Docker images, we can store them in what are called “Registries”. There are many registries on the internet for example Google has a Registry, Amazon has a registry, Microsoft has a registry, and many companies run their own private registries for storing Images they don’t want to be hosted on other registries.

Inside of a registry, we can create repositories for storing distinct groups of images

```
gcloud artifacts locations list
PROJECT_ID=hthaogcrj-practice
gcloud artifacts repositories list
gcloud artifacts repositories create repo-for-job-1 --repository-format=docker --location=us-east1 --description="Repository for Job 1’s Docker images" --project $PROJECT_ID
gcloud artifacts repositories list
gcloud artifacts repositories describe repo-for-job-1 --location=us-east1
gcloud artifacts docker images list us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1
```

Now that we have our Image Repository set up we can now take our Dockerfile.prod file, build it, and store the resulting image into the repository…

I’m going to show you how to do this 2 ways: Using Cloud Build AND using the Docker client

First let’s walkthrough how to do this with a GCP product called Cloudbuild, which we enabled earlier…

In the cloudbuild.yaml we can see a script that will build the Dockerfile.prod file and store the resulting image into our repository…

The URLs for Artifact Registry Docker repositories in Google Cloud follow a specific format, based on the region. Here's the general format…

[region]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]

So as long as we name our image appropriately things will work

The -t flag allows us to name our image whatever we like but in order for the docker push command to know where to store the resulting image, the name must follow this format

```
gcloud builds submit --config=cloudbuild.yaml
gcloud artifacts docker images list us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1
```

And now let’s walkthrough how to build and store images into Artifact Registry using the docker client installed in “Dev Container”…

```
docker build --platform linux/amd64 -t  -f Dockerfile.prod .
gcloud auth print-access-token
docker login -u oauth2accesstoken https://us-east1-docker.pkg.dev # And then paste in the access token
gcloud auth configure-docker us-east1-docker.pkg.dev
docker build --platform linux/amd64 -t us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1/job-1-image:latest -f Dockerfile.prod .
docker push us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1/job-1-image:latest # for storing the image into "Artifact Registry"
```

Now that have our image stored in the Cloud, we can deploy our first job ever to Cloud Run…

```
gcloud run jobs deploy job-1 --image us-east1-docker.pkg.dev/$PROJECT_ID/repo-for-job-1/job-1-image:latest --region us-east1 --project $PROJECT_ID
```

NOTE: Explain how tags work

And now that we have our job registered in Cloud Run we can trigger it like so…

```
gcloud run jobs execute job-1 --region us-east1
gcloud run jobs execute job-1 --tasks 2 --region us-east1
```

VERIFY: https://console.cloud.google.com/run/jobs?project=hthaogcrj-practice
LOOK AT THE LOGS: https://console.cloud.google.com/run/jobs/details/us-east1/job-1/logs?project=hthaogcrj-practice

Alright great! We now know how to manually deploy and execute containerized scripts using Cloud Run Jobs.

Next up, we’ll automate this deployment process using GitHub Actions