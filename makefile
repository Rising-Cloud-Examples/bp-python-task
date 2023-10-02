#############################
# Application Make Commands #
#############################

####################
# RC Make Commands #
####################

# Grabs the dockerfile Rising Cloud uses to build the application
# and builds the image locally. The image name will match the task-url.
rc-build-test-image:
	risingcloud build --local

# Spin up the test-container. Stop and delete an old one if it exists.
# The test container will be doing nothing until we `docker exec` a command
# onto it. This way we can hijack the run process to run tests in
# the container mimicking how the task would run on Rising Cloud.
rc-start-container:
	make rc-kill-container
	docker run -i -d --entrypoint="bash" --name bp-python-task --volume ${PWD}:/app/app bp-python-task
	make rc-start-daemons

# Start all the daemons for the container. For every daemon you have,
# add a line below in the form: `docker exec -d bp-python-task {DAEMON_COMMAND}`
# Ensure each daemon you add here is replicated in
# the risingcloud.yaml under "daemons:"
rc-start-daemons:
#	docker exec -d bp-python-task {DAEMON_COMMAND}

# Stops and removes the existing bp-pyton-task container
rc-kill-container:
	docker stop bp-python-task || true
	docker rm bp-python-task || true

# Tests a single request. This assumes the test container is already up and
# running and the request file is passed in as $(f). The resulting data will
# be saved in ./rcTests/responses/$(f).
# Example usage: `make rc-test-single f={TEST_NAME}`
# Don't include the full path to the test. The command will automatically
# look for it in the ./rcTests/requests folder and add the .json extension.
rc-test-single:
	docker exec bp-python-task /bin/bash ./rcFunctions/runTest.sh $(f)

# Iterates through every test file in ./rcTests/requests and writes the output
# of every test file to ./rcTests/responses under the same name.
rc-test-all:
	docker exec bp-python-task /bin/bash ./rcFunctions/runTests.sh
