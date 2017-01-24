require 'test/unit'
require 'page'
require 'search_result_page'

class PropertyDetailPage < Page
  include Test::Unit::Assertions

  def initialize(driver)
    @driver = driver
  end

end