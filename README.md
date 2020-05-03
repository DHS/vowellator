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

If you haven't created a python virtualenv before there is a handy guide [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).

In the terminal navigate to this folder then run the following two commands:

    mkvirtualenv vowellator
    pip install -r requirements.txt

Running the script
------------------

To run the script run the following:

    python vowellator.py "toller edwards aldrich"

Running the tests
-----------------

You can check whether your script meets the requirements by running:

    pytest
