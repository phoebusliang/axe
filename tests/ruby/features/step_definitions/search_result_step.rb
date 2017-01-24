When /^Click the property name "(.*?)" in search result page$/ do |property|
  @property_href = @srp.get_property_href property
  @pdp = @srp.click_property property
end

Then /^The type of property should be "(.*?)"$/ do |property_type|
  @srp.check_property_type property_type
end

Then /^The price of listings should be in range "(.*?)" and "(.*?)"$/ do |min_price, max_price|
  @srp.check_price_in_range min_price, max_price
end
