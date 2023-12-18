from bs4 import BeautifulSoup
import os
import csv
import openai
import requests

# Directory containing HTML files
html_files_directory = '/home/amr/PycharmProjects/journal_of_management/htmls'


def get_authors_dict(soup):
    # Find the div with the id "tab-contributors"
    contributors_div = soup.find('section', {'class': 'core-authors'})

    # Extract the text content of the divs
    if not contributors_div:  # abstracts_div and
        return {}
        # abstracts_content = abstracts_div.text.strip()
    # contributors_content = contributors_div.text.strip()
    # citing_articles_element = citing_articles_element.text.strip()
    author_divs = contributors_div.find_all('div', {'id': lambda x: x and x.startswith('con')})

    # Initialize a dictionary to store author names and affiliations
    authors_dict = {}

    for author_div in author_divs:
        # Find the author's name
        givenName = author_div.find('span', {'property': 'givenName'})
        givenName = givenName.text if givenName else ''
        familyName = author_div.find('span', {'property': 'familyName'})
        familyName = familyName.text if familyName else ''
        author_name = givenName + ' ' + familyName

        # Find the author's affiliation
        affiliation = author_div.find('div', {'property': 'affiliation'})

        # Add the author and affiliation to the dictionary
        if author_name.strip():
            authors_dict[author_name] = affiliation.text.strip() if affiliation else ""
    return authors_dict


def get_citing_dict(soup):
    citing_articles_element_dict = {}
    tags = soup.find_all('span', class_='font-weight-semibold',
                         string=lambda t: any(c in t for c in ["Web of Science:", "Crossref:"]))
    if tags:
        for tag in tags:
            tag_list = tag.text.split(":")
            citing_articles_element_dict[tag_list[0]] = int(tag_list[1].strip())

    return citing_articles_element_dict


def get_the_issue_value(soup):

    main_element = soup.find("div", {"class": "core-enumeration"})
    if not main_element:
        return ""
    volume_span = main_element.find('span', {'property': 'volumeNumber'})
    issue_span = main_element.find('span', {'property': 'issueNumber'})

    # Get the text content
    volume_text = volume_span.get_text(strip=True) if volume_span else None
    issue_text = issue_span.get_text(strip=True) if issue_span else None

    # Create the desired text
    result_text = f"Volume {volume_text}, Issue {issue_text}" if volume_text and issue_text else None

    return result_text


def get_article_date(soup):
    tag = soup.find("div", {"class": "meta-panel__onlineDate"})
    if not tag:
        return ""
    tag_data = tag.text.strip("First published online")
    return tag_data


def get_article_name(soup):
    tag = soup.find("h1", {"property": "name"})
    if not tag:
        return ""
    tag_data = tag.text
    return tag_data


def get_abstract_paragraph(soup):
    abstracts_div = soup.find('div', {'id': 'abstracts'})
    abstracts_text = abstracts_div.find("div", {"role": "paragraph"}).text if abstracts_div else ''
    return abstracts_text


def get_key_words_list(soup):
    keywords_section = soup.find('section', {"property": "keywords"})
    if not keywords_section:
        return []
    keywords_as = keywords_section.find_all('a', {"alt": "Search on this keyword"})
    keywords_list = [a.text for a in keywords_as]
    return keywords_list


# Loop through HTML files in the directory
articles_dict = {}
for filename in os.listdir(html_files_directory):
    if filename.endswith('.html'):
        file_path = os.path.join(html_files_directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the HTML content from the file
            html_content = file.read()

            soup = BeautifulSoup(html_content, 'html.parser')

            article_date = get_article_date(soup)

            citing_articles_element_dict = get_citing_dict(soup)

            issue = get_the_issue_value(soup)

            abstract_paragraph = get_abstract_paragraph(soup)

            authors_dict = get_authors_dict(soup)

            article_name = get_article_name(soup).strip()

            keywords_list = get_key_words_list(soup)
            print(f"File: {filename}")

            articles_dict[article_name] = {
                'Article date': article_date,
                'Citing': citing_articles_element_dict,
                'Issue info': issue,
                'Abstract Paragraph': abstract_paragraph,
                'Authors': authors_dict,
                'Keywords': keywords_list,
            }
            # Parse the HTML content with BeautifulSoup

            # Find the div with the id "abstracts"

            # if filename:
                # Print or process the content as needed
                # print(f"File: {filename}")
                # print("Abstracts Content:")
                # print(abstracts_content)
                # print("Keywords:")
                # print(keywords_list)
                # print("\nContributors Content:")
                # print(authors_dict)
                # print("\nArticle name:")
                # print(article_name)
                # print("\nArticle Date:")
                # print(article_date)
                # print("\nCiting articles element:")
                # print(citing_articles_element_dict)
                # print("\nIssue Info:")
                # print(issue)

            #     print("\n" + "=" * 50 + "\n")
            # else:
            #     print(f"Could not find 'abstracts' or 'tab-contributors' in {filename}")

print(len(articles_dict))


def export_to_csv_file(file_name, articles_dict):

    # Define the CSV header
    header = [
        'Issue info', 'Article date', 'Article Name', 'Article Abstract', 'Web of Science', 'Crossref',
        'Research Question', 'Keywords', 'Theme Analysis', 'Research Methodology'
    ]
    # Write to CSV
    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)

        for article_name, article_data in articles_dict.items():
            issue_info = article_data['Issue info']
            article_date = article_data['Article date']
            if article_data['Citing']:
                if article_data['Citing']['Web of Science']:
                    web_of_science = article_data['Citing']['Web of Science']
                else:
                    web_of_science = ''
                if article_data['Citing']['Crossref']:
                    crossref = article_data['Citing']['Crossref']
                else:
                    crossref = ''
            else:
                web_of_science = ''
                crossref = ''
            abstract = article_data['Abstract Paragraph']
            keywords = article_data['Keywords']
            research_question = ''  # Fill in your actual data
            theme_analysis = ''  # Fill in your actual data
            research_methodology = ''  # Fill in your actual data
            # Flatten authors' data
            authors_data = article_data['Authors']
            authors_info = []

            for author, organization in authors_data.items():
                country = ''  # Fill in your actual data
                gender = ''  # Fill in your actual data
                authors_info.extend([author, organization, country, gender])

            # Create a row for the CSV
            row = [
                issue_info, article_date, article_name, abstract, web_of_science, crossref,
                research_question, ", ".join(keywords), theme_analysis, research_methodology
            ]
            row.extend(authors_info)

            # Write the row to the CSV file
            csv_writer.writerow(row)

    print(f'Data has been written to {csv_filename}')


csv_filename = 'output_stage_1.csv'

export_to_csv_file(csv_filename, articles_dict)