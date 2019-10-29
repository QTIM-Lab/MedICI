# MedICI
Composite Challenge Platform

## What is MedICI

The Medical Challenge Initiative is a platform to promote innovation through collaboration, to harness the ingenuity of the American public. It is based on the Microsoft open source project [CodaLab](https://github.com/codalab/codalab-competitions), with integrations with caMicroscope and ePAd. Additional customizations to enhance the project were incorporated based on user inputs. 

Codalab has their own installation instructions you can follow and we generally recommend following those. However, MedICI has a set of installation instructions performed step by step on Microsoft’s Azure platform. They are located [here](https://wiki.nci.nih.gov/display/MEDICI/Installing+MedICI+and+CodaLab)

## Customizations

### An Issue Reporting System

Participants routinely have questions that are answered in CodaLabs forums regarding first time use and the submission process. Occasionally issues with an evaluation script or website functionality prevents users from submitting their results or incorrectly scores their algorithm. MedICI provides additional functionality to track these specific issues.

How to use:

Once logged in users should navigate to a specific challenge. At a challenge home page you will see two new tabs present (Report Issue and Issue Status). Use Report Issue to send an email to the challenge organizers. Organizers can then go to an admin only tab called Issue Status and see a table with issues logged.


### Integrations with Imaging Platforms

The following imaging technologies have been added to MedICI. In order to use you need to install the docker images following the instructions on each platform's website (linked below).

#### ePAD

[ePad](https://epad.stanford.edu/) is a freely available quantitative imaging informatics platform, developed at the Rubin lab. This software handles the radiology annotations and metadata management. 


#### caMIcroscope

[caMicroscope](https://github.com/camicroscope/Distro), a web based annotation and visualization platform designed for digitized whole slide images. This software handles pathology annotations optimized for large bio-medical image data, with an emphasis on cancer pathology.


