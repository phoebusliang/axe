require 'test/unit'
require 'page'
require 'search_result_page'

class HomePage < Page

  include Test::Unit::Assertions

  def initialize(driver)
    @driver = driver
  end

  def click_search_btn
    wait_for_script("return $('.searchButton')[0]", lambda { |ele| return ele }).click
    SearchResultPage.new(@driver)
  end


end
