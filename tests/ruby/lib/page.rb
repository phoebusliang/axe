class Page

  def wait_for_script script, lamb
    start = Time.now
    while Time.now - start < 15
      val = @driver.execute_script(script)
      if lamb.call(val)
        return val
      end
    end
    raise Exception, val
  end

end
