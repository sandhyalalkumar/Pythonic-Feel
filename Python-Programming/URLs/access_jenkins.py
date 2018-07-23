import jenkinsapi
import jenkins
import os
os.environ.setdefault("PYTHONHTTPSVERIFY", "0")
jen = jenkins.Jenkins(url="https://us1salxhpu0066.corpnet2.com:9080/" ,username="skg80826", password="00326aef715012a227bf874180815695")
print jen.get_whoami()

#"https://skg80826:00326aef715012a227bf874180815695@us1salxhpu0066.corpnet2.com:9080