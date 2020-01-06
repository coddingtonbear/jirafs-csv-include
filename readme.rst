Jirafs csv_include Macro
================

*NOTE: This is a work in progress!*

Adds a macro used for including a CSV file as a Jira table::

  <jirafs:csv_include filename="my_file.csv" />

if you have a file named `my_file.csv` containing the content::

  ,Canada,United States of America,Mexico, Guatemala
  Capital,"Ottawa, Ontario","Washington, DC","Mexico City, DF","Guatemala City"
  Population (millions),35.16,318.9,122.3,15.47

will be automatically transformed into JIRA's special markup::

  || ||Canada||United States of America||Mexico||Guatemala||
  |Capital|Ottawa, Ontario|Washington, DC|Mexico City, DF|Guatemala City|
  |Population (millions)|35.16|318.9|122.3|15.47|

which, when rendered by JIRA, will look something like this:

+------------+-----------------+--------------------------+-----------------+----------------+
|            | Canada          | United States of America | Mexico          | Guatemala      |
+============+=================+==========================+=================+================+
| Capital    | Ottawa, Ontario | Washington, DC           | Mexico City, DF | Guatemala City |
+------------+-----------------+--------------------------+-----------------+----------------+
| Population | 35.16           | 318.9                    | 122.3           | 15.47          |
| (millions) |                 |                          |                 |                |
+------------+-----------------+--------------------------+-----------------+----------------+

Parameters
----------

* `filename`: Path to CSV file to include.
* `delimiter`: CSV delimiter; defaults to ",".  You can use standard python
  string escape sequences; so for using a tab as your file's field delimiter,
  you can provide the value of "\t".

Requirements
------------

This version requires a Jirafs version of at least 2.0.0.

Installation
------------

1. Install from PIP::

    pip install jirafs_csv_include

2. Enable for a ticket folder::

    jirafs plugins --enable=csv_include

Note that you can globally enable this (or any) plugin by adding the
``--global`` flag to the above command::

    jirafs plugins --global --enable=csv_include

