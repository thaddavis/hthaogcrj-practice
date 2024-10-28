# PART 1 - Setting up our Development environment

You can watch this video without coding along BUT in case you do, here’s what you’ll need…

- A computer ie: a Laptop or Desktop with Docker and VSCode installed
    - don’t forget to install the “Docker” and “Dev Containers” VSCodes extensions too
- A GCP account
- An OpenAI Account

You’ll need a laptop (or Desktop) with Docker and VSCode installed
	- And don’t forget to install 2 VSCode extensions namely the `Docker` extension and the `Dev Containers` extension

You’ll also need a GCP account. You can get a GCP account by coming over to https://cloud.google.com and signing up OR by simply activating your GCP account on the https://cloud.google.com/cloud-console page if you already use gmail

You should get some free credits on sign up and the cost of what we’re doing in this video with GCP will be practically free.

And for powering our AI Agents, we’ll be using OpenAI. We can later switch to other LLM providers but for the purpose of keeping things simple we’ll go with OpenAI for now. Sign up on https://platform.openai.com and later in this video we’ll show how to quickly set it up if you haven’t already.

Let me know in the comments if you have issues installing Docker, VSCode, or signing up for either GCP or OpenAI.

SEVERAL BORING MOMENTS LATER…

Ok I’m assuming you’ve set everything up, so let’s get started by creating a folder on our file system…

I’m going to call mine (`mkdir hthaogcrj`)

and let’s open this folder using VSCode…

If we quickly pop open VSCode’s terminal we can confirm where we are on the file system…

```pwd`` and we are indeed in the empty folder we just created

As we are starting from scratch, let’s first set up our “Development Environment”…

By “Development Environment” we mean the tools and software that we as creators of this application will use to build it…

Kitchen : Food :: Development Environment : Application

So inside this empty folder we just created, let’s create the following folder and files…

```
mkdir .devcontainer
touch .devcontainer/devcontainer.json
touch Dockerfile.dev
```

And populate the devcontainer.json with this content 
And populate the Dockerfile.dev with this content

The code we just added looks a bit hectic but it’s actually quite useful.

These files will build a little mini-computer that will run on top of our actual computer. This mini-computer, called a “Docker Container”, is where we will write all the code for powering our team of A.I. News Reporters.

When we’re finished with this walkthrough, we’ll delete this “Docker Container” (or mini-computer) and our base machine (aka our laptop or Desktop or whatever we’re using) will be left clean as if nothing ever happened…

In addition to helping us stay organized, these “Docker containers” are also highly compatible with Cloud platforms like AWS, GCP, and Azure so using them for Development will make running our application in the cloud a breeze as we’ll shortly see.

The code we just added will build us a “Docker Container” (or “kitchen”) with some amazing software installed like Python, .git, gcloud, and Docker itself

And yes you heard that correctly. We will be installing a Docker client into our Docker Container and configuring it to communicate with the Docker daemon (or server) running on our base machine.

https://docs.docker.com/get-started/docker-overview/#docker-architecture

Metaphorically, these softwares are like the oven, microwave, utensils, & fridge that make up a kitchen. In the same way that we would use combinations of kitchen components to cook amazing food, we will use these softwares to build amazing applications…

When we use a “Docker Container” for the purpose of developing software in it, we call it a “Dev Container”…

Moving along…

If we type these key strokes, SHIFT + COMMAND + P, we’ll pop open the command palette in VSCode (as it’s so called) and we can select an option called “Reopen in Container” to trigger a script provided by the “Dev Containers” extension that will build a “Docker Container” based on the config we’ve specified. After the Docker build process has completed, we will see that VSCode is connected to the /code folder at the root of the Dev container and NOT the original folder we first opened.

Let’s confirm all the software we’ll need is indeed installed in this Dev container…

```sh
python --version
git -v
gcloud --version
docker version
```

And everything is looking good.

<FIRST_GIT_TAG> and include README.md too 🔑