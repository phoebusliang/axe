require 'httparty'
require 'json'

class Browser
  attr_reader :driver

  def initialize
    @app_path = '/Users/twe/Downloads/StartKit.app'
    @command_path = '/Users/twe/Documents/fbsimctl/fbsimctl'
    @bundle_id = 'com.thoughtworks.StartKit'
  end

  def wait_for_response(request_route, request_type, body, lamb, timeout=10)
    start = Time.now
    while Time.now - start < timeout
      case request_type
        when 'post'
          val = HTTParty.post(request_route, :body => body.to_json)
        when 'get'
          val = HTTParty.get(request_route)
        when 'delete'
          val = HTTParty.delete(request_route, :body => body.to_json)
      end
      if lamb.call(val)
        return val
      end
    end
    raise Exception, val
  end

  def open_app(device)
    app_body = {:desiredCapabilities => {:bundleId => 'com.thoughtworks.StartKit'}}
    response = HTTParty.post(DEVICE_URL[device], :body => app_body.to_json)
    @url = DEVICE_URL[device]
    @session_id = response['sessionId']
    # HomePage.new(@driver)
    find_elements_by_class 'XCUIElementTypeTextField'
  end

  def clean_keychain(device)
    system(@command_path + ' ' + DEVICE_INFO[device] +' clear_keychain ' + @bundle_id)
  end

  def install_app(device)
    system(@command_path + ' ' + DEVICE_INFO[device] +' install ' + @app_path)
  end

  def uninstall_app(device)
    system(@command_path + ' ' + DEVICE_INFO[device] +' uninstall ' + @bundle_id)
  end

  def find_elements_by_class(class_val)
    body = {:using => 'class name', :value => class_val}
    request_route = @url+'/'+@session_id+'/elements'

    response = wait_for_response(request_route, 'post', body, lambda { |val| return val.to_s.include? class_val })
    response['value'].collect { |item| item['ELEMENT'] }
  end

  

end
