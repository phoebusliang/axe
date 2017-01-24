When /^Type the "(.*?)" in search box and select "(.*?)" from list$/ do |search_info, auto_suggest|
  @homepage.type_search_box search_info
  @homepage.select_option_from_auto_suggest auto_suggest if auto_suggest != ''
end