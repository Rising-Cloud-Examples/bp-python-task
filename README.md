# Overview
This is part of the Rising Cloud Boilerplate Series. The purpose of
`bp-python-task` and other the templates is to quickly get you started get you
started building, testing and running code on Rising Cloud, with minimal steps.

This template will provide a working application out of the box. If you
follow the steps under the "Using this Boilerplate" heading without
making any changes, you will have made a fully functioning Rising Cloud Task. If
this is your first time creating a Rising Cloud Task, it is recommended to
follow the steps below first. After you have seen the development and build
process, and have familiarized yourself with the template code, please adjust it
to fit your individual needs.

It is intended to use Rising Clouds Command Line Interface (CLI) to create a
task based on this code. If you have not already installed the CLI, please
install it from [here](https://risingcloud.com/docs/install) before continuing.

TODO: Create and link the page which describes the general terms you might
see while reading this document.

It is recommended to have our
[Rising Cloud Terminology]()
page up while reading through this template.

## bp-python-task
The `bp-python-task` template is a demonstration of the bare minimum necessary
to get a python Rising Cloud Task up and running on the Rising Cloud Platform.
By following the steps below, you will be left with boilerplate code that will
allow you to easily make adaptations for your very own python Rising Cloud Task.

## Rising Cloud Task Overview
This template will create a Rising Cloud Task. Rising Cloud Tasks are best
utilized for large distributed workloads that are heavy on compute (CPU or GPU)
and memory (RAM) resources. A Rising Cloud Task is a serverless function that
fully leverages Rising Cloud's packaging and scaling tools to reduce developers
time and increase application efficiency.

Below are some high level points about Rising Cloud Tasks, along with some links
to our documentation covering Rising Cloud Tasks.

- **Runtime**
  - A Rising Cloud Tasks is a Linux based command line process.
  - For every request that comes in, a single call of your `run` command as
specified in the `risingcloud.yaml` will process.
  - Each instantiation of your Task that is run is run within a Rising Cloud
Worker. The worker manages the communication from your Task to the greater
Rising Cloud ecosystem.
      - The worker is what is responsible for fielding requests and calling
your command line process for each request.
      - The worker is also responsible for starting any daemons you specify
in your `risingcloud.yaml`.
      - The worker does ***not*** maintain the health of your daemons. It is
recommended to check daemon health at the start of processing each request.
      - Each worker on initial load will have a clean filesystem, however, the
worker while running does ***not*** manage local storage. It is recommended
to clean up the local filesystem after each request to ensure new requests
start in the same state.
- **Input/Output**
  - Rising Cloud Tasks communicate to the worker that houses them via an input
and output file.
    - A `./request.json` file will be populated by the Rising Cloud Worker
before it calls your Task. It is your Task's responsibility to read from that
file to gather any information that was POSTed during the request.
    - The worker reads from `./response.json` after your Task exits. It is your
Task's responsibility to ensure that file is populated so a proper response to
each request may be recorded.
- **Build Process**
  - For Rising Cloud Tasks, Rising Cloud builds a Docker image for you based on
your specifications in the `risingcloud.yaml`. For detailed information, check
out our docs on the build process [here]().

TODO: Link the above to the new build page

TODO: Link the below to the new Rising Cloud Task page

See [here]() for useful information
regarding Rising Cloud Tasks.

## Using this Boilerplate

### Requirements

- A Rising Cloud account. If you do not have one, request access
[here](https://risingcloud.com/invitation)
- The Rising Cloud CLI. Download it [here](https://risingcloud.com/docs/install)
- Docker (To assist with local building and testing)
  - The easiest choice to get up and running with Docker is to install the
desktop application [here](https://www.docker.com/products/docker-desktop/).
  - If you would like to install Docker without the desktop application, follow
the official Docker Engine installation instructions for your platform found
[here](https://docs.docker.com/engine/install/).
- Postman or Insomnia (To assist with testing)
  - 


### Setup the Template

1. Navigate to an empty folder on your local system were you would like to
create your project You can name this folder whatever you would like.
   - You may also start from a project/folder that already has code, although
you will not be able to pull from the template if there are any filename
clashes between the template repository and your local files.

1. Start the Task Initialization Wizard by running: `risingcloud init`
   - ***To use this template, be sure to select the "risingcloud" mode when the
wizard prompts you for the mode of your task. Also make sure you specify the
template as "bp-python-task".***
   - For the rest of this document, the Task URL you create for your task will
be referred to as `$TASK_URL`.
   - If you would like to initialize a task without using the initialization
wizard, use this command instead:
`risingcloud init --risingcloud --template bp-python-task $TASK_URL`
   - If this is your first time making a Rising Cloud Task, it is recommended to
use the wizard to familiarize yourself with all the options.

1. Once you have initialized your new Rising Cloud Task, the
template code will populate in your workspace along with a file named
`risingcloud.yaml`. This file is your task configuration.
   - Only the necessary task configuration values for this boilerplate are
included in the `risingcloud.yaml`. If you would like to view all the available
options and learn in more detail what each one does, visit
https://risingcloud.com/docs/config-glossary.
   - The `risingcloud.yaml` could be named something different if you selected
a different config location either during the initialization wizard or by
passing the `--task-config` flag to the init command.
   - Your local template will have a copy of this readme but with all the
instances of the template url replaced with the url you chose in the
initialization process.
   - Before moving on to testing locally, you should have a quick read through
the template files and review the code comments to help orient yourself.

1. You are now ready to test, build and run your new Rising Cloud Task based on
the bp-python-task template.

### Local Testing

Rising Cloud provides a set of tools integrated into the CLI which make testing
and developing your code locally easy. It is recommended to use these tools
during development as they they will streamline your build and deploy process
by mirroring the build and run processes the Rising Cloud Platform
uses as closely as possible in your local environment. Below is a step-by-step
process for how to get this template Rising Cloud Task up and running in your
local development environment.

1. Ensure you are logged into the Rising Cloud CLI:
`risingcloud login`.

1. Run the local Rising Cloud build command: `risingcloud local build`.
   - This will grab the most recent `risingcloud.yaml` from Rising Cloud and
generate a temporary dockerfile that mimics the one Rising Cloud uses to build
during the actual build step.
   - This temporary dockerfile is then used to build an image locally and save
it under the name of your chosen taskUrl.
   - All the steps and logs of the temporary dockerfile will be printed out when
you run the `local build` command.
   - /app/app is the absolute path your working directory will be in the
resulting Docker image.

1. Start up the test container: `risingcloud local start`.
   - This spins up an instance of the image that was just built as a detached
docker container.
   - It will automatically delete any old running containers of the same name
for you.
   - Any daemons specified in the `risingcloud.yaml` will also automatically
start up when you run the command.
   - A volume will be attached to the container so that you can easily test
changes to your code without requiring a docker build every time. This volume
maps your working directory to the /app/app directory on the container.
   - ***This command isn't strictly necessary. If you would prefer to not leave
your container detached while testing locally, you can skip this step.***

1. Populate any test files you'd like to be able to test in
the `/tests/requests` folder.
   - You can put test files anywhere, however this location is standard
practice for the Rising Cloud template repositories.
   - Ensure test files are named in the format `{TEST_NAME}.json` and are
proper JSON format.

1. To run a test file through your container, use: `risingcloud local run`.
   - This command runs the command specified in the `risingcloud.yaml` under the
"run" heading. By default, that is `run: python main.py`
for this template.
   - By default, this will look for a test file to run at `./response.json`
However you can specify any file location with the `--input {INPUT_FILE}` flag.
     - The `--input` flag also supports folders as inputs. If you pass a folder
into the command, it will recursively run through every nested folder and send
every `.json` file through as a test.
   - By default, the resultant file will be saved at `response.json`. However
you can also specify any file location you'd like with the
`--output {OUTPUT_FILE}` flag. Just ensure the parent folder exists if you
specify an output.
     - If you are running a test with an input folder and keep `--output` as
its default value or pass in a file as the output, every request will still be
processed and written to the same output file.
     - You may also specify a folder as the output, although this is only valid
when you pass a folder as the input as well. In this case, the entirety of the
input folder structure will be mimicked into the specified output folder,
allowing you to track all the responses your task gives.
   - This will automatically shutdown the container after it has finished
processing. If you would like to leave it detached, pass the `--detach` flag.
   - If the local container is already running because you previously ran the
run command with the `--detach` flag or you used the `local start` command, it
will not be restarted when using this command.
   - If you would like to force a restart of a detached container (usually this
would be to update daemons or because you are using a compiled language and have
a new binary), simply pass the `--restart` flag to the run command.

1. If you have a container that's detached, either because you passed the
`--detach` flag to the `local run` command, or because you ran the
`local start` command, you can kill it using: `risingcloud local kill`.

For all the above commands, you can expedite testing and remove the prompt
"No task URL provided. Use `$TASK_URL` as your task URL? [y/n]" by
providing the command with your Task URL appended at the end.
- ex. 1: `risingcloud local build` -> `risingcloud local build $TASK_URL`
- ex. 2: `risingcloud local run` -> `risingcloud local run $TASK_URL`
- ex. 3: `risingcloud local run -i {INPUT_FILEPATH} -o {OUTPUT_FILEPATH}` ->
`risingcloud local run -i {INPUT_FILEPATH} -o {OUTPUT_FILEPATH} $TASK_URL`

### Building and Deploying
Once you have locally tested your app and verified it's functioning as expected,
you may simply run `risingcloud build`. This will queue a build of your Task on
the Rising Cloud build servers.

- If you'd like the application to be automatically deployed and available after
the build completes, you may pass the `--deploy` flag into the build command
like so: `risingcloud build --deploy`.
   - If you would prefer to deploy your task through the UI, navigate to
https://my.risingcloud.com/task/$TASK_URL/ and deploy the task
by pressing the "Deploy" button on the top right of the page.
- If you'd like the application to automatically update based on the local task
configuration before pushing, you can add the `--reconfigure` flag into the
build command. This effectively just runs a `risingcloud push` prior to your
build command to ensure everything is synced up before each build. If you have
made local changes to the `risingcloud.yaml`, this is a handy shorthand.

You can monitor the build progress via the link output from the command, through
the `risingcloud status $TASK_URL` command, or just navigate to the
"Build Status" page of the application you are building found here:
https://my.risingcloud.com/task/$TASK_URL/build-status

### Using your Deployed Rising Cloud Task
When the application is built, how do you use it?

#### With Insomnia or Postman
You may test your deployment using Postman or Insomnia. Rising Cloud
automatically registers a url for you so you can communicate with your task.
The URL for your task is https://$TASK_URL.risingcloud.app/risingcloud/jobs.
- Open up the `requestCollection.json` file in either Insomnia or Postman
  - A couple sample requests are included by default, but you can easily
copy in some test json requests you have into the body to test specific cases.
  - In Postman, the `{{host}}` and `{{auth}}` variables are set in the
collection variables.
  - In Insomnia, the `{{host}}` and `{{auth}}` variables will be imported
under the Environment Overrides. 
- For detailed information on how to communicate with your application, see
the docs [here](https://risingcloud.com/docs/task-api).

#### With Our CLI
You may also test your deployment with our CLI. The Rising Cloud CLI has some
built in functions that allow you to queue jobs and view results.
- You can post a job to your task with our CLI using the `risingcloud jobs post`
command. By default, this will send whatever is in `./request.json`, but you
can specify a custom file location with the `--request` flag.
   - This will return with a jobId which you can use to further track your job
- You can check on your job results at any time using the
`risingcloud jobs get --job-id $JOB_ID` command.
   - This command requires you to pass in a jobId via the `--job-id` flag.
   - If you would like full run logs to also be returned, you may also pass the
`--debug` flag to this command.
- You can kill a processing job at any time with
`risingcloud jobs kill --job-id $JOB_ID`
   - The `--job-id` flag is required for this command as well

***If your task has an API key enabled, you can pass your desired key
with the `--auth $KEY` flag to all of the above commands.***

If you'd like, you may also just make a curl commands to your task if you are
more comfortable with that. All the documentation regarding task routes can be
found [here](https://risingcloud.com/docs/task-api).

#### With our UI
Our UI also allows you to queue and view jobs for your newly created task.
- After the task has successfully started, navigate to the jobs page, located at
https://my.risingcloud.com/task/$TASK_URL/jobs.
- On the jobs page, you may press the "New Job Request" button to send a json
request to the worker. (You can just grab one of the test requests you have
locally and copy it into the prompt)
- You can click view all the associated job information by selecting within the
job row itself.

### Securing your Task
If you would like to restrict access to your Task, you can do so either through
our CLI or UI.

#### CLI
You can add a key to your Task with the `risingcloud key add $TASK_URL` command. 
- The `--name $NAME` flag sets the name for the flag so it is easily
identifiable. If you leave this empty, a default random name will be provided.
- The `--key $KEY` flag allows you to specify the specific value of your key.
If you leave this empty, a default random key value will be provided.

You can remove a key with the `risingcloud key remove $TASK_URL` command. You
are also able to view all current keys with just `risingcloud key $TASK_URL`.

#### UI
Navigate to: https://my.risingcloud.com/task/$TASK_URL/security and check
"Require app users use an API key to send jobs to this task." This will make it
so that all requests to your jobs endpoint will require a key to be included
when they are sent. The key should be included as "X-RisingCloud-Auth" in the
headers of the request.

### Adding Custom Functionality
This template repository is intended to be a boilerplate and a jump-start for
Python Tasks.

Please add, edit, and customize this code to your liking for whatever your
specific use case may be. Code comments were left throughout the template to
make it easier to understand where modifications will likely need to be made.
Additionally, below is a list of common modifications you might like to make
and how you would do them:

TODO: Create the pages for the below links and insert them into this guide
   - Build Process
   - Daemons

1. **Changing your Base Image:** Some code might require you to utilize a
different base image than what is provided in this template. This is as simple
as modifying `from` in the `risingcloud.yaml`.
   - As a general rule, you should try and keep your images as lightweight as
possible.

1. **Adding Dependencies:** To add dependencies, read through and follow the
information provided in the commented `risingcloud.yaml` file.
   - If you still would like more help or want more advanced information, check
out our docs page on the build process [here]().

1. **Adding a Daemon:** To learn more about when you would want to use a daemon,
how to create one, and some rules of thumb for using them, see our docs page
[here]().

TODO: Add Daemon link above when the daemon page is created

1. If you need to add any dependencies to your project, you can add them to the
`requirements.txt` in the root directory. By default, this file is empty, but
the it is still included to make it clear how you would go about adding those
dependencies in the `deps` section of the configuration.
