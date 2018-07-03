# Project Summary: #
This project is a internal reporting tool, answering questions about a newspaper
site's user activity, using information from a already established database.
The questions we are concerned with answering are:
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

# Installation: #

### Step 1: Installing Required Files ###

**Required Programs and OS:**

  * Windows 10
  * Python 3.6.5 - https://www.python.org/downloads/release/python-365/
  * Vagrant 2.1.1 - https://www.vagrantup.com/downloads.html
  * Git Bash 2.18.0 - https://git-scm.com/download/win

Must have the above programs before moving onto step 2!

### Step 2: Readying Database Config ###

Once you have downloaded and installed the requirements, we can then download
the preloaded vagrant database configuration using this links:

[Link 1](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
[Link 2](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

**Extract content within the zip folder to your desktop**

If all goes well, then you should see two additional folders on your desktop:

**1. newsdata-1**
**2. FSND-Virtual-Machine**

Now, move the file **newsdata.sql** within newsdata-1 folder into the folder
**vagrant** within FSND-Virtual-Machine.

To actually run this project, we will need to have **logs.py**, which is in this
GitHub repository, to be inside folder vagrant as well. Download logs.py and
move it into vagrant.

### Finish Installation ###

If you have finished Step 1 and 2 then on your desktop you should have a folder
called FSND-Virtual-Machine and within it, you should also see a file called
vagrant.

Go into the vagrant folder and check if you have the files **newsdata.sql** and
**logs.py**.

If both files are in there then you are ready to run the project!

# Running the Project: #

### Getting into Linux System ###

First, open up Git Bash and then navigate to the folder **vagrant** within
the folder FSND-Virtual-Machine on your Desktop.

Once you have reached into the folder vagrant, I want you to run the following
commands while waiting in between each operation so they finish:

```Shell Session
vagrant up
vagrant ssh
```

**Note: the command 'vagrant up' will take a while since it is booting up your
linux OS in the virtual environment and command 'vagrant ssh' will allow you to
sign into the OS as a user which then means you can start using the linux OS**

### Creating the database ###

You are almost there! Now that we are in the Linux OS on our shell session,
there is two more commands to run:

**cd ../../vagrant**
**psql -d news -f newsdata.sql**

running these two commands will build the database this project works with.

### Run the Python File ###

Finally, we actually get to see our reports! Now within the linux OS, we should
still be in the same location.

Run the following command:

python logs.py

If the above gives an error run this command instead:

python3 logs.py

Wait for a little and the reports will come in! A sample report is in the
example_output.txt and its provided within this same repository.
