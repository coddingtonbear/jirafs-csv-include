Jirafs csv-table Macro
======================

This Jirafs plugin adds a macro allowing you to create tables in your Jira issues by rendering them from a CSV file.

.. image:: http://coddingtonbear-public.s3.amazonaws.com/github/jirafs-csv-table/demo_v1.gif

and the comment posted will appear in Jira as:

.. image:: http://coddingtonbear-public.s3.amazonaws.com/github/jirafs-csv-table/demo_v1_jira.png

Quickstart
----------

1. Create your CSV file.
2. Use the macro, setting the 'src' field to the path to your CSV file::

   <jirafs:csv-table src="my_csv_file.csv" />

Parameters
----------

* `src`: Path to CSV file to include as a table.
* `delimiter`: (Default: ",") Delimiter used for separating each column's
  values.  You can use standard python string escape sequences; so for using
  a tab as your file's field delimiter, you can provide the value of "\t".
* `has_header`: (Default: True) If the first row of your CSV file is not a
  header, set this to False.

Requirements
------------

This version requires a Jirafs version of at least 2.0.0.

Installation
------------

1. Install from PIP::

    pip install jirafs_csv_table

2. Enable for a ticket folder::

    jirafs plugins --enable=csv_table

Note that you can globally enable this (or any) plugin by adding the
``--global`` flag to the above command::

    jirafs plugins --global --enable=csv_table

