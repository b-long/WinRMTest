# WinRMTest
A connectivity test for WinRM.  Useful when debugging things like [Jenkins' EC2 plugin](https://github.com/jenkinsci/ec2-plugin).

[![Build Status](https://travis-ci.org/b-long/WinRMTest.svg)](https://travis-ci.org/b-long/WinRMTest)

To run this module:
```
export test_host="<host>" test_u="<user>" test_p="<password>" && python WinRM_Test.py
```
