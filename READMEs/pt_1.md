# PART 1 - Setting up our Dev Container

Welcome! So I’m assuming you have at least these prerequisites set up on your computer…

- Docker
- VSCode or Cursor (I’ll be using VSCode)
- The `Docker` extension
- The `Dev Containers` extension
- A GitHub account
- And a GCP account

Let’s get started by creating a folder somewhere on our machine (for example somewhere in the Home folder perhaps, it’s up to you)…

I’m going to call my folder (`mkdir hthtogcrj`)

Let’s open this folder using our editor…

And if I pop open VSCode’s terminal to confirm where we are on the file system you can see we’re in the empty folder we just created (pwd)

Let’s now set up our “Dev Container”…

If you unfamiliar with the term “Dev Container”, hold tight, it’ll make sense in a few minutes…

Inside of this empty folder, we’ll create the following folder and files…

```
mkdir .devcontainer
touch .devcontainer/devcontainer.json
touch Dockerfile.dev
```

And let’s populate the devcontainer.json with this content 
And populate the Dockerfile.dev with this content

The code we just added looks a bit hectic but it’s actually quite useful.

These files will build a little mini-computer that will run on top of our actual computer. This mini-computer, called a “Container”, is where we’ll write almost all the code for powering our application

When finishing this walkthrough, we can easily delete this “Container” (or mini-computer) to keep our base machine (aka our laptop or Desktop or whatever we’re using) clean as if nothing ever happened to it…

In addition to helping us stay organized, the use of “Containers” is highly compatible with Cloud platforms like AWS, GCP, and Azure. So using them for development will make running our application in the cloud easy as we’ll shortly see.

To shed some light on what these files are doing, the Dockerfile.dev does most of the work of configuring our “Container” while the devcontainer.json mostly outlines how our editor should connect to this “Container” and allow us to edit the files inside of it.

If we take a closer look at the Dockerfile.dev, we see it’s creating a “mini-computer” for us that comes installed with Python, .git, gcloud, and a Docker client (we’re installing a Docker client so we can send instructions to the Docker server on our base machine from inside the Container)

If we take a closer look at the devcontainer.json, we see it’s telling VSCode to open the /code folder in this “mini-computer” when attaching to it.

https://docs.docker.com/get-started/docker-overview/#docker-architecture

FYI: When we use a “Docker Container” for the purpose of developing applications in it, we call it a “Dev Container”…

In the coming sections, we will use another “Container”, almost identical to this “Dev Container”, but for running our application in GCP. We’ll refer to this 2nd container as our “Production Container”. 

Don’t worry if this is confusing to you. It’ll all make sense shortly. Let’s move on…

If we type these key strokes into VSCode or Cursor, SHIFT + COMMAND + P, we’ll pop open the “Command Palette” (as it’s so called) and we can search & select an option that says “Reopen in Container” to trigger a script provided by the “Dev Containers” extension that will build a “Docker Container” based on the configuration we’ve just specified.

Before we select this option tho, let’s take a look at the Docker Desktop UI that we got when installing Docker to can compare the before and after of happens when “Reopening our project folder” in a container”…

At the moment we see that the Docker GUI shows no Containers, no Images, and no Volumes.

Let’s now select the “Reopen in Container” option in the command palette and watch what happens…

You will have a wait few moments the first time you build a “Dev Container” BUT after it’s built, launching it will only take a few seconds…

After the Container has finished building let’s take another look at the Docker Desktop UI…

We see blah, blah, blah. What this all means will make sense shortly…

If we come back to VSCode and pop open the built-in terminal again to confirm where we are on the file system now, we see that VSCode is connected to the /code folder at the root of the Dev container and NOT the original folder we first opened.

We’ll be building our PRODUCTION application inside of this Dev Container…

Let’s quickly confirm all the software we’ll need is indeed installed…

```sh
python --version
git -v
gcloud --version
docker version
```

And everything’s looking good.

Let’s save our progress so far in a remote .git repository on GitHub.

- https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials
- https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git

“Dev Containers” built with VSCode offer support for connecting to .git repos via both ssh AND https BUT for demonstration purposes we’ll use HTTPS. The long story short of how this works is the .git credentials set up on our base machine get shared with the “Dev Container” automatically behind the scenes.

Let me show you what I mean…

1st let’s create a repo in GitHub — I’ll call mine `hthtogcrj`. And then let’s configure our project folder to use this GitHub repository for storing backups of all the code we write along our journey by entering the following commands…

```
git init
git remote add origin https://github.com/thaddavis/hthaogcrj-practice.git
```

If I delete the credential for github.com in my MacOS’s built in credential management application, Keychain Access, you’ll see my attempts to push code to the repo fail on my base machine as well as in the Dev Container…

FYI/SIDENOTE/TMI: If you’re following along as a Windows or Linux fan, the corresponding credential management application I believe would be Credential Manager and libsecret respectively…

Anyways, if I re-authenticate with GitHub in my base environment, I’ll use GitHub’s new Personal Access Token (PAT) feature to only include `Contents` and `Metadata` permissions for the repo we just created

And now, we can see that the .git push commands now work on both the base machine and in the Dev Container…

We probably won’t need to use this PAT again but just in case we do store it somewhere safe for example I’ll store it in a .env file at the root of the project. Worst case scenario, you’ll have to generate a new one if you lose it.

```
touch .env
```

We will be storing sensitive data in this .env file, let’s add a .gitignore to make sure it never gets uploaded to GitHub

And Because this video is NOT a deep dive on GitHub, we’ll leave it there for now…

PRO TIP: If you have issues connecting to your remote .git repository from inside the “Dev Container”, just use a terminal on your host machine for interacting with GitHub as backup.

Now let’s move on to PART 2!