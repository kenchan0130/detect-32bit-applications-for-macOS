#!/usr/bin/env python
# -*- coding:utf-8 -*-

import plistlib
import subprocess
import platform
import re
import sys
import codecs


# System application is excluded by default because it will not be 32bit due to version upgrade.
# If you want to get system app, you can change this variable to 'False'.
IGNORE_SYSTEM_APP = True


# Some apps may have some utf-8 charactors.
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
sys.stderr = codecs.getwriter("utf-8")(sys.stderr)


def formatApplicationForConsole(application):
    path = application["path"]
    if "version" in application:
    	version = application["version"]
    	return "%s | %s" % (path, version)
    else:
    	return path


result = ""
# Confirmation is made because it affects macOS Catalina (10.15) and below.
if int(platform.mac_ver()[0].split(".")[1]) < 15:
    sp_applications_data_type_xml = subprocess.check_output(["/usr/sbin/system_profiler",  "SPApplicationsDataType", "-xml"])
    sp_applications_data_type = plistlib.readPlistFromString(sp_applications_data_type_xml)

    all_applicatons = sp_applications_data_type[0]["_items"]
    finded_32_bit_applications = [application for application in all_applicatons if application["has64BitIntelCode"] == "no"]
    if IGNORE_SYSTEM_APP:
        repatter = re.compile(r"^/System", re.IGNORECASE)
        finded_32_bit_applications = [application for application in finded_32_bit_applications if not repatter.match(application["path"])]

    result = "\n".join(map(formatApplicationForConsole, finded_32_bit_applications))

# Jamf Pro collects the results when sandwiched between <result>
print("<result>%s</result>" % "None" if result == "" else result)
