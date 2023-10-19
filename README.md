# bp-python
This is part of the Rising Cloud Boilerplate Repositories. The purpose of
`bp-python-task` and other boilerplate repositories is to quickly get
applications running on Rising Cloud, without having to worry about any of the
basic configuration that is required.

This boilerplate is functional out of the box. If you follow the steps under
the "Using this Boilerplate Repository" without making any changes, you will
have made a fully functioning Rising Cloud Task! If this is your first time
creating a Rising Cloud task of this type, it is recommended to follow those
steps below with no modifications first. After you have seen the build process
and are comfortable with the layour, adjust the code to fit individual needs.

This application demonstrates a working app in base python, with no added
dependencies/libraries/packages. It is intended to use the CLI to create a
task based on this code. If you did not use the CLI, please install it from
[here](https://risingcloud.com/docs/install) before following the rest of the
steps below.

## Rising Cloud Task Overview
See [here](https://risingcloud.com/docs/technicals) for useful information
regarding Rising Cloud Tasks. Additionally, there is more information on
daemons, networking, input/output, workers, and more there.

## Using this Boilerplate Repository

### Requirements
- Python 3.5+
- Docker (To assist with local building and testing)

### Local Testing and Development

There are two ways to test your application locally. You could just define a
request.json in the root folder and run `python3 main.py`. If you are unable
to utilize docker for any reason, this is how you will need to test. However,
it is a much prefered paradigm to test in a docker container. By running
in a container, you ensure that your testing is consistent with deployment. The
provided makefile gives simple bindings necessary to create the image, run the
container, and test requests.

To get the local docker container up and running for testing and development:
1. Ensure you are logged into the risingcloud cli with a valid token:
`risingcloud login`.
1. Run the local risingcloud build command: `risingcloud build --local`.
This will grab the currently pushed yaml from Rising Cloud's repository,
and generate the relevant portion of the dockerfile that Rising Cloud uses
during the normal build step. That dockerfile is then automatically run
locally and will save the resultant image as bp-python-task
1. Start up the test container: `risingcloud run -s`. This spins up the image
that was just built and the `-s` (`start`) flag keeps it running in the
background. It will automatically delete any old running containers of the same
name for you. Your daemons will automatically start up when you run the command.
It will also attach a volume to the container so that you can easily test
changes to your code without requiring a docker build every time. This volumne
matches the working directory with the /app/app directory on the image. You can
skip this step if you'd like, but it's often easier to debug your container if
it is left running in a detached state.
1. Populate any test `request.json` files you'd like to be able to test in
the `/tests/reqeusts` folder. As long as they are named in the format
`{TEST_NAME}.json` and are proper json, they will work fine!
1. To run a test on `request.json`: `risingcloud run -d`. To run any arbitrary
request test through: `risingcloud run -i {INPUT_FILEPATH} -d`. This will copy
the request into `request.json` and then run the `run` command in the testing
docker container. The resultant file will be located at `response.json`.
If you'd like to save the file elsewhere, you can instead run
`risingcloud run -i {INPUT_FILEPATH} -o {OUTPUT_FILEPATH} -d`. If you would
like the container to shut down after processing, you can remove the `-d` flag.
1. To run every test in a folder, run the above commands, but simply point the
`{INPUT_FILEPATH}` and `{OUTPUT_FILEPATH}` to a folder of tests instead. This
folder can have any structure as long as it's base level it contains only json
files.
1. Whenever you're done testing, you can clean up the docker environment with
`risingcloud kill-local`.

For all the above commands, you can expedite testing and remove the prompt
"`No task URL provided. Use "bp-python-task" as your task URL? [y/n]`" by
providing the command with the taskURL in question on the end of the command.
- ex. 1: `risingcloud build --local` -> `risingcloud build --local bp-python-task`
- ex. 2: `risingcloud run -s` -> `risingcloud run -s bp-python-task`
- ex. 3: `risingcloud run -i {INPUT_FILEPATH} -o {OUTPUT_FILEPATH} -d` ->
`risingcloud run -i {INPUT_FILEPATH} -o {OUTPUT_FILEPATH} -d bp-python-task`

### Building/Deploying
Once you have locally tested your app and verified it's functioning as expected,
you may simply run `risingcloud build` (without the `--local` flag). This will
queue a build of your application on the Rising Cloud build servers. You can
monitor the build progress via the link output from the command, or just
navigate to the "Build Status" page of the application you are building.
https://my.risingcloud.com/task/bp-python-task/build-status

### Using the App
When the application is built, how do you use it? First, you can navigate to
https://my.risingcloud.com/task/bp-python-task/ and ensure the app is deployed
by pressing the "Deploy" button on the top right of the page. After the task has
succesfully been started, navigate to the jobs page, which should be located
at https://my.risingcloud.com/task/bp-python-task/jobs.  On the jobs page, you
may press the "New Job Request" button to send a json request to the worker.
If that is successful, you will likely next want to programmatically send jobs
to your worker from elsewhere. Rising Cloud automatically registers a url for
you so you can communicate with your task. The URL for this task is
https://bp-python-task.risingcloud.app/risingcloud/jobs.
For detailed information on how to communicate with your application, see the
docs [here](https://risingcloud.com/docs/task-api).

If you'd like to test the deployment with Postman or Insomnia, you can do that
as well. Open up the `requestCollection.json` file in either application.
Modify the collection as you please, but this should give a good starting point
on how you can interact with your application locally and when it is deployed.
In Postman, the `{{host}}` and `{{auth}}` variables are set in the collection
variables. In Insomnia, they will be imported under the Environment Overrides.

### Securing your App
You can navigate to this page
https://my.risingcloud.com/task/bp-python-flask-service/security and check
"Require app users use an API key to send jobs to this task." to require a key
to be included when commnunicating with your app. The key should be included
as "X-RisingCloud-Auth" in the headers.

### Adding Custom Functionality
This repository is boilerplate for a reason. Please add, edit, and customize
code to your liking for whatever your use case may be. Some code comments were
left in the places where most applications are most likely to add or modify
the boilerplate.