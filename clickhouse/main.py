from clickhouse_driver import Client

if __name__ == '__main__':
    client = Client(host='localhost')
    clusters = client.execute('SELECT cluster FROM system.clusters;')
    print(clusters)