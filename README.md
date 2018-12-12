# eventboybot

main logic:
1. webhook triggered
2. "update" json object is passed to lambda handler
3. lambda handler checks for chatid
4. lambda handler checks for user state, from db, based on chatid
5. based on state and input (command and arguments extracted from 'update' object), execute the corresponding handler

always ensure that:
- lambda is exited and db connection is closed when logic is done.
- errors are handled.
- test cases are done for all edge cases and at least 2 common cases.

general project workflow:
1. set up aws lambda endpoint on AWS Lambda [done]
2. set up telegram webhook with Telegram HTTPS API
3. design state machine for bot user experience
4. create db schema
5. point python script to some url?
6. run tests
7. upload deployment package (zip source code and dependencies from site-packages)