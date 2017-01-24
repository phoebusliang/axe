require 'cucumber'
require 'require_all'

require_all 'lib'

Before do |scenario|
  @browser = Browser.new(ENV['DRIVER'])
end

After do |scenario|
  if scenario.failed?
    # @browser.driver.save_screenshot(File.join(File.dirname(__FILE__), '..'+File::SEPARATOR+'..'+File::SEPARATOR, 'report', scenario.name + '.png'))
  end
  @browser.driver.quit
end

AfterStep do |scenario|
  #do something
end

