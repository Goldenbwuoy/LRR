# About LRR

LRR (Lab Report Repository) is an online software application for posting assignments, submitting assignments and marking (re-marking) assignments.

This software was originally developed by by Mahomed Nor, a graduate student in the Department of Computer Science at the Zhejiang Normal University,
while he was taking a graduate course called **Advanced Software Engineering** (http://lanlab.org/course/2018f/se/homepage.html).

The LRR's project home page is at http://118.25.96.118/nor/homepage/index.html.



# Mission

Our mission is to make the experience of submitting assignments great for tens of hundreds of students in the department of computer science at the Zhejiang Normal University (Jinhua City, Zhejiang Province).



# Installation Instructions


## Hui's steps

I spent about two hours on installing LRR to a bare, remote Ubuntu server (Ubuntu 20.04 LTS).

LRR needs Apache and MySQL to run.  I followed [How To Install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04) to set up these server applications.

LRR uses a database called `lrr`.  I need to export existing `lrr` to a plain text file (including many sql commands) and import that text file to the newly created `lrr` database on the new server.
The command for exporting the database is `mysqldump -u mnc -p lrr > lrr_database_dump.txt`.
The command for importing is `mysql -u mnc -p lrr < lrr_database_dump.txt`.  Read [How to Import and Export MySQL Databases in Linux](https://phoenixnap.com/kb/import-and-export-mysql-database) for more detail.

LRR also needs to store assignment submissions.  We store them in a folder called `../../lrr_submission`.  Note that `lrr_submission` is two levels above the project folder (where many PHP files reside).  I copied this folder from the existing one.  I think it is also OK if you create an empty folder.   
We need to set a proper owner and accessibility for `lrr_submission` using the following two commands:
`sudo chown -R www-data:www-data lrr_submission` and  `sudo chmod -R g+rw lrr_submission`.  Also, remember to change the user name and password in `lrr_submission//KeepItSafe.txt` for the database connection.

The above steps are preparation work. Now we could clone the LRR's repository to `/var/www/html/`.
Rename LRR to lrr.  Change the owner of lrr: `sudo chown -R $USER:$USER /var/www/lrr`. Edit apache configure file: `sudo nano /etc/apache2/sites-available/lrr.conf`.


    <VirtualHost *:80>
        ServerName lrr
        ServerAlias www.lrr.com
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/lrr
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>

Enable the site lrr: `sudo a2ensite lrr`.  Restart the apache server: `sudo systemctl reload apache2`.
Visit the LRR application by entering this URL in a web browser: http://121.4.94.30/.


## Enock's steps

Enock has made a tutorial about how he deployed LRR to a remote server (http://lanlab.org/course/2021s/spm/PuTTY-Server.txt).




# Current Status

This software has been actively used by students who took or are
taking courses (Introduction to Software Engineering and Software
Project Management) taught by Hui.

There are more than 200 student accounts created since its first
launch in 2018.

A running instance of this software is at http://118.25.96.118/nor/

There are about 40 bugs (most being CRITICAL) that remain unresolved
before LRR can hit its beta release.  See the section *The Bug
Tracker* for more detail.  Currently, there are a few groups (formed
by students who are taking Software Project Management) working on
these bugs.




# The Bug Tracker

We use Bugzilla to track LRR's bugs and feature requests.

Most bugs of this software are recorded on the  bug tracker for LRR:
http://118.25.96.118/bugzilla/describecomponents.cgi?product=Lab%20Report%20Repository%20%28nor%20houzi%29



# TODO

-  *Receiving email for password resetting*. Password resetting link is not always sent successfully.

-  *How assignements should be stored?*  Creating sub-directories on all student submissions course-code/semester/section-number.  (/student-number/course-code/semester/section-number/assignement-title/submission.txt)

-  [SOLVED] Editing the assignment title after uploading a new assignment (instructor).

-  [SOLVED] A new user could not login immediately after sign up.

- A more complete list of TODO's is at http://lanlab.org/course/2020s/spm/decide-areas-for-improvement-review.html


# How to Contribute

We welcome your participation in this project.

Your participation does not have to be in the form of contributing code.  You could help us on
ideas, suggestions, documentation, etc.


You need to be an invited member of *Lan Laboratory* before you can
push your feature branch or bugfix branch to the central reops at
https://github.com/lanlab-org

Send Hui (lanhui at zjnu.edu.cn) an email message including your
GitHub account name so that he could invite you to be a member of *Lan
Laboratory*.

As of March 31 2020, there are 30 members in *Lan Laboratory* (https://github.com/orgs/lanlab-org/people).

You will use the feature-branching workflow (see below) when
interacting with the central repo.  The main point of this workflow is
that you work on a branch on your local drive, push that branch to the
central repo, and create a Pull Request (i.e., Pull Me Request) at
GitHub for other people to review your changes.  When everything is
OK, then *someone* could merge your changes to the master branch in the
central repo.

I believe that *code review* at the Pull Request stage is important
for both improving code quality and improving team quality.



## The Feature-branching Workflow

We will use the feature-branching workflow for collaboration.  The
idea is that you make your own branch, work on it, and push this branch to
the central repo for review.

Check the section **The feature-branching workflow** in the following link for more detail:

https://github.com/spm2020spring/TeamCollaborationTutorial/blob/master/team.rst



## Communications Method

For real-time communication, check our IRC channel `#lrr` at irc.freenode.org.  Check this link http://lanlab.org/course/2020s/spm/irc-instruction.txt
for how to use IRC.

To submit bug reports or improvement ideas, please ask Hui [lanhui at zjnu.edu.cn] to open a Bugzilla account for you.





## Frequently Asked Questions


1. Q: The web application's front page does not show properly, i.e., elements are not well aligned.
   A: You missed two folders `css` and `font-awesome`.  These folders include third-party js or css files and therefore are not included.

1. Q: What if I do not have any information about the `lrr` database?
   A: You could use `lrr(1).sql` or `lrr_database.sql`.  It seems `lrr(1).sql` is more complete.



# The Original GitHub Repo

The original GitHub Repo is at https://github.com/EngMohamedNor/LabReportRepo


# Contributor List

*Important contributors are highlighted.*

GitHub Account - Full Name - Student number

CODEwithZAKI - Omar Mohamud Mohamed - 202025800041

BloudYoussef - Khayat Youssef - 202025800042 

TanakaMichelle - Tanaka Michelle Sandati - 201732120134

WhyteAsamoah  - Yeboah Martha Asamoah   - 201732120135

xiaoyusoil - ZhengXiaoyu - 201732120110

Benny123-cell - ZhangBin - 201732120127

421281726 - LiJiaxing - 201732120118

zhenghongyu-david - ZhengHongyu - 201732120128

wkytz - YeHantao - 201732120125

zego000 - GaoZeng - 201732120117

Richard1427 - XieJiacong - 201732120123

yutengYing - YingYuteng - 201732120126

Samrusike  - Samantha Rusike  - 201632120140

*enockkays* <enockkhondowe94@yahoo.com>

*Teecloudy*  - Ashly Tafadzwa Dhani - 201632120150

GuedaliaBonheurSPM - Guedalia Youma - 201925800221

ACorneille - Alimasi Corneille - 201925800168

Tabithakipanga - Kipanga Dorcas - 201925800170

Mary-AK  - Mary Akussah Doe - 201925800173

pkkumson  - Kumson Princewill Kum - 201925800166

Twizere  -  Twizere Pacifique  -  201925800174

Nicole-Rutagengwa  - Nicole Rutagengwa  - 201925800169

