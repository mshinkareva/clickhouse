from clickhouse_driver import Client

client = Client(host='localhost')


def get_clusters():
    full_clusters_query = 'SELECT * FROM system.clusters;'
    full_clusters = client.execute(full_clusters_query)
    print(full_clusters)


def create_database():
    create_database_query = "CREATE DATABASE IF NOT EXISTS example ON CLUSTER company_cluster"
    client.execute(create_database_query)


if __name__ == '__main__':
    get_clusters()
    create_database()
