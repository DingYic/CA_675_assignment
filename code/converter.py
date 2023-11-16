import os
import email
import pandas as pd
import re
from bs4 import BeautifulSoup

import warnings

warnings.filterwarnings('ignore')


def removeHtmlTags(data):
    # define beautiful soup variable
    soup = BeautifulSoup(data, "lxml")

    # for loop to iterate through soup variables and remove the tags
    for script in soup(['script', 'style', 'head', 'meta', 'noscript']):
        # decompose method to remove the tags as well as all the inner content from the data
        script.decompose()

    # remove all the extra white spaces from the data
    data = " ".join(soup.stripped_strings)
    return data


def cleanData(data):
    if not data:
        return ""
    else:
        return removeHtmlTags(data)


def formatString(str):
    str = re.sub(",", "", str)
    str = re.sub("\"", "", str)
    formattedString = re.sub("\n", "", str)
    return formattedString


def createData():
    # directory path of the data
    DIR_PATH = "dataset/raw_data"

    OUTPUT_PATH = "dataset"

    # defined a data frame to store data
    df = pd.DataFrame(columns=["from_email", "to_email", "subject", "body"])

    # define sequence variable to update data frame location
    sequence = 1

    # iterate the files and store them in the data frame in a structured format
    # the loop is also used to fetch files present inside a directory in the data folder
    for root, dirs, files in os.walk(DIR_PATH):
        for f in files:
            with open(os.path.join(root, f), "r", encoding="ISO-8859-1") as file:

                # printing file name to identify processing of the file
                print("Processing file: " + f)

                # read content from the file
                content = file.read()

                # parse the content using email library
                parsed_content = email.message_from_string(content)

                # extract information from the parsed_content such as {subject, to email, from email, body}
                # format the string by removing unnecessary special characters and white spaces
                subject = formatString(str(parsed_content["subject"]))
                to_email = formatString(str(parsed_content["to"]))
                from_email = formatString(str(parsed_content["from"]))

                # extracting the message from the parsed_content
                body = ""
                if parsed_content.is_multipart():
                    for payload in parsed_content.get_payload():
                        body = body + str(payload)
                else:
                    body = parsed_content.get_payload()

                # clean the data by removing html tags and scripts from the body to store in a human readable format
                body = str(cleanData(body))

                # format body by removing unnecessary white spaces and comma's
                body = formatString(body)

                # insert data into the data frame
                df.loc[sequence] = [from_email, to_email, subject, body]
                # increase the sequence for the position in data frames
                sequence = sequence + 1

    # write the structured data frame in csv
    df.to_csv(OUTPUT_PATH + "/processed_data.csv", index=False)
    print("Data generation completed and file is present at " + OUTPUT_PATH)


if __name__ == "__main__":
    createData()