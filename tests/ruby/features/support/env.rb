require 'cucumber'
require 'require_all'

require_all 'lib'

DEVICE_INFO = Hash['7p' => '49066C3A-1BB3-440B-B660-C9AAF02B176A', '6sp' => 'BC9D083F-111E-4022-A5BA-EF1BDB9B8AD0']

DEVICE_URL = Hash['7p' => 'http://localhost:8101/session', '6sp' => 'http://localhost:8102/session']

TIME = 1

Before do |scenario|
  @browser = Browser.new()
end

After do |scenario|
  # if scenario.failed?
  # @browser.driver.save_screenshot(File.join(File.dirname(__FILE__), '..'+File::SEPARATOR+'..'+File::SEPARATOR, 'report', scenario.name + '.png'))
  # end
  # @browser.driver.quit
  # @browser.clean_keychain '7p'
  # p tag.name
end

After ('@complete-7p') do
  @browser.clean_keychain '7p'
  @browser.uninstall_app '7p'
  @browser.install_app '7p'
end

After ('@complete-6sp') do
  @browser.clean_keychain '6sp'
  @browser.uninstall_app '6sp'
  @browser.install_app '6sp'
end

AfterStep do |scenario|
  #do something
end

