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

  def tap(element_id)
    request_route = @url+'/session/'+@session_id+'/element/'+element_id+'/click'
    wait_for_response(request_route, 'post', '', lambda { |val| return val.to_s.include? element_id })
  end

  def type(element_id, val)
    request_route_clear = @url+'/session/'+@session_id+'/element/'+element_id+'/clear'
    wait_for_response(request_route_clear, 'post', '', lambda { |val| return val.to_s.include? element_id })

    request_route_type = @url+'/session/'+@session_id+'/element/'+element_id+'/value'
    body = {:value => val}
    wait_for_response(request_route_type, 'post', body, lambda { |val| return val.to_s.include? element_id })
  end

  def scroll(name, element_id)
    request_route = @url+'/session/'+@session_id+'/uiaElement/'+element_id+'/scroll'
    body = {:name => name}
    wait_for_response(request_route, 'post', body, lambda { |val| return val.to_s.include? @session_id })
  end

  def take_screenshot(to_file: './screenshot.png')
    request_route = @url+'/screenshot'
    response = wait_for_response(request_route, 'get', '', lambda { |val| return val.to_s.include? @session_id })
    File.write to_file, Base64.decode64(response['value'])
    response['output'] = to_file
    response
  end

end
