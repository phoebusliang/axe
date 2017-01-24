require 'test/unit'
require 'page'

class SearchResultPage < Page
  include Test::Unit::Assertions

  def initialize(driver)
    @driver = driver
  end

  def click_property name
    wait_for_script("return $('.row.container article h2 a:contains(#{name})')[0]", lambda { |ele| return ele }).click()
    PropertyDetailPage.new(@driver)
  end

end