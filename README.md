# dont sleep

simple script to move the mouse every few minutes to keep my computer from going to sleep.

yes, it's a parody on No Doubt's song "Don't Speak", so shit talking about the repo name will not be tolerated!

## prereqs:
1. `python3`, let's just hope y'all have always had this. don't embarrass me.

## linux specific
1. if you're using a linux box, you may have to install `python3-venv` (otherwise, it should come as a default when you install python3 elsewhere). in order to use `MouseInfo`, linux requires your ass to install `tkinker` as well.
    ```
    $ sudo apt install python3-venv
    $ sudo apt install python3-tk python3-dev
    ```
1. python package `wheel` should also be installed, if not, it'll default to using the regular shmegular `setup.py install`.
    ```
    $ pip3 install wheel
    ```

## how to install:
1. now that we've got all that out of the way, clone this repo. https or ssh way, doesn't matter.
    ```
    $ git clone https://gitlab.com/lifeless-devs/dont-sleep.git
    ```
    ```
    $ git clone git@gitlab.com:lifeless-devs/dont-sleep.git
    ```
1. create an environment to install python packages (we don't want that shit to be global or else it could screw up other projects you've been working on) and activate it.
    ```
    $ python3 -m venv env
    $ source env/bin/activate
    ```
1. install python package `pyautogui`.
    ```
    $ pip3 install pyautogui
    ```
1. and you're done! just start the script. you're gonna have to be activated in this environment in order to run (unless you installed it globally but that's on you).
    ```
    $ python3 src/main.py
    ```

**note/todo:** i'll eventually update this to work on windows. i'll do it later lol.
