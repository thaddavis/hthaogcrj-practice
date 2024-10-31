INTRO - How to host CrewAI Agents on Google Cloud Run

In this video we’ll take a close look at a PRODUCTION application involving the use of LLMs, AI agents, GCP, Python, and Docker.

That’s right I said PRODUCTION. This is the real deal. Wake up!

If you’re new to these technologies, I’ll do my best to make them approachable but you will need at least some familiarity with Python, Cloud Computing, and CLIs to easily follow along.

If you’re already very familiar with these technologies, I’d love your feedback on this application’s overall design in the comments…

In this video we’re going to build a team of personalized A.I. news reporters who will send us daily bullet points highlighting news updates happening across multiple websites

Here’s an architecture diagram of what we’ll be building for clarity…

This design can be used as the foundation for many applications BUT to get your creative juices flowing, I’ll give you 2 that come to mind…

	1) a productivity hack for staying up-to-date on a niche that matters to you
	2) building your own A.I.-powered newsletter

We’ll build these news reporters using CrewAI (which is a Python-based tool for programming AI Agents) and we’ll design these A.I. news reporters to run on a hosting service managed by Google called “Cloud Run Jobs”.

Running our application in the Cloud means it’ll work for us regardless of if our personal computer is turned on or off

🔥

HERE’S AN OVERVIEW OF THE SECTIONS THAT FOLLOW SO YOU KNOW WHAT’S COMING
 
- PART 1 - Setting up our Dev Container
- PART 2 - Deploying a simple Job to Google Cloud Run with CICD
- PART 3 - CICD with GitHub Actions
- PART 4 - Setting up a cron job using Cloud Scheduler
- PART 5 - Adding CrewAI Agents
- PART 6 - Adding Mailgun
- PART 7 - Deploying the application to GCP
- PART 8 - Adding AgentOps
- PART 9 - Wrapping up

And I 100% guarantee this is going to be incredible

For those interested in coding along, here’s what you’ll need…

- A) A PC aka: a Laptop or Desktop
- B) This PC will need these 2 applications installed onto it: Docker and VSCode
- C) And after you have VSCode installed you’ll need to add 2 VSCode extensions namely the “Docker” extension and “Dev Containers” extension
- D) A GitHub account
- E) A GCP account
- F) An OpenAI account
- G) A Mailgun Account
- I) An AgentOps Account
- J) Optionally: You’ll need a domain

I know this sounds like a lot but it’s not that bad. Let me break it down…

To give you a feel for how easy it was for me to install Docker, VSCode, and these 2 VSCode Extensions onto my M1 Macbook Pro, I’ll be playing a clip shortly that shows how I did it…

Even though my machine is Mac-based, the broad strokes of what you’ll see in that clip should apply even if you’re machine is Windows or Linux-based.

In regards to the GitHub account, you can get an account by coming over to https://github.com/ and signing up

In regards to GCP, you can get an account by coming over to https://cloud.google.com and signing up. OR you can simply press the “Activation” button on the https://cloud.google.com/cloud-console page if you already have a gmail account you’d like to use GCP with…

GCP usually offers free credits on signup or activation PLUS the cost of what we’re doing here will be in the pennies so the GCP side of things should be practically free assuming you tear down the project we create within a few days after building it. We’ll show how to tear down the GCP project at the end of this video.

When we get to the 2nd half of this walkthrough (aka PART 5) we will need the remaining prereqs…

Those being…

- An OpenAI account
    - For powering our LLM-based Agents
- A Mailgun account - https://try.mailgun.com/api-1
    - For delivering our A.I. generated emails
- And an AgentOps account
    - For monitoring our Agents after they’ve been deployed

- And optionally: a Domain

    - Hopefully you have an extra domain handy, but, in case you don’t, you can purchase one from any Domain Registrar that lets you edit the domain’s DNS records (for example I’ll be using Amazon Route 53) 
    - By adding a few entries to the domain’s DNS settings we can “verify it” 
    - Without verifying a domain we own as the sender of our emails, the messages we send with Mailgun will probably land in the recipient’s SPAM folder
    - So if you don’t mind the A.I. generated emails we create being delivered to SPAM, you don’t need a domain, BUT if you do want them delivered to INBOX proper, you will need a domain.

The design of this application we’re going building is modular so you could switch out certain components for others you prefer BUT this is what we’ll be using for demo purposes

If you have any setup or installation roadblocks leave a comment and for additional support you can enter the details of the issues you come across into either Google or ChatGPT.

Good luck and I’ll see you in part 1 when you’re ready to go : )

[PLAY CLIP OF INSTALLING DOCKER AND VSCODE]

PART 1 - Setting up our Dev Container

Welcome! So I’m assuming you have the following prerequisites set up on your personal computer…

- Docker
- VSCode
- The `Docker` VSCode extension
- The `Dev Containers` VSCode extension
- A GitHub account
- And a GCP account

Let’s get started by creating a folder somewhere on our machine (for example the Desktop or Home folder perhaps)…

I’m going to call my folder (`mkdir hthtogcrj`)

and let’s open this folder using VSCode…

If we pop open VSCode’s terminal we can confirm where we are on the file system…

```pwd``` and indeed we’re in the empty folder we just created

As we’re starting from scratch, let’s 1st set up our “Dev Container”…

If you unfamiliar with the term “Dev Container” hold tight, it’ll make sense in a few minutes…

Inside this empty folder let’s create the following folder and files…

```
mkdir .devcontainer
touch .devcontainer/devcontainer.json
touch Dockerfile.dev
```

And populate the devcontainer.json with this content 
And populate the Dockerfile.dev with this content

The code we just added looks a bit hectic but it’s actually quite useful.

These files will build a little mini-computer that will run on top of our actual computer. This mini-computer, called a “Docker Container”, is where we will write all the code for powering our application

When finishing this walkthrough, we can delete this “Docker Container” (or mini-computer) and our base machine (aka our laptop or Desktop or whatever we’re using) will be left clean as if nothing ever happened…

In addition to helping us stay organized, the use of “Docker Containers” is highly compatible with Cloud platforms like AWS, GCP, and Azure. So using them for development will make running our application in the cloud easy as we’ll shortly see.

To shed some light on what these files are doing, the Dockerfile.dev does most of the work of configuring our “Docker Container” while the devcontainer.json mostly outlines how VSCode should connect to the “Docker Container” and allow us to edit files inside of it.

The Dockerfile.dev will create a “mini-computer” that comes with Python, .git, gcloud, and Docker installed WHILE the devcontainer.json file is telling VSCode to, by default, open the /code folder in this “mini-computer” when we want to view the files inside of it. Let’s not get too in the weeds but we can also see on lines 24 & 25 that we’re configuring the Docker client installed in the “Docker Container” to forward commands to the Docker server running on our base machine…

https://docs.docker.com/get-started/docker-overview/#docker-architecture

When we use a “Docker Container” for the purpose of developing applications in it, we call it a “Dev Container”…

In the coming sections, we will use another “Docker Container” that is almost identical to our “Dev Container” for running our application in GCP. We will refer to this 2nd container as our “Production Container”. Don’t sweat it if this confusing. It’ll makes sense shortly. Let’s move on.

If we type these key strokes into VSCode, SHIFT + COMMAND + P, we’ll pop open the “Command Palette” (as it’s so called) and we can select an option that says “Reopen in Container” to trigger a script provided by the “Dev Containers” extension that will build a “Docker Container” based on the configuration we’ve specified.

Before we select this option though, let’s take a look at the Docker Desktop GUI that comes with Docker to compare the before and after…

At the moment we see the Docker GUI shows no Containers, Images, or Volumes.

Now let’s select the “Reopen in Container” option and watch what happens…

You will have a wait few moments the first time you build a “Dev Container” BUT after it’s built, launching it will only take a few seconds…

Now that the Container is finished building let’s take another look at the Docker Desktop GUI…

We see blah, blah, blah. What this all means will make sense shortly…

If we come back to VSCode and pop open the built-in terminal again to confirm where we are on the file system, we see that VSCode is connected to the /code folder at the root of the Dev container and NOT the original folder we first opened.

We will be building the PRODUCTION application mentioned at the start inside of this Dev Container…

Let’s quickly confirm all the software we’ll need is installed…

```sh
python --version
git -v
gcloud --version
docker version
```

And everything’s looking good.

Let’s save our progress in a remote .git repository. We will be using GitHub.

- https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials
- https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git

Dev Containers offer built-in support for connecting to .git repos via both SSH AND HTTPS protocol BUT for demonstration purposes we’ll use HTTPS. The long story short of how this works is the credentials set up on our base machine get shared with the “Dev Container” automatically behind the scenes.

Let me show you what I mean…

1st let’s create a repo in GitHub — I’ll call mine `hthtogcrj`. And then let’s configure our project folder to use this GitHub repository for storing a backup of all the changes we make along our journey by entering the following commands…

```
git init
git remote add origin https://github.com/thaddavis/hthaogcrj-practice.git
```

If I delete the credential for github.com in MacOS’s built in credential management application, called Keychain Access, you’ll see my attempts to push code to the repo fail both on my base machine as well as in the Dev Container…

FYI/SIDENOTE/TMI: I think the corresponding credential management applications on Window and Linux would be Credential Manager and libsecret respectively…

Anyways…

If I re-authenticate with GitHub in my base environment using a GitHub Personal Access Token (PAT) that has permissions attached to it to view and edit the contents of the `hthtogcrj` repo we just created, 

For now, I’ll just `Contents` and `Metadata` permissions. We can always add more permissions later if needed…

We can see that the .git push commands now work on both the base machine and in the Dev Container…

In practical terms here’s the difference between the authentication options offered by GitHub…

- Authenticating via SSH protocol is the most permissive. It’ll allow you to interact with all repos in your GitHub account
- Authenticating via HTTPS offer fine-grained access control. It allows you to specify exactly which data in your GitHub account a machine can access

Because this video is NOT a deep dive on GitHub, we’ll leave it there…

If you have issues connecting to your remote .git repository in the “Dev Container”, you can use a terminal on your host machine for interacting with GitHub as PLAN B.

To be cute I’ll store the PAT in the .env file in our project. Because .env is listed as entry in the .gitignore, the .env file will NOT be uploaded to GitHub so we are safe to store the PAT here for the time being…

So let’s save all our code so far.

<FIRST_GIT_TAG> and include README.md too 🔑

And now that we have our code stored in GitHub let’s continue on to PART 2!

PART 2 - Deploy a simple Job to Google Cloud Run

Let’s now take a look at Google Cloud Run. As we’re starting from scratch, let’s create a new project in GCP. You can do this in multiple ways but let’s use the web console for now…

Come over to https://console.cloud.google.com/welcome

And on the top navbar you should see a dropdown for viewing your projects. And after opening the dropdown, you should see a button that says “Create Project”

Click it and let’s create a new project. I’ll call mine `hthtogcrj`

All of the GCP-related work we will implement will be done in this project for organizational purposes and after we’ve finished with this walkthrough, we can release whatever resources we provision inside of it to keep our costs low.

And after our GCP project is created, let’s come over to the Cloud Run page by either searching and selecting “Cloud Run” in the search bar up top OR by clicking the Cloud Run option in the sidenav…

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

Let’s save our work

And next up, we’ll automate this manual deployment process using GitHub Actions

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

PART 4 - Set up a cron job using Cloud Scheduler

https://console.cloud.google.com/marketplace/product/google/cloudscheduler.googleapis.com?project=hthaogcrj-practice

To use Cloud Scheduler we have to enable it in our project by entering the following command…

```
gcloud services list --enabled
gcloud services enable cloudscheduler.googleapis.com --project=hthaogcrj-practice
gcloud services list --enabled
```

Now we can create a cron job 

A cron job, for those who have never heard the term, is a scheduled task that runs a regular interval

The way we define the interval is with this cool expression: 

Minute (0-59) <> Hour (0-23) <> Day of the month (1-31) <> Month (1-12) <> Day of the week (0-7) (0 or 7 = Sunday)

ie: * * * * * - once a minute
ie: 0 */3 * * * - every 3 hours
ie: 0 9 * * 1 - every Monday at 9:00am

And you can do some wild ones like

0 14 1,15 * * - the 1st and 15th of each month at 2 PM
*/5 8-10 * * * - every 5 minutes between 8 AM and 10 AM

Here is the gcloud command that we create our CRON job (which will trigger our Cloud Run Job)

gcloud scheduler jobs create http cron-job-1 --location us-east1 --schedule="* * * * *" --uri="https://us-east1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/hthaogcrj-practice/jobs/job-1:run" --http-method POST --oauth-service-account-email 148827868659-compute@developer.gserviceaccount.com

gcloud scheduler jobs create http $SCHEDULER_JOB_NAME --location $SCHEDULER_REGION --schedule=“$CRON_EXPRESSION” --uri=“https://REGION-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/$PROJECT_ID/jobs/$JOB_NAME:run” --http-method POST --oauth-service-account-email $SERVICE_ACCOUNT_EMAIL_WITH_PERMISSIONS

$SCHEDULER_JOB_NAME -> cron-job-1
$SCHEDULER_REGION -> us-east1
$CRON_EXPRESSION -> * * * * *
$SERVICE_ACCOUNT_EMAIL_WITH_PERMISSIONS -> aka the “Default compute service account”

https://console.cloud.google.com/run/jobs/details/us-east1/job-1/logs?project=hthaogcrj-practice

Here is how you pause the job…

gcloud scheduler jobs pause cron-job-1 --location=us-east1

And here is how you delete the job

gcloud scheduler jobs delete cron-job-1 --location=us-east1

Fabulous. Now we know how to run CRON Jobs in the Cloud…

***INTERMISSION***

PART 5 - Adding CrewAI Agents

- Update the requirements.txt file to contain the following 3rd-party packages as well as these specific versions…
    - pip install -r requirements.txt
- Next let’s update the `main.py` file to include a bunch of CrewAI-related code…
    - And you can see we’re importing a helper function and a pydantic type as well…
    - So let’s add the files for supporting these imports…
        - touch helpers/replace_yaml_variables.py
        - mkdir application_schema
        - touch application_schema/news_results.py
        - mkdir config
        - touch config/tasks.yaml
        - touch config/agents.yaml

- If you look closely at this config you can see we are creating a group of agents that are specialized in reporting information about the niche of Haitian Global News
- You can easily tweak this config to report information about whatever niche matters to you
- For example, at the end of this walkthrough we’ll adjust these prompts to focus on reporting the latest news in the world of Insurance Technology
- Anyways!
- Let’s now try running this script and see what happens - `python main.py`
- We can see an ERROR has been thrown due to a missing OPENAI_API_KEY
    - CrewAI, aka the Multi-Agent framework we’re using, supports a number of LLMs but by default is set up to use OpenAI
    - If your new to all this Agent stuff, here’s a quick little diagram that sheds some light on what I just said…
        - An Agent, in the context of this video, is like a virtual person and an LLM acts as the virtual person’s brain
    - You can get an OPENAI_API_KEY by coming over to https://platform.openai.com/ and signing up…
    - And after you’re signed up, make sure to add some credits to your balance. OpenAI’s API is pay-per-use it’s like a gas station so you will need some credits.
    - I recommend adding whatever the minimum allowed amount is as the cost of what we’ll be doing will only be in the pennies
    - After you have some credits added come over to the Dashboard > API keys section and create an API key
        - Let’s copy this API key’s value into our project by adding a new entry in the .env file that reads, in all caps, OPENAI_API_KEY=<API_KEY_HERE>
    - Then we add these lines to the top of our `main.py` file to make the entries in the .env file available to our code
    - And when that’s all set up let’s run our script again
    - `python main.py`
    - This are now looking good…
    - If we take a close look at this code, we can see we’re creating 2 Agents - A Manager Agent and a Researcher Agent…
    - And 1 Task - that being to perform research across a list of web pages
    - This configuration gets tied together with the Crew object provided by CrewAI
        - As of the time of recording CrewAI let’s you run your Agents in 2 modes: Sequential and Hierarchical
        - Sequential Mode means the Agents will perform the tasks outlined in the tasks.yaml file sequentially one-by-one
            - In Sequential Mode, you must manually map each task to one of the agents in your project 
    - Hierarchical Mode, which is what we’re using at the moment, means we delegate one of the Agents in our project as the “Manager” of the other Agents. We then assign tasks to the Manager Agent who will break the task up into sub-tasks as needed and automatically assign each sub-task to one or more Agents in the Crew.
    - Depending on the LLM and other implementation details, the reliability of Hierarchical Mode can be either impressive or atrocious BUT for the job of synthesizing information across a number of web pages in a particular niche, I found Hierarchical Mode to be worthy match

    - Let’s run our Crew a few times to get feel for what it’s doing…
    - Each time we run our Crew we’ll add another website to this list and review the output

- And yea things generally look like they are working so let’s move on to part 6 where will will send this A.I. research report via email to a list of subscribers

Before we move on though let’s save our code in GitHub…

We don’t need to save the report.md file so let’s add it to the .gitignore before committing and pushing and now we’re ready to move on

PART 6 - Add Mailgun

Next up we’ll integrate email into our application…

There are many email providers we could use but for demonstration purpose we will go with Mailgun…

- https://signup.mailgun.com/new/signup
- After signing up you’ll have to verify your email and/or phone number with Mailgun via an Authorization Code that you’ll receive in either your inbox or on your phone…
- After you complete this account verification process, you can then provision an API key
    - This API key is what will authenticate our application with Mailgun’s Email API
- We can store this API key in the .env file
    - Let’s add an entry that reads MAILGUN_API_KEY=<API_KEY_HERE>
- And now let’s add some code for testing that we can send emails from our application
- If we come over to https://app.mailgun.com/mg/sending/domains, we can see that Mailgun provides us with a free domain to test with…
- We will be able to send emails FROM this domain TO any email we list as authorized recipients here…
- To authorize a recipient, we enter and submit its address with this form AND have the owner accept the invitation that they’ll receive via email
- After we authorize some email we own (by own I mean we have access to its inbox), let’s add the following code to our application…

	
    - touch helpers/send_email.py
```
import requests
import os

def send_email():
    print("Sending email...")
    requests.post(
      "https://api.mailgun.net/v3/sandboxd7c358e02f26415dbb7329dd994a8334.mailgun.org/messages",
      auth=("api", os.getenv("MAILGUN_API_KEY")),
      data={"from": "Wishbliss Mailing List <mailgun@sandboxd7c358e02f26415dbb7329dd994a8334.mailgun.org>",
        "to": ["tad@cmdlabs.io"],
        "subject": "Hello",
        "text": "Testing !!! some !!! weirdness"})
```

    - main.py
```
send_email()
```

- After adding this code, we can test our script again and we should receive an email in our SPAM folder
- Out of courtesy of the time let’s comment out and just test that the email API works…
- python main.py
- If you don’t mind finishing this walkthrough with emails being delivered to SPAM then skip ahead to PART 7
- BUT if you’d like the emails to be delivered to INBOX proper, here are the steps you’ll need to take…
    - Come over to the https://app.mailgun.com/mg/sending/domains page again and click “Add new domain”
    - Then specify the subdomain of some domain you own for example I used the name mail.wishbliss.link (where my domain is wishbliss.link)
    - After you add you domain you’ll be presented with a list of records that you’ll need to add to your domain’s DNS settings through your DNS provider
    - Here is what adding these records to my DNS settings in AWS Route 53 looks like for me reference
    - And after this records are added to our DNS we can click `Verify` to have Mailgun confirm that we are indeed the owner of this domain
    - And now when we send email with an email from our verified domain as the send the emails should land in our INBOX proper
        - noreply@wishbliss.link

If you have issues purchasing a domain or verifying it with your email provider, leave a comment or paste detailed descriptions of your issues into either Google or ChatGPT. If you’ve gotten this far, don’t be discouraged. Setting up emailing from a custom domain is not too difficult but can be tricky if you do something slightly off.

SIDENOTE: If someone in the audience knows of a simpler way to implement email integrations please leave a comment and I’ll pin it to the top of the comments

PART 7 - Deploying the application to GCP

Now we’re going to most fast through making the remaining changes to this PRODUCTION APPLICATION. So pay attention closely!

First of all, we don’t want our research report written to a file but instead would like it delivered to us via email

- Let’s edit the params of our Crew class in the main.py file like so…
	```
	output_pydantic=NewsResults,
        output_file='report.json'
	```
    - This change tells the Manager in our Crew to output a very specific data structure when completing tasks…
    - Let’s test this out so you see what’s happening
    - We see that a “structured” JSON output has been generated by our crew
    - Now we can combine the flexibility of LLMs with the predictability of traditional programming so transform this JSON output into an email with the following code…
        - And we’ll need to add a few more helper functions
        - `touch helpers/is_valid_email.py`
        - `touch helpers/format_news_for_email.py`
    - And now if we test our script again let’s see what happens…
    - PLUS update main.py & send_email.py
    - `python main.py`

GREAT!!!

Next, let’s deploy this application to a Google Cloud Run Job so we automatically get regular reports from our Crew regardless of if our computer is turned on or off…

- In order for that to work though we will need to make our OPENAI_API_KEY and MAILGUN_API_KEY available to any application running in our GCP project
- And here is how we do that…
- GCP offers another API/product in its suite dedicated to storing sensitive data like API_KEYS and passwords
- That product is called Secret Manager

```
gcloud services enable secretmanager.googleapis.com
gcloud services list --enabled
```

Now that this API is enabled on our GCP account, we can store sensitive data in “Secret Manager” like so…

https://console.cloud.google.com/security/secret-manager?referrer=search&hl=en&project=hthaogcrj-practice

```
echo -n "<SECRET>" | gcloud secrets create $SECRET_NAME --data-file=-
```

This is the command template so this is how we would add our OPENAI_API_KEY to “Secret Manager”

& this is how we would add our MAILGUN_API_KEY to “Secret Manager”

```
echo -n "<YOUR_OPENAI_API_KEY>" | gcloud secrets create OPENAI_API_KEY --project $PROJECT_ID --data-file=-
```

https://console.cloud.google.com/security/secret-manager?referrer=search&hl=en&project=hthaogcrj-practice

```
echo -n "<YOUR_MAILGUN_API_KEY>" | gcloud secrets create MAILGUN_API_KEY --data-file=-
```

FYI, as a quick sidenote, this is the command for how to update a secret to have a new value…

```
echo "YOUR_NEW_SECRET_VALUE" | gcloud secrets versions add OPENAI_API_KEY --data-file=-
```

And the way we load these secret values into our Cloud Run is like so…

We add a new flag called `—set-secrets` to the `gcloud run jobs deploy` command of our CICD script and pass in a list of ENVIRONMENT_VARIABLES for our job by referencing them in “Secret Manager”

--set-secrets "OPENAI_API_KEY=projects/${{ env.PROJECT_NUMBER }}/secrets/OPENAI_API_KEY:latest,MAILGUN_API_KEY=projects/${{ env.PROJECT_NUMBER }}/secrets/MAILGUN_API_KEY:latest" \

Let’s push this code to GitHub and then trigger our application in Cloud Run Jobs to confirm we still receive an email…

OK! So thing are looking good but we did get an error saying our “Default compute service account” needs permissions to access our secrets

The “Default compute service account” outlines the permissions given to the Cloud Run API running in our GCP project

So long story short is the following 2 commands will grant our “Default compute service account” permissions to access the two 2 secrets we added to “Secret Manager” 

Make sure the PROJECT_NUMBER variable is defined in your shell

gcloud secrets add-iam-policy-binding OPENAI_API_KEY \
  --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"

gcloud secrets add-iam-policy-binding MAILGUN_API_KEY \
  --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"


Now that we’ve granted these permissions let’s do one more thing that comes to my mind…

Because Multi-Agent systems spit out a lot of text, I often see them consume a lot of memory so let’s double the default amount of memory allocated to the container running our job before redeploying by adding another flag to the deploy step of our CICD script

--memory 1Gi

And now let’s re-run our CICD script in GitHub…

WHILE THE CICD PIPELINE IS IN FLIGHT, show how you might need to tweak a few  “meta” parameters (as we’ll call them) depending on the details of your job ie:

- cpu
- memory
- maxRetries
- timeoutSeconds

Alright that looks like it worked!

Let’s trigger our job to confirm we receive an email

`gcloud run jobs execute job-1 --region us-east1`

And we do indeed see an email arrive in our inbox with an A.I. generated report

Let’s move on…

Next up we’ll add a Monitoring Tool called AgentsOps. AgentsOps will give us quicker and easier insight into how our A.I. Agents are performing compared to observing them through the GCP console. Once you get to point where you have dozens or even hundred of Agents working for you, you’re going to need a tool like AgentOps to easily monitor them all.

PART 8 - Adding AgentOps

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

PART 9 - Wrapping things up

To wrap things up, let’s do 3 things

First let’s update our agents to focus on a different niche so you understand how to customize this application for your own purpose and then set a daily cron job so we automatically get reports delivered to us daily!

Second, let’s re-enable the CRON job and adjust the CRON expression to trigger out Agents once a day…

And third let’s make the list of email recipients a secret so we don’t dox whoever is receiving these reports…

```
echo “tad@cmdlabs.io” | gcloud secrets create AI_NEWS_RECIPIENTS --data-file=-
gcloud secrets add-iam-policy-binding AI_NEWS_RECIPIENTS \
  --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

--set-secrets “AI_NEWS_RECIPIENTS=projects/${{ env.PROJECT_NUMBER }}/secrets/AI_NEWS_RECIPIENTS:latest” \

gcloud run jobs execute job-1 --region us-east1

So that’s all folks. We now have a team of A.I. News Reporters synthesizing information for us across a number of sources.

In conclusion, this entire video can be summed up in 3 words: Welcome to PRODUCTION!

BONUS SECTION: As promised, here’s how you can easily tear down a GCP project. Click SHUT DOWN to destroy all the resources in the project.

STRATEGY - Record each part as a separate Camtasia project…

Then combine them in Premier
