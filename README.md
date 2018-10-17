# Spanner CI #

[Spanner CI](https://spannerci.com) is a Continuous Integration Platform for IoT and Embedded Devices. It can be used for automated code quality checks, automated firmware builds and automated functional tests in real hardware that run with every new version of your firmware.

This repository contains everything that is needed to get started with Spanner CI. It's highly recommended to make a fork of this repository and use it as a starting point to understand how Spanner CI can be easily integrated with your own github repository.

In the next sections you'll find detailed information of how to setup Spanner CI. In short, we will create an account in Spanner CI Platform and use a `.spannerci.yml` configuration file in the root directory of our repository to trigger Spanner CI for every commit or pull request. Each time Spanner CI is triggered, it reads the instructions in `.spannerci.yml` file and starts the relevant service, like automated builds or automated tests. All the test scripts are also part of the repository.  

## Creating an Account

If you haven't used Spanner CI before, you can create a new account: 

1. Visit the [Create an Account](http://console.spannerci.com/app/accounts/register) page.
2. If you already have a GitHub account click the `SIGN UP WITH GITHUB` button otherwise enter your basic information and click `REGISTER` to continue.
3. Use the credentials provided above to sign-in.
4. Enter your organization info and you're ready to go!

Next step is to integrate Spanner CI with GitHub.

**Note**: By signing in with GitHub, the `GitHub Authorization` section below can be skipped.

## Integration with GitHub

Spanner provides an official Github Spanner CI Application for easy integration with GitHub. This authorises the Spanner CI platform to access Github repositories. 

#### Create a Github repository:
To freely experiment with the **Spanner CI Test Examples**, it is necessary to fork this repository into your Github account.

#### Installation of GitHub Spanner CI App:
1. Visit https://github.com/apps/spannerci-app
2. Click on install.
3. Select the repository that you created in the previous section in order to provide access to the Spanner CI platform.

Note: that the account where the GitHub Spanner CI app is installed, must be the same as the one authorised using the GitHub sign in. 

#### GitHub Authorization:
1. After sign in the Spanner CI platform, click the username on the left upper corner.
2. Select Settings on the dropdown menu.
3. Click on the "Connect with Github" button to link the GitHub account with Spanner CI.
4. Spanner CI account is ready and authorised to use the selected GitHub repositories.

## Spanner Configuration

Modify .spannerci.json configuration file to enable Spanner CI integration. The structure of the file is shown below:

    {
      "code_quality": false,
      "build_binary": false,
      "deploy": false,
      "tests": false,
      "script": "path/to/script/myscript.py"
    }
    
The most important setting of this file is the path of the script that contains the example test. In the folder `examples/` can be found example test scripts for various use cases. Choose the one that you want to experiment with by defining the right path. The test cases are split into three categories:

1. **Basic Tests**, which only perform one action and one test, to showcase that individual test function
2. **Simple Tests**, which perform a simple real-world scenario, i.e. *Turn Light on through Network Command*
3. **Complex Tests**, which perform a more common and complex real-world scenario, and whose goal is to showcase what an actual Functional test for a real product would test, with more than one assertions and using multiple APIs.

## Spanner Projects
Spanner supports the creation of one or more projects for working with different repositories. To create a new project:

1. Select Projects from the navigation menu on the left side of the dashboard.
2. Click on New Project.
3. Select the repository from the connected repositories on Github.
4. Click on create project.

## Spanner Jobs
Spanner executes each test script inside a virtual environment. For each run, a new job is created. Jobs can run automatically (through pull requests) or manually as described below.

### Manual Job Creation:
1. Click on projects, from the navigation menu on the left side of the dashboard.
2. Select the run by Branch or Commit option. By selecting run by commit, the commit id (sha hash) should manually be provided. By selecting the branch option, an available branch from the repository can be selected.
3. Click on the play Button to start the new job.
4. If any errors have occurred, an alert message will appear prompting the error on the test script.
5. If the test has completed successfully, a message will appear and the user will be redirected to the Jobs page.

### Job Creation from Pull Request

This will automatically trigger a Spanner CI Job on each Pull Request

1. Click on the Pull request button in the Github Repository homepage.
2. Create a new Pull request and wait for the notification messages delivered from the SpannerCI platform.
3. After the completion of the test cases, a message will appear together with a link to the SpannerCI platform with more information, on the run itself.

### Job History

1. Click on Jobs from the navigation menu on the left side of the dashboard.
2. A list of the latest running jobs will be shown.
3. By clicking the Stats button on each job, enables us to watch each running test and their corresponding results.

## Spanner CLI
Spanner provides a Command Line Interface (CLI) which can be used instead of the Web Interface. For more information please contact us.
