#!/usr/bin/env python3

import psycopg2

DBName = "news"

def prompt_1():
    """
    1. What are the most popular three articles of all time?
    """
    conn = psycopg2.connect(database=DBName)
    cursor = conn.cursor()
    cursor.execute(
        """
        select title, sum from
        (
            select name, count(*) as sum from (
                select replace(substr(path, 11), '-', ' ') as name from log
                where path != '/' and path != ' '
            ) as fixed_log
            where name != '' and name != ' spam humbug'
            group by name
            order by name desc
        ) as final_log inner join articles
        on title like '%' || name || '%'
        order by sum desc;
        """)
    list_path = cursor.fetchall()

    # Traverse through results from query and print out article and views.
    print("Q1: What are the most popular three articles of all time?\n")
    print("Answer:")
    for i in range(3):
        title = list_path[i][0]
        views = str(list_path[i][1])
        print("\t" + str(i+1) + ". " + title + " -- " + views)
    conn.close()
    print('\n')
    return


def prompt_2():
    """
    2. Who are the most popular article authors of all time?
    """
    conn = psycopg2.connect(database=DBName)
    cursor = conn.cursor()
    cursor.execute(
        """
        select name, count(*) as sum
            from (
                    select title, joined_id.name, author from (
                        select name, title, articles.author
                        from articles inner join authors
                        on articles.author = authors.id
                    ) as joined_id inner join
                    (
                        select name from
                        (
                            select replace(replace(replace
                                (substr(path,11), '-', ' '),
                                'o many bears', 'here are a'),
                                'googles', 'Google') as name
                            from log
                        ) as replaced
                        where name != '' and name != ' spam humbug'
                    )
                    as fixed on title like '%' || fixed.name || '%'
                )
        as final group by name order by sum desc;
        """)
    list_authors = cursor.fetchall()
    print("Q2: Who are the most popular article authors of all time?\n")
    print("Answer:")
    for i in range(len(list_authors)):
        authors = list_authors[i][0]
        views = str(list_authors[i][1])
        print("\t" + str(i+1) + ". " + authors + " -- " + views)
    conn.close()
    print('\n')
    return


def prompt_3():
    """
    3. On which days did more than 1% of requests lead to errors?
    """
    conn = psycopg2.connect(database=DBName)
    cursor = conn.cursor()
    cursor.execute(
        """
        select time, err_percent from (
            select total.time,
            err_req/cast(tot_req as float) * 100.0 as err_percent
            from (
                select time, count(*) as tot_req from (
                    select to_char(time, 'MM/DD/YYYY') as time, status from log
                    ) as fixed
                group by time
                ) as total inner join
                (
                select time, count(*) as err_req from (
                    select to_char(time, 'MM/DD/YYYY') as time, status from log
                    ) as fixed
                where status != '200 OK' group by time
                ) as errors
            on total.time = errors.time
            order by err_percent desc) as percent_table
        where err_percent > 1.0;
        """)
    list_err_dates = cursor.fetchall()
    print("Q3: On which days did more than 1% of requests lead to errors?\n")
    print("Answer:")
    for i in range(len(list_err_dates)):
        month, day, year = list_err_dates[i][0].split('/')
        err_percent = list_err_dates[i][1]
        print(
            "\t" + "July, " + str(day) + ", " + str(year) + " - " +
            str(err_percent) + "% errors")
    conn.close()
    print('\n')
    return


prompt_1()
prompt_2()
prompt_3()
