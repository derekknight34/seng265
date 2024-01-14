/** @file route_manager.c
 *  @brief A pipes & filters program that uses conditionals, loops, and string processing tools in C to process airline routes.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Saasha J.
 *  @author Victoria L.
 *  @author STUDENT_NAME Derek Knight
 *
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef char Strings[10][200];

/**
 * Function: obtain_arguments
 * --------------
 * @brief The obtain_arguments function takes the inputs from the command line and parses them into typedef Strings.
 *
 * @param num_arg The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @param filter_array The Strings array to pass the filter arguments into.
 * @param field_array The Strings array to pass the field arguments into.
 * @param sort_filter_array A Srings array that standardizes the array numbers where the filter arguments are stored.
 */

void  obtain_arguments(int num_arg, char *argv[], Strings* filter_array, Strings* field_array, Strings* sort_filter_array) {
    
    int i;

    char field[1000] = { 0 };
    char filter[1000] = { 0 };

    for (i = 1; i < num_arg; i++) {
        sscanf(argv[i], "--%[^=]=%[^\n]", field_array[i - 1][0], filter_array[i - 1][0]);
    }

    for (i = 1; i < num_arg; i++) {
 
        char temp[200];
        char air_line_str[200];
        char src_city_str[200];
        char src_country_str[200];
        char dest_city_str[200];
        char dest_country_str[200];

        strcpy(air_line_str, "AIRLINE");
        strcpy(src_city_str, "SRC_CITY");
        strcpy(src_country_str, "SRC_COUNTRY");
        strcpy(dest_city_str, "DEST_CITY");
        strcpy(dest_country_str, "DEST_COUNTRY");

        sprintf(temp, "%s", field_array[i][0]);

        if (strcmp(temp, air_line_str) == 0) {
            strcpy(sort_filter_array[0][0], filter_array[i][0]);
        }
        else if (strcmp(temp, src_city_str) == 0) {
            strcpy(sort_filter_array[1][0], filter_array[i][0]);
        }
        else if (strcmp(temp, src_country_str) == 0) {
            strcpy(sort_filter_array[2][0], filter_array[i][0]);
        }
        else if (strcmp(temp, dest_city_str) == 0) {
            strcpy(sort_filter_array[3][0], filter_array[i][0]);
        }
        else if (strcmp(temp, dest_country_str) == 0) {

            strcpy(sort_filter_array[4][0], filter_array[i][0]);
        }
    }
}

/**
 * Function: process_lines
 * --------------
 * @brief The process_lines function reads the input csv file, filters the data, and outputs to output.txt.
 * 
 * @param filename The filename of the input csv file.
 * @param sort_filter_array The Srings array with the standard the array numbers where the filter arguments are stored.
 * sort_filter_array[0] airline
 * sort_filter_array[1] src_city
 * sort_filter_array[2] src_country
 * sort_filter_array[3] dest_city
 * sort_filter_array[4] dest_country
 * @param num_arg The number of filter arguments passed to the program.
 */

void process_lines(char* filename, Strings* sort_filter_array, int num_arg) {

    FILE* ifp;

    ifp = fopen(filename, "r");
    
    FILE* output_file;
    output_file = fopen("output.txt", "w");

    if (ifp == NULL) {
        printf("Error opening file %s\n", filename);
    }
    char AIRLINE_NAME[200];
    char AIRLINE[200]; //airline_icao_unique_code
    char SRC_CITY[200]; //from_airport_city
    char SRC_COUNTRY[200]; //from_airport_country
    char SRC_AIRPORT_NAME[200];
    char SRC_AIRPORT_CODE[200];
    char DEST_AIRPORT_NAME[200];
    char DEST_CITY[200]; //to_airport_city
    char DEST_COUNTRY[200]; //to_airport_country
    char DEST_AIRPORT_CODE[200];

    char* sp;

    int i = 0;

    char csv_line[5000];
    while (fgets(csv_line, 5000, ifp) != NULL) {

        sp = strtok(csv_line, ",");
        if (sp == NULL) {
            ;
        }
        else {
            strcpy(AIRLINE_NAME, sp);
        }
        sp = strtok(NULL, ",");

        if (sp == NULL) {
            ;
        }
        else {
            strcpy(AIRLINE, sp);
        }
        sp = strtok(NULL, ",");
        sp = strtok(NULL, ",");
        if (sp == NULL) {
            ;
        }
        else {
            strcpy(SRC_AIRPORT_NAME, sp);
        }
        sp = strtok(NULL, ",");

        if (sp == NULL) {
            ;
        }
        else {
            strcpy(SRC_CITY, sp);
        }
        sp = strtok(NULL, ",");

        if (sp == NULL) {
            ;
        }
        else {
            strcpy(SRC_COUNTRY, sp);
        }
        sp = strtok(NULL, ",");

        if (sp == NULL) {
            ;
        }
        else {
            strcpy(SRC_AIRPORT_CODE, sp);
        }
        sp = strtok(NULL, ",");
        sp = strtok(NULL, ",");
        if (sp == NULL) {
            ;
        }
        else {
            strcpy(DEST_AIRPORT_NAME, sp);
            sp = strtok(NULL, ",");

            if (sp == NULL) {
                ;
            }
            else {
                strcpy(DEST_CITY, sp);
            }
            sp = strtok(NULL, ",");
            if (sp == NULL) {
                ;
            }
            else {
                strcpy(DEST_COUNTRY, sp);
            }
            sp = strtok(NULL, ",");
            if (sp == NULL) {
                ;
            }
            else {
                strcpy(DEST_AIRPORT_CODE, sp);
            }

            char temp_airline[200];
            char temp_src_city[200];
            char temp_src_country[200];
            char temp_dest_city[200];
            char temp_dest_country[200];

            sprintf(temp_airline, "%s", sort_filter_array[0][0]);
            sprintf(temp_src_city, "%s", sort_filter_array[1][0]);
            sprintf(temp_src_country, "%s", sort_filter_array[2][0]);
            sprintf(temp_dest_city, "%s", sort_filter_array[3][0]);
            sprintf(temp_dest_country, "%s", sort_filter_array[4][0]);

            if (sort_filter_array[1][0] != NULL && (strcmp(temp_airline, AIRLINE) == 0) && sort_filter_array[4][0] != NULL && (strcmp(temp_dest_country, DEST_COUNTRY) == 0)) {
                printf("break3\n");
                if (i == 0) {
                    fprintf(output_file, "FLIGHTS TO %s BY %s (%s):\n", DEST_COUNTRY, AIRLINE_NAME, AIRLINE);
                }
                fprintf(output_file, "FROM: %s, %s, %s TO: %s (%s), %s\n", SRC_AIRPORT_CODE, SRC_CITY, SRC_COUNTRY, DEST_AIRPORT_NAME, DEST_AIRPORT_CODE, DEST_CITY);
                i++;
            }

            if ((strcmp(temp_src_country, SRC_COUNTRY) == 0) && (strcmp(temp_dest_city, DEST_CITY) == 0) && (strcmp(temp_dest_country, DEST_COUNTRY) == 0) && num_arg == 5) {
                printf("break4\n");
                if (i == 0) {
                    fprintf(output_file, "FLIGHTS FROM %s TO %s, %s:\n", SRC_COUNTRY, DEST_CITY, DEST_COUNTRY);
                }
                fprintf(output_file, "AIRLINE: %s (%s) ORIGIN: %s (%s), %s\n", AIRLINE_NAME, AIRLINE, SRC_AIRPORT_NAME, SRC_AIRPORT_CODE, SRC_CITY);
                i++;
            }

            if ((strcmp(temp_src_city, SRC_CITY) == 0) && (strcmp(temp_src_country, SRC_COUNTRY) == 0) && (strcmp(temp_dest_city, DEST_CITY) == 0) && (strcmp(temp_dest_country, DEST_COUNTRY) == 0 && num_arg == 6)) {
                printf("break4\n");
                if (i == 0) {
                    fprintf(output_file, "FLIGHTS FROM %s, %s TO %s, %s:\n", SRC_CITY, SRC_COUNTRY, DEST_CITY, DEST_COUNTRY);
                }
                fprintf(output_file,"AIRLINE: %s (%s) ROUTE: %s-%s\n", AIRLINE_NAME, AIRLINE, SRC_AIRPORT_CODE, DEST_AIRPORT_CODE);
                i++;
            }


        }
    }
    if (i == 0) {
        fprintf(output_file, "NO RESULTS FOUND.\n");
    }
    fclose(output_file);
}


/**
 * Function: main
 * --------------
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
#pragma warning(disable : 4996)

int main(int argc, char *argv[])
{
    int num_arg = argc;

    Strings field_array[num_arg];
    Strings filter_array[num_arg];

    Strings sort_field_array[6];
    Strings sort_filter_array[6];

    obtain_arguments(num_arg, argv, field_array, filter_array,sort_filter_array);

    int i;

    char* csv_fp = field_array[0][0];
    char* output_file_name = "output.txt";

    process_lines(csv_fp, sort_filter_array, num_arg);


    exit(0);
}


