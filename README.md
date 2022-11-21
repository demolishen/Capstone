# Brianna's Cleaning Business/Project Overview

My sibling started a Cleaning Business recently and could use a scheduling website to help keep her and her clients stay organized
and up to date with the cleaning(s) service they've requested/paid for. I believe this is something that would boost her profits and
help grow her reputation in her profession. Clients and prospective clients are able to visit her website and view personal reviews
and photos from past customers who've had something good to say about how they enjoyed their services provided. I want to increase my
abilities and personal portfolio, so I am doing this and maintaining this website as long as my sister is in business for herself.

## Home Page/User Profile

1. Registration Sign-up/User Base with Profiles containing scheduling information and more

2. Create view of easy to read Schedule with availability

3. Add ability to select individual date and time to submit a booking with location and photo of forseen cleaning task(s)

4. Get a response via phone/text/email or view estimate directly on the website once it's completed by Brianna

## Before and After photos

1. Let clients view and upload before and after photos of completed jobs

2. Display on front page somewhere to invite future prospects

## About Section

1. Brief personal history, history about the business, goals of the business, etc

2. Contact

    -Email

    -Phone/Text

    -Facebook

    -Etc.

## Functionality

The user will be greeted by the main page but not have access to it's use without first registering/signing up for their own account following their registration, they would follow the next steps to uploading photos of their prospective jobs to be completed, they send
the request with details of location, type of cleaning(deep, light, focused to certain areas, etc), date available for the cleaning along with time slots pre-determined by the owners scheduling of course and any details for arriving and where to park or where the key to enter may be. Their name and number and other methods of contact are in their profile and easily accessible to the owner so that they can contact the client for any further information if needed. Once the request is sent by the user, then there will be some sort of notification to the owner of their work requests to needed to be reviewed and returned with an estimate of the costs and which time
slots would work best plus any details needed for coordinating the cleaning time.
the user would get notified of when their estimate is completed and ready to be confirmed
and paid for deposit and then final payment.

## Data Models

1. PK = int(UserID) NOT NULL

        - Password NOT NULL = CharField

        - Profile

            - Name NOT NULL = CharField

            - Age NOT NULL = NumberField

            - Phone Number NOT NULL = NumberField

            - Email NOT NULL = EmailField

            - Location NOT NULL = CharField

2. PK = int(Scheduling ID) NOT NULL

        - FK = int(UserID) NOT NULL 

        -Location NOT NULL = CharField

        -Time/Date of possible cleaning availability slots NOT NULL = DateTimeField

        -Photo section for whats being cleaned at said location (with details) NOT NULL = ImageField

        -Type of cleaning to be performed NOT NULL = CharField(Choice Param.)

        -list of usual fees/rates NOT NULL = TextField

3. PK = int(Estimate Return ID) NOT NULL

        - FK = int(Scheduling ID) NOT NULL

        -Agreement of type of work/cost of work getting done NOT NULL = CharField

        -Agreement of location to be worked on/in NOT NULL = CharField

        -Agreement of concent to enter/how and where to enter NOT NULL = TextField

        -Agreement of date the work is to be completed and the time of arrival/estimated completion(s) NOT NULL = TextField

        -Agreement of whatever else I'm not thinking of that is normal for this type of business NOT NULL = FieldField

## Timeline

- Week 1 ("Milestone 1" Work Week: November 18th - November 25th)

  - Create base pages with HTML and basics for reaching "Milestone 2"

- Week 1 ("Milestone 1" Work Week: November 18th - November 25th)

  - Create the connections between views to display the user(s) their desired/selected results
  - Make sure functionality between pages and scheduling requests are syncing up and displaying properly to the user(s)

- Week 2 ("Milestone 2" Work Week: November 28th - December 2nd)

  - Add bells and whistles for uploading images and reviewing the business via each profile if they choose to do so
  - Make sure all bugs are found and resolved before moving on to final area of "Milestone 2"

- Week 2 ("Milestone 2" Work Week: November 28th - December 2nd).

  - Style the pages to represent a solid business website
  - Ask for suggestions to improve the functionality/appearance of page and implement what stands out

- Week 3 ("Milestone 2" Work Week: December 5th - December 9th).

  - Fine tune and sand any rough edges
  - Make sure the page is presentable and prepare to present
  - Have a solid foundation to be able to reach "Milestone 3"

- Week 4 ("Milestone 3" Work Week: December 12th - Continued).

  - Create a payment system for users to pay their deposit/invoice for services rendered
  - Apply any changes the owner(my sister) would like to have added/removed
  - Maintain and update the website as needed
  - Branch out from here for greater ideas that may be implemented in the future
