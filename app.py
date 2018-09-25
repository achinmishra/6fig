from connexion.resolver import RestyResolver
import connexion

if __name__ == '__main__':
    myApp = connexion.App(__name__, specification_dir='swagger/')
    myApp.add_api('my_service.yaml', resolver=RestyResolver('api'))
    myApp.run(port=9091)