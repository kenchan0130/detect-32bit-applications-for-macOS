#!/usr/bin/env python
# -*- coding:utf-8 -*-

import plistlib
import subprocess

def formatApplicationForConsole(application):
    path = application["path"]
    if "version" in application:
    	version = application["version"]
    	return "%s | %s" % (path, version)
    else:
    	return path


sp_applications_data_type_xml = subprocess.check_output(["/usr/sbin/system_profiler",  "SPApplicationsDataType", "-xml"])
sp_applications_data_type = plistlib.readPlistFromString(sp_applications_data_type_xml)

all_applicatons = sp_applications_data_type[0]["_items"]
finded_32_bit_applications = [application for application in all_applicatons if application["has64BitIntelCode"] == "no"]
formattedApplicaions = "\n".join(map(formatApplicationForConsole, finded_32_bit_applications))

print("<result>%s</result>" % formattedApplicaions)
