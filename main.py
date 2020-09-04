import requests
from bs4 import BeautifulSoup

BASE_URL = r'https://www.sec.gov'


def _build_hardcoded_url():
    base_url = r'https://www.sec.gov'
    data_url = r'/Archives/edgar/data/'
    cik_number = r'789019'
    filing_number = r'000156459020019706'
    filing_directory_url = base_url + data_url + cik_number + '/' + filing_number + '/index.json'
    return filing_directory_url


def get_filing_summary_xml_url(filing_url):
    filing_contents = requests.get(filing_url).json()

    for filing in filing_contents['directory']['item']:
        if filing['name'] == 'FilingSummary.xml':
            return BASE_URL + filing_contents['directory']['name'] + '/' + filing['name']

    return ''


def get_filing_summary_soup(filing_summary_xml_url):
    filing_summary_xml = requests.get(filing_summary_xml_url).content
    filing_soup = BeautifulSoup(filing_summary_xml, 'lxml')
    return filing_soup


def get_all_valid_reports(filing_summary_soup):
    # last report does not contain all components that make up other reports, therefore excluded
    return filing_summary_soup.find('myreports').find_all('report')[:-1]


def get_report_lst(reports):
    report_lst = []
    for report in reports:
        report_dict = {}
        report_dict['long_name'] = report.longname.text
        report_dict['short_name'] = report.shortname.text
        report_dict['position'] = report.position.text
        report_dict['category'] = report.menucategory.text
        report_dict['url'] = report.htmlfilename.text

        report_lst.append(report_dict)
    return report_lst


def get_financial_statements_url(report_lst):
    statement_names_lst = ['BALANCE SHEETS', 'INCOME STATEMENTS', 'CASH FLOWS STATEMENTS', 'STOCKHOLDER\'S EQUITY STATEMENTS']

    financial_statements_url_dict = {}

    for report in report_lst:
        if report['short_name'] in statement_names_lst:
            financial_statements_url_dict[report['short_name']] = report['url']
            print('*'*100)
            print('NAME OF STATEMENT - {}'.format(report['short_name']))
            print('URL - {}'.format(report['url']))

    return financial_statements_url_dict


if __name__ == "__main__":
    directory_url = _build_hardcoded_url()
    filing_summary_url = get_filing_summary_xml_url(directory_url)
    filing_soup = get_filing_summary_soup(filing_summary_url)
    reports =  get_all_valid_reports(filing_soup)
    report_list = get_report_lst(reports)
    get_financial_statements_url(report_list)

    print('Hello World!')
