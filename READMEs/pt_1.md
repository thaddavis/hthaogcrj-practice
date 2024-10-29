# PART 1 - Setting up our Dev Container

Welcome! So I’m assuming you have the following prerequisites set up on your personal computer…

- Docker
- VSCode
- The `Docker` VSCode extension
- The `Dev Containers` VSCode extension
- Credentials for connecting to a GitHub account
- And credentials for using a GCP account

Let’s get started by creating a folder somewhere on our machine that keeps us organized (for example the Desktop or Home folder perhaps)…

I’m going to call my folder (`mkdir hthtogcrj`)

and let’s open this folder using VSCode…

If we pop open VSCode’s terminal we can confirm where we are on the file system…

```pwd``` and we are indeed in the empty folder we just created

As we’re starting from scratch, let’s 1st set up our “Dev Container”…

If you unfamiliar with the term “Dev Container” hold tight, it’ll make sense in a few minutes…

Inside of this empty folder let’s create the following folder and files…

```
mkdir .devcontainer
touch .devcontainer/devcontainer.json
touch Dockerfile.dev
```

And populate the devcontainer.json with this content 
And populate the Dockerfile.dev with this content

The code we just added looks a bit hectic but it’s actually quite useful.

These files will build a little mini-computer that will run on top of our actual computer. This mini-computer, called a “Docker Container”, is where we will write all the code for powering our application

When we’re finished with this walkthrough, we can delete this “Docker Container” (or mini-computer) and our base machine (aka our laptop or Desktop or whatever we’re using) will be left clean as if nothing ever happened…

In addition to helping us stay organized, “Docker Containers” are also compatible with Cloud platforms like AWS, GCP, and Azure so using them for development will make running our application in the cloud easy as we’ll shortly see.

The Dockerfile.dev does most of the work of configuring our “Docker Container” while the devcontainer.json file mostly outlines how VSCode should connect to the “Docker Container” and allow us to edit the files inside of it.

The Dockerfile.dev is creating a “mini-computer” that comes with Python, .git, gcloud, and Docker installed WHILE the devcontainer.json file is telling VSCode to, by default, open the /code folder in this “mini-computer” when we want to view files inside of it among other things like, for example, on lines 24 & 25 we’re are configuring the Docker client installed in the “Docker Container” to forward commands to the Docker server running on our base machine…

https://docs.docker.com/get-started/docker-overview/#docker-architecture

When we use a “Docker Container” for the purpose of developing applications in it, we call it a “Dev Container”…

In the coming sections, we will use another “Docker Container” that is almost identical to our “Dev Container” for running our application in GCP. We will refer to this 2nd container as our “Production Container”. Don’t sweat it if this confusing. It’ll makes sense shortly. Let’s move on.

If we type these key strokes into VSCode, SHIFT + COMMAND + P, we’ll pop open the “Command Palette” (as it’s so called) and we can select an option called “Reopen in Container” to trigger a script provided by the “Dev Containers” extension that will build a “Docker Container” based on the configuration we’ve specified.

Before we select this option though, let’s look at the Docker Desktop GUI that comes with Docker to compare the before and after…

At the moment we see that the Docker GUI shows no Containers, Images, or Volumes.

Now let’s select the “Reopen in Container” option and see what happens…

You will have a wait few moments the first time you build this “Dev Container” BUT after it’s built, launching it will only take a few seconds…

Now that the Container is finished building let’s take another look at the Docker Desktop GUI…

We see blah, blah, blah. This will make sense shortly…

If we come back to VSCode and pop open the built-in terminal again to confirm where we are on the file system, we will see that VSCode is connected to the /code folder at the root of the Dev container and NOT the original folder we first opened.

We will continue developing our application inside of this Dev Container…

Let’s quickly confirm all the software we’ll need is installed…

```sh
python --version
git -v
gcloud --version
docker version
```

And everything’s looking good.

Before moving to PART 2, let’s save our progress in a remote .git repository. We will be using GitHub.

- https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials
- https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git

There are multiple ways to authenticate a .git client with remote repository, for example, after creating a repo in GitHub you can connect to it via SSH or HTTPS protocol. Dev Containers offer built-in support for connecting to .git repos via both of these protocols BUT for demonstration purposes we’ll use HTTPS. Long story short, how this works is the credentials that are set up on our base machine get shared with the “Dev Container” automatically in the background.

Let me show you what I mean…

1st let’s create a repo in GitHub — I’ll call mine `hthtogcrj`. And then let’s configure our project folder to use this GitHub repository for storing a backup of all the changes we make by entering the following commands…

```
git init
git remote add origin https://github.com/thaddavis/hthaogcrj-practice.git
```

If I delete the credential for github.com in MacOS’s built in credential management application, called Keychain Access, you’ll see that my attempts to push code to the repo fail both on my base machine as well as in the Dev Container…

If I re-authenticate in the base environment using a GitHub Personal Access Token (PAT) that contains the permissions to view and edit the contents of this repo we just created, we can see the .git commands now work on both the base machine and in the Dev Container…

If we need more permissions attached to this PAT we can always add them later in the GitHub console…

In practical terms here’s the difference between the authentication options offered by GitHub…

- Authenticating via SSH protocol is the most permissive. It’ll allow you to interact with all repos in your GitHub account
- Authenticating via HTTPS offer fine-grained access control. It allows you to specify exactly which data in your GitHub account a machine can access

Because this video is NOT a deep dive on GitHub, we’ll leave it there…

If you have issues connecting to your remote .git repository in the “Dev Container”, you can use a terminal on your host machine for interacting with GitHub as PLAN B.

So let’s save all our code so far.

<FIRST_GIT_TAG> and include README.md too 🔑

And no that we have our code stored in GitHub let’s continue on to PART 2!