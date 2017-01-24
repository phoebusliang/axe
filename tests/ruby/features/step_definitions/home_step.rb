Given /^Start the resi app for "(.*?)"$/ do |device|
  @homepage = @browser.open_app device
end

When /^Click "Search" button$/ do | |
  @srp = @homepage.click_search_btn
end

