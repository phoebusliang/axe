import time
import tests.python.steps.log as log
import requests
import os
import datetime
import calendar
import json


def wait_for_element(context, request_type, body, check=bool, timeout=30, error_template="Value is %s"):
    start = time.time()
    while time.time() - start < timeout:
        if request_type == "post":
            response = requests.post(context.route, data=json.dumps(body))
        else:
            response = requests.get(context.url)
        response = json.loads(response.text)
        if check(response):
            return response
    raise AssertionError(error_template % response)


def wait_for_script(browser, script, check=bool, timeout=30, error_template="Value is %s"):
    start = time.time()
    while time.time() - start < timeout:
        value = browser.execute_script(script)
        if check(value):
            return value
    raise AssertionError(error_template % value)


def wait_for_css_selector(browser, selector, timeout=30, error_template="%s"):
    start = time.time()
    while time.time() - start < timeout:
        elements = browser.find_elements_by_css_selector(selector)
        if len(elements) > 0:
            return
    raise AssertionError(error_template % "Element Not Found")


def do_find_fund_index(browser, name):
    fund_count = len(browser.find_elements_by_css_selector(".fund-summary-row"))
    for i in range(0, fund_count):
        fund_name = browser.find_elements_by_css_selector('.fund-summary-row div.description h3')[i].text
        if name in fund_name:
            return i


def verify_fund_row(browser, index, row):
    for heading in row.headings:
        verify_cell_content(browser, index, heading, row[heading])


def verify_additional_issues(browser, row_index, row):
    for additional_issue_idx, head in enumerate(row.headings):
        verify_additional_issue(browser, row_index, row[head], additional_issue_idx)


def verify_instrument_detail_table_row(browser, row_index, row):
    for head_idx, head in enumerate(row.headings):
        if head != 'NAV Comment':
            verify_instrument_detail_table_row_cell(browser, row_index, head_idx, row[head])
        else:
            verify_instrument_detail_comments(browser, row_index, head_idx, row[head])


def verify_additional_issue(browser, row_index, value, additional_issue_idx):
    cell_script = "return $('.fund-summary-row-pane:eq(" + str(
        row_index) + ") .fund-summary-row-detail .additional-issue-row .additional-category:eq(" + str(
        additional_issue_idx) + ") div').text()"
    try:
        # assert value.strip() in cell_content.strip()
        cell_content = wait_for_script(browser, cell_script, check=lambda content: value.strip() in content.strip())
    except AssertionError:
        raise AssertionError(
            log.Formatter.regular_category_table.format(row_index, additional_issue_idx, cell_content, value))
    except:
        raise AssertionError(log.Formatter.unexpected_assertion)


def verify_cell_content(browser, row_index, name, value):
    cate_index = find_category_index(name)
    cell_script = "return $('.fund-summary-row:eq(" + str(row_index) + ")> *:eq(" + str(cate_index) + ")').text()"
    try:
        cell_content = wait_for_script(browser, cell_script, check=lambda content: content.strip() == value.strip())
    except AssertionError:
        raise AssertionError(log.Formatter.regular_category_table.format(row_index, cate_index, cell_content, value))
    except:
        raise AssertionError(log.Formatter.unexpected_assertion)


def verify_instrument_detail_table_row_cell(browser, row_index, head_idx, value):
    cell_sel = detail_cell_selector(row_index, head_idx + 1)
    try:
        cell_content = wait_for_script(browser, "return $('{0}').text()".format(cell_sel),
                                       check=lambda text: value.strip() in text.strip())
    except AssertionError:
        raise AssertionError(log.Formatter.instrument_detail_table.format(row_index, head_idx, cell_content, value))
    except:
        raise AssertionError(log.Formatter.unexpected_assertion)


def verify_instrument_detail_comments(browser, row_index, head_idx, value):
    cell_sel = detail_cell_selector(row_index, head_idx + 1)
    try:
        cell_content = wait_for_script(browser, "return $('{0} input').val()".format(cell_sel),
                                       check=lambda text: value.strip() in text.strip())
    except AssertionError:
        raise AssertionError(log.Formatter.instrument_detail_table.format(row_index, head_idx, cell_content, value))
    except:
        raise AssertionError(log.Formatter.unexpected_assertion)


def find_category_index(name):
    category_index_map = dict(Indicator=0,
                              Description=1,
                              Adj_Opening_Capital=2,
                              Single_Source=3,
                              Exceptions=4,
                              Base_MV_Diff=5,
                              With50bp_PL_Difference=6,
                              Excluded_From_MD_Escalation=7,
                              Additional_Issues=8)
    return category_index_map[name]


def clean(url, type='put'):
    start = time.time()
    while time.time() - start < 15:
        if type == 'delete':
            req = requests.delete(url)
        else:
            req = requests.put(url)
        if req.status_code == 201:
            return
        time.sleep(0.2)
    return


def clean_env(uuid, bundle_id='athome.lu.v3'):
    url = 'http://localhost:8080/'
    requests.get(url + uuid + '/' + bundle_id)


def get_detail_pane_head_index(browser, head_name):
    heads = browser.execute_script("return $('.instrument-table .header-cell span').map("
                                   " function() {return $(this).text();}"
                                   ").get()")
    return heads.index(head_name) + 1


def detail_cell_selector(row_idx, col_idx):
    return '.instrument-table .fixedDataTableLayout_rowsContainer > div:eq(2) >  \
               div:eq({0}) .fixedDataTableCellGroupLayout_cellGroup:eq(1) >  \
               div:eq({1})'.format(row_idx, col_idx)


def generate_file(file_name, file_size):
    with open(file_name, 'w') as f:
        f.seek(1024 * 1024 * int(file_size))
        f.write('\n')
    start = time.time()
    while time.time() - start < 60:
        size = os.path.getsize(file_name)
        if int(size) >= int(file_size):
            return
        time.sleep(0.2)
    return


def get_today(format_type='%b %m%Y'):
    return datetime.date.today().strftime(format_type)


def get_yesterday(format_type='%b %m%Y'):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    return yesterday.strftime(format_type)


def get_prior_month_end(format_type='%b %m%Y'):
    d = datetime.date.today()
    year = d.year
    month = d.month
    if month == 1:
        month = 12
        year -= 1
    else:
        month -= 1
    days = calendar.monthrange(year, month)[1]
    return (datetime.datetime(year, month, 1) + datetime.timedelta(days=days - 1)).strftime(format_type)


def get_prior_year_end(format_type='%b %m%Y'):
    d = datetime.date.today()
    year = d.year - 1
    days = calendar.monthrange(year, 12)[1]
    return (datetime.datetime(year, 12, 1) + datetime.timedelta(days=days - 1)).strftime(format_type)


def check_file_existed(file):
    start = time.time()
    while time.time() - start < 60:
        if os.path.isfile(os.path.join(os.getcwd() + os.sep + 'data' + os.sep + file)):
            break
        time.sleep(0.2)


def clean_keychian(uuid, bundle_id='athome.lu.v3', url='http://localhost:8080/'):
    requests.get(url + uuid + '/' + bundle_id)
