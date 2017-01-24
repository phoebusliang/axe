require 'httparty'

class Browser
  attr_reader :driver

  def open_app(device)
    app_body = {:desiredCapabilities => {:bundleId => 'com.thoughtworks.StartKit'}}
    case device
      when '7p'
        @driver = HTTParty.post('http://localhost:8101/session', :body => app_body.to_json)
      when '6sp'
        @driver = HTTParty.post('http://localhost:8102/session', :body => app_body.to_json)
      else
        @driver = HTTParty.post('http://localhost:8101/session', :body => app_body.to_json)
    end
    HomePage.new(@driver)
  end

  def set_timeout(timeout)
    @driver.manage.timeouts.implicit_wait = timeout
  end

end
