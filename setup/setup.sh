#!/usr/bin/env bash

/Users/twe/Documents/fbsimctl/fbsimctl 49066C3A-1BB3-440B-B660-C9AAF02B176A boot &
/Users/twe/Documents/fbsimctl/fbsimctl BC9D083F-111E-4022-A5BA-EF1BDB9B8AD0 boot
#/Users/twe/Documents/fbsimctl/fbsimctl 92A7F012-0270-4C06-83F9-DEF643883CC8 boot &
#/Users/twe/Documents/fbsimctl/fbsimctl A915EE37-E942-43D7-8F67-B1ADDC743433 boot

/Users/twe/Documents/fbsimctl/fbsimctl --state=booted install /Users/twe/Downloads/StartKit.app

/Users/twe/Documents/fbsimctl/fbsimctl --state=booted install /Users/twe/Downloads/xxx.app

#/Users/twe/Documents/fbsimctl/fbsimctl --state=booted install /Users/twe/Documents/workspace/xcode/xxx/Build/Products/Debug-iphonesimulator/xxxUITests-Runner.app
/Users/twe/Documents/fbsimctl/fbsimctl --state=booted install /Users/twe/Downloads/xxxUITests-Runner.app

/Users/twe/Documents/fbsimctl/fbsimctl 49066C3A-1BB3-440B-B660-C9AAF02B176A launch_xctest /Users/twe/Documents/workspace/xcode/WebDriverAgent/Build/Products/Debug-iphonesimulator/WebDriverAgentRunner-Runner.app/PlugIns/WebDriverAgentRunner.xctest tw.xxx --port 8101 -- listen &

/Users/twe/Documents/fbsimctl/fbsimctl BC9D083F-111E-4022-A5BA-EF1BDB9B8AD0 launch_xctest /Users/twe/Documents/workspace/xcode/WebDriverAgent/Build/Products/Debug-iphonesimulator/WebDriverAgentRunner-Runner.app/PlugIns/WebDriverAgentRunner.xctest tw.xxx --port 8102 -- listen &

#/Users/twe/Documents/fbsimctl/fbsimctl 92A7F012-0270-4C06-83F9-DEF643883CC8 launch_xctest /Users/twe/Documents/workspace/xcode/WebDriverAgent/Build/Products/Debug-iphonesimulator/WebDriverAgentRunner-Runner.app/PlugIns/WebDriverAgentRunner.xctest tw.xxx --port 8103 -- listen &
#
#/Users/twe/Documents/fbsimctl/fbsimctl A915EE37-E942-43D7-8F67-B1ADDC743433 launch_xctest /Users/twe/Documents/workspace/xcode/WebDriverAgent/Build/Products/Debug-iphonesimulator/WebDriverAgentRunner-Runner.app/PlugIns/WebDriverAgentRunner.xctest tw.xxx --port 8104 -- listen &
