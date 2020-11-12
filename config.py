URL = 'https://www.worldometers.info/coronavirus/'

FIELDS = (
    'country', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_recovered', 'new_recovered',
    'active_cases', 'serious_critical', 'tot_cases_per_1m_pop', 'Deaths_per_1m_pop', 'total_tests', 'Tests_per_1m_pop',
    'population', 'continent', 'one_case_every_x_ppl', 'one_death_every_x_ppl', 'one_test_every_x_ppl',
)

DAYS = ['today', 'yesterday', 'yesterday2', ]

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'myroot'
MYSQL_DB = 'covid'
MYSQL_HOST = '127.0.0.1'