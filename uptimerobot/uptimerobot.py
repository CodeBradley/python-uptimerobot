#!/usr/bin/env python

from __future__ import print_function

try:
    import urllib.request as urllib_request
except ImportError:
    import urllib2 as urllib_request
import json
import sys
import os
try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

monitorFriendlyName = None
monitorURL = None
apiKey = None
monitorAlertContacts = ""

MONITORS_PER_PAGE = 50

class UptimeRobot(object):
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.baseUrl = "https://api.uptimerobot.com/"


    def addMonitor(self, monitorFriendlyName, monitorURL):
        """
        Returns True if Monitor was added, otherwise False.
        """
        url = self.baseUrl
        url += "newMonitor?apiKey=%s" % self.apiKey
        url += "&monitorFriendlyName=%s" % monitorFriendlyName
        url += "&monitorURL=%s&monitorType=1" % monitorURL
        url += "&monitorAlertContacts=%s" % monitorAlertContacts
        url += "&noJsonCallback=1&format=json"
        success, response = self.requestApi(url)
        if success:
            return True
        else:
            return False


    def getMonitors(self, response_times=0, logs=0, uptime_ratio='', offset=None, limit=None, search=None, monitors=None):
        """
        Returns status and response payload for all known monitors.
        """
        url = self.baseUrl
        url += "getMonitors?apiKey=%s" % (self.apiKey)
        url += "&noJsonCallback=1&format=json"
        # responseTimes - optional (defines if the response time data of each
        # monitor will be returned. Should be set to 1 for getting them. Default
        # is 0)
        if response_times:
            url += "&responseTimes=1"
        # logs - optional (defines if the logs of each monitor will be returned.
        # Should be set to 1 for getting the logs. Default is 0)
        if logs:
            url += '&logs=1'
        # customUptimeRatio - optional (defines the number of days to calculate
        # the uptime ratio(s) for. Ex: customUptimeRatio=7-30-45 to get the
        # uptime ratios for those periods)
        if uptime_ratio:
            url += '&customUptimeRatio=%s' % uptime_ratio
        if offset is not None:
            url += "&offset=%s" % offset
        if limit is not None:
            url += "&limit=%s" % limit
        if search is not None:
            url += "&search=%s" % search
        if monitors is not None:
            url += "&monitors=%s" % '-'.join(str(m) for m in monitors)
            pass
        url += "&noJsonCallback=1&format=json"
        return self.requestApi(url)


    def getMonitorById(self, monitorId):
        """
        Returns monitor by MonitorId.
        """
        try:
            monitor = self.iterMonitors(monitors=[monitorId]).next()
        except StopIteration:
            return None
        return monitor


    def getMonitorByName(self, monitorFriendlyName):
        """
        Returns monitor by MonitorFriendlyName.
        """
        try:
            monitor = self.iterMonitors(search=monitorFriendlyName).next()
        except StopIteration:
            return None
        if monitor['friendlyname'] != monitorFriendlyName:
            return None
        return monitor


    def editMonitor(self, monitorID, monitorStatus=None, monitorFriendlyName=None, monitorURL=None, monitorType=None,
                    monitorSubType=None, monitorPort=None, monitorKeywordType=None, monitorKeywordValue=None,
                    monitorHTTPUsername=None, monitorHTTPPassword=None, monitorAlertContacts=None):
        """
        monitorID is the only required object. All others are optional and must be quoted.
        Returns Response object from api.
        """

        url = self.baseUrl
        url += "editMonitor?apiKey=%s" % self.apiKey
        url += "&monitorID=%s" % monitorID
        if monitorStatus:
            # Pause, Start Montir
            url += "&monitorStatus=%s" % monitorStatus
        if monitorFriendlyName:
            # Update their FriendlyName
            url += "&monitorFriendlyName=%s" % monitorFriendlyName
        if monitorURL:
            # Edit the MontiorUrl
            url += "&monitorURL=%s" % monitorURL
        if monitorType:
            # Edit the type of montior
            url += "&monitorType=%s" % monitorType
        if monitorSubType:
            # Edit the SubType
            url += "&monitorSubType=%s" % monitorSubType
        if monitorPort:
            # Edit the Port
            url += "&monitorPort=%s" % monitorPort
        if monitorKeywordType:
            # Edit the Keyword Type
            url += "&monitorKeywordType=%s" % monitorKeywordType
        if monitorKeywordValue:
            # Edit the Keyword Match
            url += "&monitorKeywordValue=%s" % monitorKeywordValue
        if monitorHTTPUsername:
            # Edit the HTTP Username
            url += "&monitorHTTPUsername=%s" % monitorHTTPUsername
        if monitorHTTPPassword:
            # Edit the HTTP Password
            url += "&monitorHTTPPassword=%s" % monitorHTTPPassword
        if monitorAlertContacts:
            # Edit the contacts
            url += "&monitorAlertContacts=%s" % monitorAlertContacts
        url += "&noJsonCallback=1&format=json"
        success = self.requestApi(url)
        return success


    def deleteMonitorById(self, monitorID):
        """
        Returns True or False if monitor is deleted
        """
        url = self.baseUrl
        url += "deleteMonitor?apiKey=%s" % self.apiKey
        url += "&monitorID=%s" % monitorID
        url += "&noJsonCallback=1&format=json"
        success, response = self.requestApi(url)
        if success:
            return True
        else:
            return False

    def requestApi(self, url):
        response = urllib_request.urlopen(url)
        content = response.read().decode('utf-8')
        jContent = json.loads(content)
        if jContent.get('stat'):
            stat = jContent.get('stat')
            if stat == "ok":
                return True, jContent
        return False, jContent

    def getAlertContacts(self, alertContacts=None, offset=None, limit=None):
            """
            Get Alert Contacts
            """
            url = self.baseUrl
            url += "getAlertContacts?apiKey=%s" % self.apiKey
            if alertContacts:
                url += "&alertContacts=%s" % alertContacts
                pass
            if offset:
                url += "&offset=%s" % offset
                pass
            if limit:
                url += "&limit=%s" % limit
                pass
            url += "&noJsonCallback=1&format=json"
            return self.requestApi(url)

    def getAlertContactIds(self, urlFormat=False):
        ids = []
        success, response = self.getAlertContacts()
        if success:
            alertContacts = response.get('alertcontacts').get('alertcontact')
            for alertContact in alertContacts:
                ids.append(alertContact.get('id'))
        if urlFormat:
            formatted = ""
            for id in ids:
                formatted += id + "-"
            return formatted[:-1]
        else:
            return ids

    def getMonitorId(self, name):
        success, response = self.getMonitors()
        if success:
            monitors = response.get('monitors').get('monitor')
            for monitor in monitors:
                if monitor['friendlyname'] == name:
                    return monitor['id']
        return None

    def deleteMonitorByName(self, name):
        return self.deleteMonitorById(self.getMonitorId(name))

    def iterMonitors(self, response_times=0, logs=0, uptime_ratio='', search=None, monitors=None):
        "Iterate all monitors."
        total = None
        offset = 0
        while total is None or offset < total:
            response = self.getMonitors(response_times, logs, uptime_ratio, offset=offset, limit=MONITORS_PER_PAGE, search=search, monitors=monitors)
            if not response[0]:
                return
            if total is None:
                total = int(response[1]['total'])
            offset += MONITORS_PER_PAGE
            for m in response[1]['monitors']['monitor']:
                yield m

if __name__ == "__main__":
    for arg in sys.argv:
        if arg.startswith("monitorFriendlyName="):
            monitorFriendlyName = arg.split("=")[1]
        elif arg.startswith("monitorURL="):
            monitorURL = arg.split("=")[1]
        elif arg.startswith("apiKey="):
            apiKey = arg.split("=")[1]
    if not monitorFriendlyName or not monitorURL:
        print ("Usage: uptimerobot.py monitorFriendlyName=\"name\" monitorURL=\"www.url.com\"")
        sys.exit(1)

    if not apiKey:
        homeDir = os.environ['HOME']
        pathToSettings = homeDir + "/.uptimeRobot.ini"
        try:
            Config = ConfigParser.ConfigParser()
            Config.read(pathToSettings)
            apiKey = Config.get("api", 'apiKey')
        except Exception as e:
            print(e)
            try:
                apiKey = raw_input("Can't continue without apiKey: ")
            except NameError:
                apiKey = input("Can't continue without apiKey: ")
            settingsFile = open(pathToSettings, 'w')
            settingsFile.write("; Settings for django-uptimerobot\n[api]\napiKey=%s" % apiKey)

    up = UptimeRobot(apiKey)
    if up.addMonitor(monitorFriendlyName, monitorURL):
        print("A new Monitor was installed successfully")
        sys.exit(0)
    else:
        print("There were some Errors, maybe the Monitor already exists?")
        sys.exit(1)
