# Spanner CI #

## Table of Contents
* [Introduction](#introduction)
* [How It Works](#how-it-works)
* [Creating An Account](#creating-an-account) 
* [Projects](#projects)
* [Jobs](#jobs)
* [Environment Variables](#environment-variables)
* [Configuration with .spannerci.yml](#configuration-with-spannerciyml)
* [Test Scripts](#test-scripts)
* [Testboards](#testboards)
* [Spanner CLI](#spanner-cli)
* [Examples](#examples)

## Introduction
[Spanner CI](https://spannerci.com) is a Continuous Integration Platform for IoT and Embedded Devices. It can be used for automated code quality checks, automated firmware builds and automated functional tests in real hardware that run with every new version of your firmware.

This repository contains everything that is needed to get started with Spanner CI. It's highly recommended to make a fork of this repository and use it as a starting point to understand how Spanner CI can be easily integrated with your own github repository. More details about this can be found in the [Examples](#examples) section.

In the following sections you'll find detailed information about Spanner CI.

## How It Works
As soon as we create an account and make a new Project in Spanner CI Platform, we can add a [.spannerci.yml](#configuration-with-spannerciyml) configuration file in the root directory of our source code repository to trigger Spanner CI for every commit or pull request. Each time Spanner CI is triggered, it reads the instructions from `.spannerci.yml` file and starts one or more virtual environments for firmware code quality checks, firmware builds or functional testing of the hardware. In the latter case, a user-defined test script is provided in the `.spannerci.yml` file that contains all the device functional tests. Before running the tests, each device under test is updated with the new firmware. Moreover, a Spanner [Testboard](#testboards) can be used to test all inputs and outputs of our device. The Testboard is connected both with the device (wired or wireless) and with the Spanner Platform over the network. Please make sure to check the [Examples](#examples) section for more details.

## Creating an Account
If you haven't used Spanner CI before, you can create a new account by visiting the [Create an Account](http://console.spannerci.com/app/accounts/register) page. To sign-up, you can either use your GitHub account (recommended) or create a new account directly from Spanner.

#### Option 1: Sign-Up with GitHub ###
If you already have a GitHub account click the `SIGN UP WITH GITHUB` button. This will redirect you to GitHub to authorize and install the Spanner App and then you'll be automatically sign-in to the Spanner CI Platform where you can fill your organization info and start using Spanner. That's the recommended way to sign-up because it doesn't require further actions regarding the Spanner integration with GitHub. Details about the GitHub integration can be then found under the [Integrations](http://console.spannerci.com/app/integrations) page. 

#### Option 2: Regular Sign-Up ###
1. Enter your basic information and click `REGISTER` to continue.
2. Use the credentials provided above to sign-in.
3. Enter your organization info to access the Spanner UI. Next step is to integrate Spanner CI with GitHub.
4. Go to the [Integrations](http://console.spannerci.com/app/integrations) page under the Organization section.
5. Under the available integrations, click the `GitHub App` and then the `Add! ` button. This will redirect you to GitHub to authorize and install the Spanner CI App, which will complete the integration with GitHub.

#### About the Spanner CI App in GitHub
Spanner provides an official Github Spanner CI Application for easy integration with GitHub. This authorises the Spanner CI platform to access Github repositories. The application can be found at: https://github.com/apps/spannerci-app and will be installed as described in the above steps. 

## Projects
Spanner supports the creation of one or more Projects for working with different repositories. Each Project represents one user repository. To create a new Project:

1. Select Projects from the navigation menu on the left side of the dashboard.
2. Click on New Project.
3. Select the preferred source code repository.
4. Add one or more [Testboards](#testboards).
5. Click Finish to complete the Project creation.

## Jobs
Each time Spanner CI is triggered from a source code commit or pull request a new Job is created automatically. Every Job gets the instructions on what to do from the [.spannerci.yml](#configuration-with-spannerciyml) file and then runs inside a virtual environment. Upon completion, Jobs provide the output result for each running stage and the resulted artifacts (e.g firmware binaries), if any. Moreover, in the `Testing` stage, the output result for each test case is provided. 

New Jobs can also be created manually. Each Job belongs to a specific Project. A list with all the Project Jobs can be found under the Project page (accessible by clicking a Project name in the [Projects](http://console.spannerci.com/app/projects) page). From there, it's possible to get various information about each Job, download any artifacts or even watch any Job in runtime or at a later time.

Also note, that because of the Spanner integration with GitHub, it's possible to watch the Job result directly from GitHub, after creating a new Pull Request.

## Environment Variables
Spanner supports the definition of environment variables for each Project. These variables can be defined from the Project Settings page and can be then used in the [.spannerci.yml](#configuration-with-spannerciyml) file and in the user defined [test scripts](#test-scripts). All the Spanner environment variables include an `ENV_` prefix. For example, we can use environment variables to define a list of device IDs that will be later used in the `.spannerci.yml` file to update these devices. Another usage example is the various access tokens, secrets and other credentials that we need to hide from the test scripts.  

## Configuration with .spannerci.yml
Spanner CI enables continuous integration by adding a `.spannerci.yml` file in the root directory of your repository. This, together with some more configuration options that are mentioned later, make every new commit or pull request to automatically trigger Spanner. 

Basically, the `.spannerci.yml` tells Spanner what to do. By default, it runs with three stages: 

1. `code_qa` stage for code quality checks
2. `build_binary` stage for firmware builds
3. `testing` stage for functional tests on real hardware

You don't need to use all the above stages and stages with no definitions will be ignored. Each stage contains definitions on what to do. A sample `.spannerci.yml` file is shown below:

```
code_qa:
    level: basic
    source: firmware/

build_binary:
    pre_flight:
    builder: particle photon
    source: firmware/
    script: make
    artifacts:
        - binaries/
        - output.logs
    post_flight:
    on_failure:
    on_success:

testing:
    script: examples/basic-tests/GPIO/read-digital-output/scenario.py
    device_update:
        devices:
            - ENV_DEVID_1
            - ENV_DEVID_2
        ota_method: particle
        binary: auto
```

A stage is defined by a list of parameters that define the stage behavior.

| Keyword | Required | Description |
| :--- | :--- | :--- |
| level         | No  | Defines the Spanner Service level |
| builder       | Yes | Defines the preferred build environment (1) |
| source        | Yes | Defines the source directory of the firmware |
| script        | Yes | Defines the script path or command to execute |
| artifacts     | No  | Defines a list of files or directories that will store the output results of the stage |
| device_update | No  | Enables OTA update of devices before testing |
| devices       | Yes | Defines a list of devices to apply the OTA update |
| ota_method    | Yes | Defines the preferred method for OTA updates (2) |
| binary        | Yes | Defines the binary source for OTA updates (auto, URL or repo path) |
| pre_flight    | No  | Override a set of commands that are executed before stage |
| post_flight   | No  | Override a set of commands that are executed after stage |
| on_failure    | No  | Override a set of commands that are executed on failure of stage |
| on_success    | No  | Override a set of commands that are executed on success of stage |

(1),(2): Please contact us to get a full list of the currently supported device builders and OTA update methods. To get started, make sure to check the [Examples](#examples) section.

## Test Scripts
Test Scripts are user defined scripts that contain a list of functional tests to be performed in one or more devices. Currently, they can be written in Python and we can trigger them by using the `script` parameter from the `Testing` stage. In the most primitive form, a test script looks like the one below:

```python
from Spanner import Spanner

def validate_dummy_test_case():
    spanner.assertTrue(1);

if __name__ == "__main__":
    validate_dummy_test_case()
```

In the above example, the validate_dummy_test_case() test case will pass because the assertion performed in this test case is true. Assertions provided by the `Spanner` module and cover various types of values. 

One of the most important aspects of Spanner Test Scripts are the Spanner [Testboards](#testboards), that enable the user to write hardware-in-the-loop functional tests. In other words, user is able to test the inputs and outputs of the device. Testboards can be added to the test scripts by importing the `Testboard` module. For example:
```python
from Testboard import Testboard
testboard = Testboard("testboard_name")
```

Example test scripts can be found under `testing` folder in this repository. Choose the one that you want to experiment with by defining the right path in the `script` parameter of `Testing` stage. The test cases are split into three categories:

* `Basic Tests`, which only perform one action and one test, to showcase that individual test function
* `Simple Tests`, which perform a simple real-world scenario, i.e. *Turn Light on through Network Command*
* `Complex Tests`, which perform a more common and complex real-world scenario, and whose goal is to showcase what an actual Functional test for a real product would test, with more than one assertions and using multiple APIs.

To understand the usage of Test Scripts in more real life scenarios, make sure to check the [Examples](#examples) section.


## Testboards
TODO

## Spanner CLI
Spanner provides a Command Line Interface (CLI) which can be used instead of the Web Interface. For more information please contact us.

## Examples
TODO
