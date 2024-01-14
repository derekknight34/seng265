/** @file route_manager.c
 *  @brief A small program to analyze airline routes data.
 *  @author Mike Z.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Saasha J.
 *  @author Victoria L.
 *  @author Derek Knight
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

// TODO: Make sure to adjust this based on the input files given
#define MAX_LINE_LEN 300

/**
 * @brief Serves as an incremental counter for navigating the list.
 *
 * @param p The pointer of the node to print.
 * @param arg The pointer of the index.
 *
 */
void inccounter(node_t *p, void *arg)
{
    int *ip = (int *)arg;
    (*ip)++;
}

/**
 * @brief Allows to print out the content of a node.
 *
 * @param p The pointer of the node to print.
 * @param arg The format of the string.
 *
 */
void print_node(node_t *p, void *arg)
{
    char *fmt = (char *)arg;
    printf(fmt, p->word);

}

/**
 * @brief Allows to print each node in the list.
 *
 * @param l The first node in the list
 *
 */
void analysis(node_t *l)
{
    int len = 0;

    apply(l, inccounter, &len);
    printf("Number of words: %d\n", len);

    apply(l, print_node, "%s\n");
}


/*
 * @brief Reads a given yaml file and filters the data for airline routes with desitnations in Canada.
 *
 * @param file_name The name of the yaml file for the program to read.
 * @return node_t* A pointer to the first element in the list in alphabetical order of airline
 * routes with destination in Canada.
 */

node_t* q1_create_airline_name_list(char* file_name){

    FILE* yaml_fp;
    yaml_fp = fopen(file_name, "r");

    char *yaml_line = NULL;
    char *field_line = NULL;
    char *formatted_line = NULL;
    char *airline_name = NULL;
    char *airline_code = NULL;
    char *airline_name_code = NULL;
    node_t *airline_name_code_list = NULL;

    yaml_line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    field_line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    formatted_line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    airline_name = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    airline_code = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    airline_name_code = (char *)malloc(sizeof(char) * MAX_LINE_LEN);

    while(!feof(yaml_fp)){
        fgets(yaml_line, MAX_LINE_LEN, yaml_fp);

        if(strcmp(yaml_line, "-") > 0){
            sscanf(yaml_line, "- %[^:]: %[^\n]", field_line, formatted_line);
        } else if (strcmp(yaml_line," ") > 0){
            sscanf(yaml_line, " %[^:]: %[^\n]", field_line, formatted_line);
        }

        if( strcmp(field_line, "airline_name") == 0){
            strcpy(airline_name, formatted_line);
        }
         else if( strcmp(field_line, "airline_icao_unique_code") == 0){

            strcpy(airline_code, formatted_line);
            strcpy(airline_name_code,airline_name);
            strcat(airline_name_code, " (");
            strcat(airline_name_code, airline_code);
            strcat(airline_name_code, ")");

        } else if(strcmp(field_line, "to_airport_country") == 0){
            if (strcmp(formatted_line, "Canada") == 0){
                airline_name_code_list = add_and_inc(airline_name_code_list, new_node(airline_name_code));
            }
        }        
    }
    fclose(yaml_fp);

    free(yaml_line);
    free(field_line);
    free(airline_name);
    free(airline_code);
    free(airline_name_code);
    
    return airline_name_code_list;
}

/*
 * @brief Reads a given yaml file and groups the routes data by destination country.
 *
 * @param file_name The name of the yaml file for the program to read.
 * @return node_t* A pointer to the first element in the list in alphabetical order of routes
 * grouped by destination country.
 */

node_t* q2_create_airline_name_list(char* file_name){

    FILE* yaml_fp;
    yaml_fp = fopen(file_name, "r");

    char *yaml_line = NULL;
    char *field_line = NULL;
    char *formatted_line = NULL;
    char *dest_country = NULL;
    node_t *airline_name_code_list = NULL;

    yaml_line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    field_line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    formatted_line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    dest_country = (char *)malloc(sizeof(char) * MAX_LINE_LEN);

    while(!feof(yaml_fp)){
        fgets(yaml_line, MAX_LINE_LEN, yaml_fp);
        //puts(yaml_line);
        if(strcmp(yaml_line, "-") > 0){
            sscanf(yaml_line, "- %[^:]: %[^\n]", field_line, formatted_line);
        } else if (strcmp(yaml_line," ") > 0){
            sscanf(yaml_line, " %[^:]: %[^\n]", field_line, formatted_line);
        }

        if( strcmp(field_line, "to_airport_country") == 0){

            while(formatted_line[0] == '\'' || formatted_line[0] == ' '){
                formatted_line++;
            }
               
            char* formatted_trailing = formatted_line + strlen(formatted_line) - 1;

            while(formatted_trailing > formatted_line && (formatted_trailing[0] == ' ' || formatted_trailing[0] == '\'')){
                   formatted_trailing--;
            }
            
            formatted_trailing[1] = '\0';
            strcpy(dest_country, formatted_line);
            airline_name_code_list = add_and_inc(airline_name_code_list, new_node(dest_country));
        }
    }
    fclose(yaml_fp);

    free(yaml_line);
    free(field_line);
    free(dest_country);

    return airline_name_code_list;
}

/*
 * @brief Reads a given yaml file and groups the routes data by destination airport.
 *
 * @param file_name The name of the yaml file for the program to read.
 * @return node_t* A pointer to the first element in the list in alphabetical order of routes
 * grouped by destination airport.
 */

node_t* q3_create_airline_name_list(char* file_name){

    FILE* yaml_fp;
    yaml_fp = fopen(file_name, "r");

    char *yaml_line = NULL;
    char *field_line = NULL;
    char *formatted_line = NULL;
    char *to_airport_name = NULL;
    char *to_airport_icao_unique_code = NULL;
    char *to_airport_city = NULL;
    char *to_airport_country = NULL;
    char *to_airport_str = NULL;
    node_t *airline_name_code_list = NULL;

    yaml_line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    field_line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    formatted_line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    to_airport_name = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    to_airport_icao_unique_code = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    to_airport_city = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    to_airport_country = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    to_airport_str = (char *)malloc(sizeof(char) * MAX_LINE_LEN);

    while(!feof(yaml_fp)){
        fgets(yaml_line, MAX_LINE_LEN, yaml_fp);
        //puts(yaml_line);
        if(strcmp(yaml_line, "-") > 0){
            sscanf(yaml_line, "- %[^:]: %[^\n]", field_line, formatted_line);
        } else if (strcmp(yaml_line," ") > 0){
            sscanf(yaml_line, " %[^:]: %[^\n]", field_line, formatted_line);
        }

        if( strcmp(field_line, "to_airport_name") == 0){
            strcpy(to_airport_name, formatted_line);
        }else if(strcmp(field_line, "to_airport_city") == 0){
            strcpy(to_airport_city, formatted_line);
        } else if( strcmp(field_line, "to_airport_country") == 0){
            strcpy(to_airport_country, formatted_line);
        }else if(strcmp(field_line, "to_airport_icao_unique_code") ==0){
                strcpy(to_airport_icao_unique_code, formatted_line);

            strcpy(to_airport_str,"\"");
            strcat(to_airport_str, to_airport_name);
            strcat(to_airport_str, " (");
            strcat(to_airport_str, to_airport_icao_unique_code);
            strcat(to_airport_str, "), ");
            strcat(to_airport_str, to_airport_city);
            strcat(to_airport_str, ", ");
            strcat(to_airport_str, to_airport_country);
            strcat(to_airport_str, "\"");
            
            airline_name_code_list = add_and_inc(airline_name_code_list, new_node(to_airport_str));
        } 
    }
    fclose(yaml_fp);

    free(yaml_line);
    free(field_line);
    free(formatted_line);
    free(to_airport_name);
    free(to_airport_icao_unique_code);
    free(to_airport_city);
    free(to_airport_country);
    free(to_airport_str);

    return airline_name_code_list;
}

/*
 * @brief Takes a list and sorts the list in desending order by counter value if the qustion number is 1 or 3
 * and in asending order if the question number is 2.
 *
 * @param node_t* start_list A pointer to the first element in the list to sort.
 * @param int question The question number to be evaluated.
 * @return node_t* A pointer to the first element in the list sorted by counter value.
 */

node_t* ordered_airline_name_list(node_t* start_list, int question){

    node_t *sort_list = NULL;

    node_t *curr = start_list;
    for (curr = start_list; curr != NULL; curr = curr->next) {


        node_t *sort_node;
        sort_node = new_node(curr->word);
        sort_node->counter = curr->counter;

        if (question == 1){
            sort_list = add_inorder_count(sort_list, sort_node);  
        } else if(question == 2){
            sort_list = add_in_asending_order_count(sort_list, sort_node);
        } else if(question == 3){
            sort_list = add_inorder_count(sort_list, sort_node);
        }
    }
    node_t *temp_n = NULL;
    for (; start_list != NULL; start_list = temp_n)
    {
        temp_n = start_list->next;
        free(start_list->word);
        free(start_list);
    }

    return sort_list;
}

/*
 * @brief Takes a sorted list and created a csv file with two columns based on the list provided.
 * The number of rows is passed as an argument num_lines.
 *
 * @param char* file_name The name of the csv file to be created.
 * @param node_t* start_list A pointer to the first element in the list to be made into a csv file.
 * @param int num_lines The number of rows in the created csv file.
 */

void create_csv(char* file_name, node_t* list, int num_lines){

    FILE* csv_file;
    csv_file = fopen(file_name, "w");

    if (csv_file == NULL){
        printf("No file with that name");
    }

    fprintf(csv_file, "subject,statistic\n");

    int line_count = 0;
    node_t *curr = NULL;
    for (curr = list; curr != NULL && line_count < num_lines; curr = curr->next) {
        fprintf(csv_file, "%s,%d\n",curr->word,curr->counter);
        line_count++;
    }

}

/*
 * @brief Takes the command line arguments and returns the question number.
 *
 * @param char* argv The command line argument input.
 * @return int The question number.
 */

int  get_question(char *argv) {

    char* question = NULL;
    char* arg_field = NULL;

    question = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    arg_field = (char *)malloc(sizeof(char) * MAX_LINE_LEN);

    
    sscanf(argv, "--%[^=]=%[^\n]", arg_field, question);

    int question_int = atoi(question);

    free(question);
    free(arg_field);

    return question_int;
}

/*
 * @brief Takes the command line arguments and returns the number of rows to be output in the csv file.
 *
 * @param char* argv The command line argument input.
 * @return int The number of rows required in the csv file.
 */

int  get_num_lines(char *argv) {

    char* num_lines_count = NULL;
    char* arg_field = NULL;

    num_lines_count = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    arg_field = (char *)malloc(sizeof(char) * MAX_LINE_LEN);

    sscanf(argv, "--%[^=]=%[^\n]", arg_field, num_lines_count);
    
    int num_lines_int = atoi(num_lines_count);

    free(num_lines_count);
    free(arg_field);

    return num_lines_int;
}


/*
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors
 *
 */

int main(int argc, char *argv[])
{
    int question_num;
    question_num = get_question(argv[2]);

    int num_lines_arg;
    num_lines_arg = get_num_lines(argv[3]);
    
    node_t *airline_name_code_list = NULL;
    if(question_num == 1){
        airline_name_code_list = q1_create_airline_name_list("routes-airlines-airports.yaml");
    } else if (question_num == 2){
        airline_name_code_list = q2_create_airline_name_list("routes-airlines-airports.yaml");
    } else if (question_num ==3){
        airline_name_code_list = q3_create_airline_name_list("routes-airlines-airports.yaml");
    }

    node_t *airline_sort_list = NULL;
    airline_sort_list = ordered_airline_name_list(airline_name_code_list, question_num);

    create_csv("output.csv", airline_sort_list, num_lines_arg);

    exit(0);
}
