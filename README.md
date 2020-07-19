
# Machine Learning and Data Science Blueprints for Finance - Jupyter Notebooks

This project aims at teaching you the fundamentals of Machine Learning in
python. It contains the code to the case studies in the O'Reilly book *Machine Learning and Data
Science Blueprints for Finance*

Simply open the [Jupyter](http://jupyter.org/) notebooks you are interested in by cloning this repository and running Jupyter locally. This option lets you play around with the code. In this case, follow the installation instructions below.

### Want to play with these notebooks online without having to install anything?
Use any of the following services.

**WARNING**: Please be aware that these services provide temporary environments: anything you do will be deleted after a while, so make sure you download any data you care about.

* **Recommended**: open this repository in [Colaboratory](https://colab.research.google.com/github/tatsath/fin-ml/blob/master):
<a href="https://colab.research.google.com/github/tatsath/fin-ml/blob/master"><img src="https://colab.research.google.com/img/colab_favicon.ico" width="90" /></a>

* Or open it in [Binder](https://mybinder.org/v2/gh/tatsath/fin-ml/master):
<a href="https://mybinder.org/v2/gh/tatsath/fin-ml/master"><img src="https://matthiasbussonnier.com/posts/img/binder_logo_128x128.png" width="90" /></a>

  * _Note_: Most of the time, Binder starts up quickly and works great, but when the github repository of this book is updated, Binder creates a new environment from scratch, and this can take quite some time.

* Or open it in [Deepnote](https://beta.deepnote.com/launch?template=data-science&url=https%3A//github.com/tatsath/fin-ml/blob/master/index.ipynb):
<a href="https://beta.deepnote.com/launch?template=data-science&url=https%3A//github.com/tatsath/fin-ml/blob/master/index.ipynb"><img src="https://www.deepnote.com/static/illustration.png" width="150" /></a>

### Just want to quickly look at some notebooks, without executing any code?

Browse this repository using [jupyter.org's notebook viewer](https://nbviewer.jupyter.org/github/tatsath/fin-ml/blob/master/index.ipynb):
<a href="https://nbviewer.jupyter.org/github/tatsath/fin-ml/blob/master/index.ipynb"><img src="https://jupyter.org/assets/nav_logo.svg" width="150" /></a>

### Want to install this project on your own machine?

Start by installing [Anaconda](https://www.anaconda.com/distribution/) (or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)), [git](https://git-scm.com/downloads), and if you have a TensorFlow-compatible GPU, install the [GPU driver](https://www.nvidia.com/Download/index.aspx).

Next, clone this project by opening a terminal and typing the following commands (do not type the first `$` signs on each line, they just indicate that these are terminal commands):



    $ cd $HOME  # or any other development directory you prefer
    $ git clone https://github.com/tatsath/fin-ml.git
    $ cd fin-ml

If you do not want to install git, you can instead download [master.zip](https://github.com/tatsath/fin-ml/archive/master.zip), unzip it, rename the resulting directory to `handson-ml` and move it to your development directory.

If you are familiar with Python and you know how to install Python libraries, go ahead and install the libraries listed in `requirements.txt` and jump to the [Starting Jupyter](#starting-jupyter) section. If you need detailed instructions, please read on.

## Python & Required Libraries
Of course, you obviously need Python. Python 3 is already preinstalled on many systems nowadays. You can check which version you have by typing the following command (you may need to replace `python3` with `python`):

    $ python3 --version  # for Python 3

Any Python 3 version should be fine, preferably 3.5 or above. If you don't have Python 3, we recommend installing it. To do so, you have several options: on Windows or MacOSX, you can just download it from [python.org](https://www.python.org/downloads/). On MacOSX, you can alternatively use [MacPorts](https://www.macports.org/) or [Homebrew](https://brew.sh/). If you are using Python 3.6 on MacOSX, you need to run the following command to install the `certifi` package of certificates because Python 3.6 on MacOSX has no certificates to validate SSL connections (see this [StackOverflow question](https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error)):

    $ /Applications/Python\ 3.6/Install\ Certificates.command

On Linux, unless you know what you are doing, you should use your system's packaging system. For example, on Debian or Ubuntu, type:

    $ sudo apt-get update
    $ sudo apt-get install python3 python3-pip

## Installing Anaconda

After installing Python, we recommend installing [Anaconda](https://docs.anaconda.com/anaconda/install/). This is a package that includes both Python and many scientific libraries. You should prefer the Python 3 version.


## Using pip

Installing Anaconda, should install most of the commonly used libraries in the case studies. Given that there might be changes to the Anaconda package and some libraries might be out of date, it is a good idea to learn how to install packages in python using pip. 

### Installing pip

These are the commands you need to type in a terminal if you want to use pip to install. Note: in all the following commands, if you chose to use Python 2 rather than Python 3, you must replace `pip3` with `pip`, and `python3` with `python`.

First you need to make sure you have the latest version of pip installed. If you are on the latest version of Python, pip should already be installed. You can check using the following command.

    $ pip -V

If you do not have pip install, you can run the following command on Linux

    $ sudo apt-get install python3-pip

Or download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and install it on Windows using

    $ python3 get-pip.py

If you have `pip` already installed, it might be a good idea to upgrade it.

    $ python3 -m pip install --user --upgrade pip

The `--user` option will install the latest version of pip only for the current user. If you prefer to install it system wide (i.e. for all users), you must have administrator rights (e.g. use `sudo python3` instead of `python3` on Linux), and you should remove the `--user` option. The same is true of the command below that uses the `--user` option.

### Creating an environment (optional)

Next, you can optionally create an isolated environment. This is recommended as it makes it possible to have a different environment for each project (e.g. one for this project), with potentially very different libraries, and different versions:

    $ python3 -m pip install --user --upgrade virtualenv
    $ python3 -m virtualenv -p `which python3` env

This creates a new directory called `env` in the current directory, containing an isolated Python environment based on Python 3. If you installed multiple versions of Python 3 on your system, you can replace `` `which python3` `` with the path to the Python executable you prefer to use.

Now you must activate this environment. You will need to run this command every time you want to use this environment.

    $ source ./env/bin/activate

On Windows, the command is slightly different:

    $ .\env\Scripts\activate

### Installing Python packages

Next, use pip to install the required python packages. If you are not using virtualenv, you should add the `--user` option (alternatively you could install the libraries system-wide, but this will probably require administrator rights, e.g. using `sudo pip3` instead of `pip3` on Linux).

The following command is used to install python package with a particular version.

    $ pip3 install <PACKAGE>==<VERSION>

If you want to try to install a list of packages from a file. You can use the following command.

    $ python3 -m pip install --upgrade -r requirements.txt

Great! You're all set, you just need to start Jupyter now.

## Installing Package models

For the chapter on Natural Language Processing. We will be using the `spaCy` python package. Installing `spaCy` does not install the language models used. In order to do that, we need to open up python and install it ourselves using the following commands.

    $ python -m spacy download en_core_web_lg


## Starting Jupyter
Okay! You can now start Jupyter, simply type:

    $ jupyter notebook

This should open up your browser, and you should see Jupyter's tree view, with the contents of the current directory. If your browser does not open automatically, visit [127.0.0.1:8888](http://127.0.0.1:8888/tree). Click on `index.ipynb` to get started!


## Installing Libraries in Jupyter using pip

If you install a library and are not able to import it on the jupyter notebook. You might be installing them on the system python environment. We can use Jupyter notebooks to install packages using the ! symbol at the start. THe following libraries are the ones that are required outside the latest Anaconda package as of now.

    $ !pip install spacy
    $ !pip install pandas-datareader
    $ !pip install keras
    $ !pip install dash
    $ !pip install dash
    $ !pip install dash_daq
    $ !pip install quandl
    $ !pip install cvxopt
    
    
    

