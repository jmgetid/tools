# Using JIRA CLIENT from http://readthedocs.org/docs/jira-python/
# Modified the client.py in C:\Software\cygwin\lib\python2.7\site-packages\jira to bypass the private certifificate from jirapdi.tid.es

from jira.client import JIRA
from subprocess import Popen, PIPE
import re

###########################
# Retrieve the log of merged branches between two tags
###########################
def gitLog(initTag, endTag, repoDir):
	ref = '..'.join([initTag,endTag])
	cmd = ['git', 'log', '--oneline', ref]	
	gitlog = Popen(cmd, cwd=repoDir, stdout=PIPE)
	grep = Popen(['grep', 'Merge pull request'], stdin=gitlog.stdout, stdout=PIPE, stderr=PIPE)
	grep.wait()
	out = grep.stdout.read()
	#out, err = grep.communicate()
	return out

###########################
# Get the issues list from the log
###########################
def issuesList(ilist):
	p = re.compile('\w*-\d+')
	issueNumbers = p.findall(ilist)
	# Remove duplicated issues by list conversion to set and then to list again
	issueNumbers = list(set(issueNumbers))
	return issueNumbers

###########################
# Retrieve info from JIRA for each issue
###########################
def jiraSummary(issue):
	jac = JIRA(options={'server': 'https://jirapdi.tid.es'}, basic_auth=('user', 'password'))
	#jac = JIRA(options={'server': 'https://jirapdi.tid.es','verify': 'False'}, basic_auth=('username','password'))
	issue = jac.issue(issue, fields='summary,status')
	return issue
	

###########################
# Release Notes example
###########################

print "*** git log command:"
#logList = gitLog('2.3.1/CC','release/2.3.1','C:\Users\cramiro\pdihub\pe\pe-dbe-common')
#logList = gitLog('2.3.1/CC','release/2.3.1','C:\Users\cramiro\pdihub\pe\pe-dbe-payment')
logList = gitLog('1.0.0/CC','1.1.0/CC','d:\Code\pdihub\pe\pe-dbe-expenditurelimit')
#logList = gitLog('2.3.1/CC','release/2.3.1','C:\Users\cramiro\pdihub\pe\pe-dbe-subscriptions')
print logList


print "*** Issues after Reg-Exp:"
issues = issuesList(logList)
print issues

print "\n*** Data retrieved from JIRA:"
for issue in issues:
	issueJira = jiraSummary(issue)
	#issue=[issueJira.key,issueJira.fields.summary
	print "  ".join([issueJira.key,issueJira.fields.summary])
	print str(issueJira.fields.status)	
	
