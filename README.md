# bp-python
This is part of the Rising Cloud Boilerplate Repositories. The purpose of
`bp-python` and other boilerplate repositories is to quickly get applications
running on Rising Cloud, without having to worry about any of the basic
configuration that is required.

The boilerplate is functional out of the box. If you follow the steps under
the "Using this Boilerplate Repository" without making any changes, you will
have made a fully functioning Rising Cloud Task! If this is your first time
creating a Rising Cloud task of this type, it is recommended to follow those
steps below with no modifications first. After you have seen the build process
and are comfortable with the layour, adjust the code to fit individual needs.

This application demonstrates a working app in base python, with no added
dependencies/libraries/packages. It is intended to use the CLI to create a
task based on this code. If you did not use the CLI, please install it from
[here](https://risingcloud.com/docs/install) and follow the steps shown
[here](TODO: Insert CLI command link here) to begin.

## Rising Cloud Task Overview
See [here](https://risingcloud.com/docs/technicals) for useful information
regarding Rising Cloud Tasks. Additionally, there is more information on
daemons, networking, input/output, workers, and more there.

## Using this Boilerplate Repository

### Requirements
- Python 3.5+
- Docker (To assist with local building and testing)
- Support for `make` commands (To assist with local building and testing)

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
2. Run the local risingcloud build command: `risingcloud build --local`.
This will grab the currently pushed yaml from Rising Cloud's repository,
and generate the relevant portion of the dockerfile that Rising Cloud uses
during the normal build step. That dockerfile is then automatically run
locally and will store the resultant image under the taskurl.
3. Start up the test container: `make rc-start-container`. This spins
up the image that was just built and keeps it running in the background. It
will automatically delete any old running containers of the same name for you.
If you have any daemons, be sure to add them under the `make rc-start-daemons`
command. They will automatically start up when you run the below command.
It will also attach a volume to the container so that you can easily test
changes to your code without requiring a docker build every time.
4. Populate any test `request.json` files you'd like to be able to test in
the `/rcTests/reqeusts` folder. As long as they are named in the format
`{TEST_NAME}.json` and are proper json, they will work fine!
5. To run a single request test through: `make rc-test-single f={TEST_NAME}`.
This will copy the request into `./request.json` and then run `python3 main.py`
in the docker container. The resultant file will be located at `./response.json`
as well as in `rcTests/responses` folder. For this command to work, the file
`/rcTests/requests/{TEST_NAME}.json` must exist.
6. To run every test in the `/rcTests/requests/` folder in sequence:
`make rc-test-all`.This will essentially run the `rc-test-single` over
and over for every test file defined.
7. Whenever you're done testing, you can clean up the docker environment with
`rc-kill-container`.

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
you so you can communicate with your task. The URL for this tasks should be
https://bp-python-task.risingcloud.app/risingcloud/jobs.
For detailed information on how to communicate with your application, see the
docs [here](https://risingcloud.com/docs/task-api).

### Adding Custom Functionality
This repository is boilerplate for a reason. Please add, edit, and customize
code to your liking for whatever your use case may be. So code comments were
left in the places where most applications are most likely to add or modify
the boilerplate.