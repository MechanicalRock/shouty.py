# Shouty

Shouty is a social networking application for short physical distances.
When someone shouts, only people within 1000m can hear it.

Shouty doesn't exist yet - you will implement it yourself!

That is, if you're attending a BDD/Cucumber course.

## Agenda

### Get the code

Git:

    git clone https://github.com/cucumber-ltd/shouty.py.git
    cd shouty.py
    git checkout YYYY-MM-DD

Subversion:

    svn checkout https://github.com/cucumber-ltd/shouty.py/branches/YYYY-MM-DD shouty.py
    cd shouty.py

Or simply [download](https://github.com/cucumber-ltd/shouty.py/releases) a zip or tarball.

### Set up environment

    virtualenv py
    source ./py/bin/activate
    pip install -r requirements.txt

### Run behave

    behave

You should see:

    1 feature passed, 0 failed, 0 skipped
    1 scenario passed, 0 failed, 0 skipped
    0 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.000s

### Brainstorm capabilities

* Who are the main stakeholders?
* What can people do with the app?
* What are the main differentiators from other apps?

### Pick one capability

* Define rules
* Create high level examples (Friends episodes)

Then do this for each example to discover more examples:

* Can you think of a context where the outcome would be different?
* Are there any other outcomes we haven't thought about?

### Implement one capability. Inner Hexagon only.

* Write a Cucumber Scenario for one of the examples
* Make it pass!
