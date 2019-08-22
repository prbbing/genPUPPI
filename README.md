This is a user friendly interface with PUPPI
It allows the user to deliver any messages via PUPPI
recipes:

Install python dependencies as certain modules are not available in the latest CMSSW

pip install Pillow
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages

Now you are all set.

To execute the command:

python genPUPPI.py "your message"

The message is formatted in the following way:

"string1,string2,string3,....,stringi"

In this case there will be i rows (separated by ,), centered

For example "hello,this is the,puppi generator" will give you

   hello
 this is the
puppi generator

Enjoy
