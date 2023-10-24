# Overview
This is part of the Rising Cloud Boilerplate Repositories. The purpose of
`template-url` and other template repositories is to quickly get
you started running and building code on Rising Cloud, without having to spend
time figuring out which specific advanced options Rising Cloud provides are
necessary for your workload.

This template is functional out of the box. If you follow the steps under the
"Using this Boilerplate Repository" heading without making any changes, you
will have made a fully functioning Rising Cloud Task! If this is your first
time creating a Rising Cloud Task, it is recommended to follow those steps
below first. After you have seen the development and build process and you have
familiarized yourself with the template code, please adjust it to fit your
individual needs.

This template demonstrates a {INSERT_SPECIFIC_TEMPLATE_DESCRIPTION_HERE},
with no additional dependencies/libraries/packages.

It is intended to use the CLI to create a task based on this code. If you did
not use the CLI to clone this repository, please install it from
[here](https://risingcloud.com/docs/install) before following the rest of the
steps below.

TODO: Create and link the page which describes the general terms you might
see while reading this document.

Additionally, it is recommended to have our
[Rising Cloud Terminology]()
page up while reading through this template doc in case you encounter a term 
or phrase you have not seen before.

## Rising Cloud Task Overview
This template is a Rising Cloud Task. Rising Cloud Tasks are best utilized for
large distributed workloads that hare heavy on compute and memory resources.
They also are able to fully leverage Rising Cloud's proprietary scaling tools
which allows for performace improvements during cold start time and volatile
work loads.

Below are some high level points about what being a Rising Cloud Task means
along with some links to our documentation covering Rising Cloud Tasks.

- **Runtime**
  - A Rising Cloud Tasks is a command line process.
  - For every request that comes in, a single call of your `run` command as
specified in the `risingcloud.yaml` is expected to process it.
  - Each instantiationg of your Task is run with a Rising Cloud Worker. This
worker manages the communication from your Task to the greater Rising Cloud
ecosystem.
      - This worker is what is responsible for fielding requests and calling
your command line process for each request.
      - The worker is also responsible for starting any daemons you specify
in your `risingcloud.yaml`.
      - The worker does ***not*** maintain the health of your daemons. It is
recommended to check daemon health at the start of processing each request.
      - The worker also does ***not*** manage local storage. It is recommended
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

## Using this Boilerplate Repository

### Requirements

- {INSERT_OTHER_REQUIREMENTS_HERE}
- Rising Cloud CLI. Download it [here](https://risingcloud.com/docs/install)
- Docker (To assist with local building and testing)
  - TODO: How to install docker with Docker Desktop (prefered as it is
compatible with every major os).
  - TODO: How to install docker on your specific system in isolation. Just find
a link to a public install page for docker that can walk someone through it.

### Setup the Template

1. Navigate to an empty folder were you would like to create your project.
   - You may also start from a project/folder that already has code, although
you will not be able to pull from the template if there are any filename
clashes between the template repository and your local files.
1. Start the Task Initialization Wizard by running: `risingcloud init`
   - ***To use this template, be sure to select the "risingcloud" mode when the
wizard prompts you for the mode of your task. Also make sure you specify the
template as "template-url".***
   - For the rest of this document, the Task URL you create for your task will
be referred to as `$TASK_URL`
   - If you would like to initialize a task without using the initialization
wizard, use this command instead:
`risingcloud init --risingcloud --template template-url $TASK_URL`
   - If this is your first time making a Rising Cloud Task, it is recommended to
use the wizard to familiarize yourself with all the options you have when
initializing a task.
1. Once you have initialized your new Rising Cloud Task with no errors, the
template code should populated in your workspace along with a file named
`risingcloud.yaml`. This file is your task configuration.
   - The `risingcloud.yaml` could be named something different if you selected
a different config location either during the initialization wizard or by
passing the `--task-config` flag to the init command.
   - Your local template will have a copy of this readme but with all the
instances of the template url replaced with the url you chose in the
initialization process.
   - Before you begin testing locally, you should have a quick read through the
template files. There are a lot of comments in the code to help orient you.
1. You are now ready to test and then build your new Rising Cloud Task based on
the template-url template.

### Local Testing

Rising Cloud provides a set of tools integrated into the CLI which make testing
and developing your code locally easy. It is recommended to use these tools
during development as they they will streamline your build and deploy process on
the Rising Cloud Platform by mirroring the build and run processes the Platform
uses as closely as possible in your local environment. Below is a step-by-step
process for how to get this template Rising Cloud Task up and running in your
local development environment.

1. Ensure you are logged into the Rising Cloud CLI with a valid token by:
`risingcloud login`.
1. Run the local Rising Cloud build command: `risingcloud local build`.
   - This will grab the most recent `risingcloud.yaml` from Rising Cloud and
generate a temporary dockerfile that mimics the one Rising Cloud uses to build
during the actual build step. That dockerfile is then built locally and the
resultant image is saved under the name of your chosen taskUrl.
   - /app/app is the absolute path your working directory will be located at in
the resulting Docker image.
1. Start up the test container: `risingcloud local start`.
   - This spins up the image that was just built as a detached docker container.
   - It will automatically delete any old running containers of the same name
for you.
   - Any daemons specified in the `risingcloud.yaml` will also automatically
start up when you run the command.
   - A volume will be attached to the container so that you can easily test
changes to your code without requiring a docker build every time. This volumne
maps your working directory to the /app/app directory on the container.
   - ***This command isn't strictly necessary. If you would prefer to not leave
your container detached while testing locally, you can skip this step.***
1. Populate any test files you'd like to be able to test in
the `/tests/reqeusts` folder.
   - You can put test files anywhere, however this location is standard
practice for the Rising Cloud template repositories.
   - Ensure test files are named in the format `{TEST_NAME}.json` and are
proper json or else they will not be consumed by Rising Cloud.
   - {INSERT_SPECIFIC_TEMPLATE_REQUEST_REQUIREMENTS_HERE}
1. To run a test file through your container, use: `risingcloud local run`.
   - This command runs the command specified in the `risingcloud.yaml` under the
"run" heading. By default, that is `{INSERT_TEMPLATE_RUN_COMMAND}`
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
processed, they will just keep writing to the same output file.
     - You may also specify a folder as the output, although this is only valid
when you pass a folder as the input as well. In this case, the entirety of the
input folder structure will be mimicked into the specified output folder,
allowing you to track all the responses your task gives.
   - This will automatically shutdown the container after it has finished
processing. If you would like to leave it detached, pass the `--detach` flag.
   - If the local container is already running because you previously ran the run
command with the `--detach` flag or you used the `local start` command, it will
not be restarted when using this command.
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
the Rising Cloud build servers. You can monitor the build progress via the link
output from the command, or just navigate to the "Build Status" page of the
application you are building found here:
https://my.risingcloud.com/task/`$TASK_URL`/build-status

If you'd like the application to be automatically deployed and available after
the build completes, you may pass the `--deploy` flag into the build command
like so: `risingcloud build --deploy`

### Using your Deployed Rising Cloud Task
When the application is built, how do you use it? 
1. Navigate to https://my.risingcloud.com/task/`$TASK_URL`/ and deploy the task
by pressing the "Deploy" button on the top right of the page if you did not
pass the `--deploy` flag to the build command.
1. After the task has succesfully started, navigate to the jobs page, located at
https://my.risingcloud.com/task/`$TASK_URL`/jobs.
1. On the jobs page, you may press the "New Job Request" button to send a json
request to the worker. (You can just grab one of the test requests you have
locally and copy it into the prompt)
1. You may also test the deployment using Postman or Insomnia. Rising Cloud
automatically registers a url for you so you can communicate with your task.
The URL for this task is https://`$TASK_URL`.risingcloud.app/risingcloud/jobs.
   - Open up the `requestCollection.json` file in either Insomnia or Postman
     - A couple sample requests are included by default, but you can easily
copy in some test json requests you have into the body to test specific cases.
     - In Postman, the `{{host}}` and `{{auth}}` variables are set in the
collection variables.
     - In Insomnia, the `{{host}}` and `{{auth}}` variables will be imported
under the Environment Overrides. 
   - For detailed information on how to communicate with your application, see
the docs [here](https://risingcloud.com/docs/task-api).

### Securing your Task
If you would like to restrict access to your Task, you can navigate to:
https://my.risingcloud.com/task/`$TASK_URL`/security and check
"Require app users use an API key to send jobs to this task." This will make it
so that all requests to your jobs endpoint will require a key to be included
when they are sent. The key should be included as "X-RisingCloud-Auth" in the
headers of the request.

### Adding Custom Functionality
This template repository is created to be a boilerplate and a jumpstart for
anything you could build on our platform using {INSERT_TEMPLATE_USE_CASE}.
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
possible as this allows Rising Cloud to more quickly move your workers around
when necessary.
1. **Adding Dependencies:** To add dependencies, read through and follow the
information provided in the commented `risingcloud.yaml` file.
   - If you still would like more help or want more advanced information, check
out our docs page on the build process [here]().
1. **Adding a Daemon:** To learn more about when you would want to use a daemon,
how to create one, and some rules of thumb for using them, see our docs page
[here]().
1. {INSERT_COMMON_MODIFICATIONS}
