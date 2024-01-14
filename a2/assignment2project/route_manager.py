#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8 14:44:33 2023
Based on: https://www.kaggle.com/datasets/arbazmohammad/world-airports-and-airlines-datasets
Sample input: --AIRLINES="airlines.yaml" --AIRPORTS="airports.yaml" --ROUTES="routes.yaml" --QUESTION="q1" --GRAPH_TYPE="bar"
@author: Derek Knight
@author: V01012490
"""

from typing import List, Dict
import pandas as pd
from matplotlib import pyplot as plt
import yaml
import sys


def open_yaml_files(airlines_filename: str, airports_filename: str, routes_filename: str) -> List[List[Dict[str, str]]]:
    """
    Opens and loads airline, airport, and route yaml files to a list.
            Parameters
            ----------
                airlines_filename: str
                    Filename of the airlines yaml file.
                airports_filename: str
                    Filename of the airports yaml file.
                routes_filename: str
                    Filename of the routes yaml file.
            Returns
            -------
            List[List[Dict[str,str]]]
                list of list of dictionaries containing airline, airport, and route data.
    """
    with open(airlines_filename, "r") as airlines_yaml:
        airlines_list: List[Dict[str, str]] = yaml.safe_load(airlines_yaml)['airlines']

    with open(airports_filename, "r") as airports_yaml:
        airports_list: List[Dict[str, str]] = yaml.safe_load(airports_yaml)['airports']

    with open(routes_filename, "r") as routes_yaml:
        routes_list: List[Dict[str, str]] = yaml.safe_load(routes_yaml)['routes']

    return [airlines_list, airports_list, routes_list]


"""Sample function (removable) that illustrations good use of documentation.
            Parameters
            ----------
                input : str, required
                    The input message.

            Returns
            -------
                str
                    The text returned.
    """


def obtain_arguments(arguments: List[str]) -> List[str]:
    """
    Takes the command line arguments as a list and parsed the arguments
    into a formatted list of strings. The list of string is returned.
            Parameters
            ----------
                arguments : list[str]
                    Arguments is the command line arguments passed as a
                    list of strings.
            Returns
            -------
                list[str]
                    A list of the command line arguments returned in a list
                    of formatted strings.
    """
    index: int = 0
    argument_list: List[str] = []
    for args in arguments:
        if index > 0:
            argument_list.append(args.split('=')[1])
        index += 1

    return argument_list


def create_data_frames(data_lists: List[List[Dict[str, str]]]) -> List[pd.DataFrame]:
    """
    Take data in the form of a list of lists of dicts and returns the data in a formatted pandas DataFrame.
    Parameters
    ----------
        data_lists : list[list[dict]]
             list of list of dictionaries containing airline, airport, and route data.
    Returns
    -------
        list[pd.DataFrame]
            A list of airline, airport, and route pd.DataFrames.

    """
    airline_df: pd.DataFrame = pd.DataFrame(data_lists[0])

    airport_df: pd.DataFrame = pd.DataFrame(data_lists[1])

    route_df: pd.DataFrame = pd.DataFrame(data_lists[2])

    return [airline_df, airport_df, route_df]


def bar_chart(bar_df: pd.DataFrame, title: str, x_axis_label: str, y_axis_label: str, pdf_filename: str) -> None:
    """
    Takes a data frame, title, axis labels, and pdf filename and export a bar char to a pdf.
            Parameters
            ----------
                bar_df : pd.DataFrame
                    bar_df is a pd.DataFrame where the x-axis data is in the first column and the y-axis data is in the
                    second column.
                title: str
                    A str containing the title of the bar chart.
                x_axis_label : str
                    A str for the label of the x-axis of the bar chart.
                y_axis_label : str
                    A str for the label of the y-axis of the bar chart.
                pdf_filename : str
                    A str for the filename of the exported pdf file.
            Returns
            -------
                None
    """
    x_axis: pd.Series[str] = bar_df[bar_df.columns[0]]

    y_axis: pd.Series[int] = bar_df[bar_df.columns[1]]

    plt.bar(x_axis, y_axis, color="#be4d25", edgecolor="#85361a", linewidth=1.2, label="Title")

    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.xticks(rotation=55, ha='right', fontsize=7)

    plt.title(title)

    plt.savefig(pdf_filename, bbox_inches='tight')


def pie_chart(pie_df, title: str, pdf_filename: str):
    """
    Takes a data frame, title, and pdf filename and export a pie char to a pdf.
            Parameters
            ----------
                pie_df : pd.DataFrame
                    bar_df is a pd.DataFrame where the x-axis data is in the first column and the y-axis data is in the
                    second column.
                title: str
                    A str containing the title of the pie chart.
                pdf_filename : str
                    A str for the filename of the exported pdf file.
            Returns
            -------
                None
    """
    x_axis: pd.Series[str] = pie_df[pie_df.columns[0]]
    y_axis: pd.Series[int] = pie_df[pie_df.columns[1]]

    plt.pie(y_axis, labels=x_axis, wedgeprops={'linewidth': 0.25, 'edgecolor': 'white'}, textprops={'fontsize': 6.5}, autopct='%1.1f%%')

    plt.title(title)
    plt.savefig(pdf_filename)


def q1(data_frames_list: List[pd.DataFrame], chart_type: str) -> None:
    """
    Takes a list of airlines, airports, and route DataFrames and exports a csv file containing the top 15 airlines that
    offer the greatest number of routes with destination country as Canada. It also exports either a bar or a pie chart
    to a pdf depending on the second argument passed.
    Parameters
    ----------
        data_frames_list : list[pd.DataFrame]
             list of pd.DataFrames containing airline, airport, and route data.
        chart_type : str
            A str containing the type of chart to be exported to the pdf.
    Returns
    -------
        None
    """
    q1_df = pd.merge(data_frames_list[2], data_frames_list[1].reset_index(), left_on='route_to_airport_id',
                     right_on='airport_id', how='left')
    q1_df = pd.merge(q1_df, data_frames_list[0].reset_index(), left_on='route_airline_id', right_on='airline_id',
                     how='left')

    canada_df = q1_df['airport_country'] == 'Canada'
    q1_df = q1_df[canada_df]
    q1_df["subject"] = q1_df['airline_name'].astype(str) + " (" + q1_df['airline_icao_unique_code'] + ")"
    q1_df = q1_df.groupby('subject').route_airline_id.count().reset_index(name='statistic')
    q1_df = q1_df.sort_values(by=['statistic', 'subject'], ascending=[False, True]).head(20)

    q1_df.to_csv("q1.csv", index=False)
    if chart_type == 'bar':
        bar_chart(q1_df, "Top 20 Airlines by Number or Routes to Canada", "Airlines", "Number of Routes", "q1.pdf")
    elif chart_type == 'pie':
        pie_chart(q1_df, "Top 20 Airlines by Routes to Canada", "q1.pdf")


def q2(data_frames_list: List[pd.DataFrame], chart_type: str) -> None:
    """
    Takes a list of airlines, airports, and route DataFrames and exports a csv file containing the top 30 countries with
    the least appearances as destination country on the routes data. It also exports either a bar or a pie chart
    to a pdf depending on the second argument passed.
    Parameters
    ----------
        data_frames_list : list[pd.DataFrame]
            list of pd.DataFrames containing airline, airport, and route data.
        chart_type : str
            A str containing the type of chart to be exported to the pdf.
    Returns
    -------
        None
    """
    q2_df = pd.merge(data_frames_list[2], data_frames_list[1].reset_index(), left_on='route_to_airport_id',
                     right_on='airport_id', how='left')
    q2_df = q2_df.groupby('airport_country').route_airline_id.count().reset_index(name='statistic')
    q2_df.airport_country = q2_df.airport_country.str.strip()
    q2_df = q2_df.sort_values(by=['statistic', 'airport_country']).head(30)
    q2_df = q2_df.rename(columns={'airport_country': 'subject'})
    q2_df.to_csv("q2.csv", index=False)

    if chart_type == 'bar':
        bar_chart(q2_df, "Top 30 Countries with Least Appearances as Destination Country", "Country", "Number of Routes", "q2.pdf")
    elif chart_type == 'pie':
        pie_chart(q2_df, "Top 15 Airlines by Routes to Canada", "q2.pdf")


def q3(data_frames_list: List[pd.DataFrame], chart_type: str) -> None:
    """
    Takes a list of airlines, airports, and route DataFrames and exports a csv file containing the top 10 destination
    airports. It also exports either a bar or a pie chart to a pdf depending on the second argument passed.
    Parameters
    ----------
        data_frames_list : list[pd.DataFrame]
            list of pd.DataFrames containing airline, airport, and route data.
        chart_type : str
            A str containing the type of chart to be exported to the pdf.
    Returns
    -------
        None
    """
    q3_df = pd.merge(data_frames_list[2], data_frames_list[1].reset_index(), left_on='route_to_airport_id',
                     right_on='airport_id', how='left')

    q3_df["subject"] = q3_df['airport_name'].astype(str) + " (" + q3_df['airport_icao_unique_code'] + "), " + q3_df[
        'airport_city'] + ", " + q3_df['airport_country']

    q3_df = q3_df.groupby('subject').route_airline_id.count().reset_index(name='statistic')
    q3_df = q3_df.sort_values(by=['statistic'], ascending=False).head(10)

    q3_df.to_csv("q3.csv", index=False)

    if chart_type == 'bar':
        bar_chart(q3_df, "Top 10 Destination Airports", "Airport", "Number of Routes", "q3.pdf")
    elif chart_type == 'pie':
        pie_chart(q3_df, "Top 15 Airlines by Routes to Canada", "q3.pdf")


def q4(data_frames_list: List[pd.DataFrame], chart_type: str) -> None:
    """
    Takes a list of airlines, airports, and route DataFrames and exports a csv file containing the top 10
    destination cities. It also exports either a bar or a pie chart to a pdf depending on the second argument passed.
    Parameters
    ----------
        data_frames_list : list[pd.DataFrame]
            list of pd.DataFrames containing airline, airport, and route data.
        chart_type : str
            A str containing the type of chart to be exported to the pdf.
    Returns
    -------
        None
    """
    q4_df = pd.merge(data_frames_list[2], data_frames_list[1].reset_index(), left_on='route_to_airport_id',
                     right_on='airport_id', how='left')

    q4_df["subject"] = q4_df['airport_city'] + ", " + q4_df['airport_country']

    q4_df = q4_df.groupby('subject').route_airline_id.count().reset_index(name='statistic')
    q4_df = q4_df.sort_values(by=['statistic'], ascending=False).head(15)

    q4_df.to_csv("q4.csv", index=False)

    if chart_type == 'bar':
        bar_chart(q4_df, "Top 10 Destination Cities", "City", "Number of Routes", "q4.pdf")
    elif chart_type == 'pie':
        pie_chart(q4_df, "Top 15 Airlines by Routes to Canada", "q4.pdf")


def q5(data_frames_list: List[pd.DataFrame], chart_type: str) -> None:
    """
        Takes a list of airlines, airports, and route DataFrames and exports a csv file containing the unique top 10
        Canadian routes with most difference between the destination altitude and the origin altitude. It also exports
        either a bar or a pie chart to a pdf depending on the second argument passed.
        Parameters
        ----------
            data_frames_list : list[pd.DataFrame]
                list of pd.DataFrames containing airline, airport, and route data.
            chart_type : str
                A str containing the type of chart to be exported to the pdf.
        Returns
        -------
            None
        """
    q5_df = pd.merge(data_frames_list[2], data_frames_list[1].reset_index(), left_on='route_to_airport_id',
                     right_on='airport_id', how='left')

    q5_df = q5_df.rename(columns={'airport_icao_unique_code': 'to_airport_code'})
    airports_df = data_frames_list[1]

    airports_df = airports_df.drop(columns=['airport_name', 'airport_city'])

    q5_df = pd.merge(q5_df, airports_df.reset_index(), left_on='route_from_aiport_id', right_on='airport_id',
                     how='left')
    q5_df = q5_df.rename(columns={'airport_icao_unique_code': 'from_airport_code'})
    q5_df.airport_altitude_x = pd.to_numeric(q5_df.airport_altitude_x, errors='coerce')
    q5_df.airport_altitude_y = pd.to_numeric(q5_df.airport_altitude_y, errors='coerce')

    q5_df["subject"] = q5_df['from_airport_code'].astype(str) + "-" + q5_df['to_airport_code']
    q5_df["statistic"] = q5_df.airport_altitude_x - q5_df.airport_altitude_y
    canada_df = q5_df['airport_country_x'] == 'Canada'
    q5_df = q5_df[canada_df]
    canada_df = q5_df['airport_country_y'] == 'Canada'
    q5_df = q5_df[canada_df]

    q5_df['statistic'] = q5_df['statistic'].abs()
    q5_df = q5_df.sort_values(by=['statistic'], ascending=False).head(10)
    q5_df = q5_df[['subject', 'statistic']]

    q5_df.to_csv("q5.csv", index=False)

    if chart_type == 'bar':
        bar_chart(q5_df, "Top 10 Canadian Routes by Difference in Altitude", "Airline Route", "Altitude Difference",
                  "q5.pdf")
    elif chart_type == 'pie':
        pie_chart(q5_df, "Top 15 Airlines by Routes to Canada", "q5.pdf")


def main():

    argument_list: List[str] = obtain_arguments(sys.argv)

    data_lists: List[List[Dict[str, str]]] = open_yaml_files(argument_list[0], argument_list[1], argument_list[2])

    data_frame_list: list[pd.DataFrame] = create_data_frames(data_lists)

    if argument_list[3] == 'q1':
        q1(data_frame_list, argument_list[4])
    elif argument_list[3] == 'q2':
        q2(data_frame_list, argument_list[4])
    elif argument_list[3] == 'q3':
        q3(data_frame_list, argument_list[4])
    elif argument_list[3] == 'q4':
        q4(data_frame_list, argument_list[4])
    elif argument_list[3] == 'q5':
        q5(data_frame_list, argument_list[4])


if __name__ == '__main__':
    main()
