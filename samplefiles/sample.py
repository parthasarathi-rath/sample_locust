from locust import HttpUser, constant, task
import urllib3

urllib3.disable_warnings()


class User(HttpUser):

    host = "https://reqres.in/api/"
    wait_time = constant(10)

    @task
    def task1(self):
        self.client.get(url="users?page=2", verify=False)

    @task
    def task2(self):
        self.client.post(url="users", verify=False)
