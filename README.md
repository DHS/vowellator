Vowellator
==========

This is a silly little Python exercise. My grandfather was a family tree
enthusiast. He was also a little eccentric. At some point he decided to
write a list of surnames found throughout the family tree ordered by
first vowel. As you do.

Thus your challenge is to write a little Python function that will sort
a list of names in order of their first vowel. See below for
instructions on how to setup the virtualenv, how to run the script and
how to run the tests to check your work.

Setting up the virtual env
--------------------------

This project requires [Python](https://www.python.org/) (3.8) and [pipenv](https://pipenv.pypa.io/en/latest/)
so you'll need to install those first.

In the terminal navigate to this folder then run the following command:

    pipenv install

Running the script
------------------

To run the script use the following command:

    pipenv run python vowellator.py "toller edwards aldrich"

Running the tests
-----------------

You can check whether your script meets the requirements by running:

    pipenv run pytest
