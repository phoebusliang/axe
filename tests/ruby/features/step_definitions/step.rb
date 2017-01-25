When /^Type the "(.*?)" in search box and select "(.*?)" from list$/ do |search_info, auto_suggest|
  @homepage.type_search_box search_info
  @homepage.select_option_from_auto_suggest auto_suggest if auto_suggest != ''
end

When /^Clean the keychain for device "(.*?)"$/ do |device|
  @browser.clean_keychain device
end

When /^Install the app for device "(.*?)"$/ do |device|
  @browser.install_app device
end

When /^Uninstall the app for device "(.*?)"$/ do |device|
  @browser.uninstall_app device
end