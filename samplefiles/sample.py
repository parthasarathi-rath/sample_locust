from locust import HttpUser, constant, task
import urllib3

urllib3.disable_warnings()


class User(HttpUser):

    host = "https://reqres.in/api/"
    wait_time = constant(10)

    @task
    def task1(self):
        with self.client.get(url="users?page=2", verify=False, catch_response=True) as resp:
            print(resp.status_code)

    @task
    def task2(self):
        with self.client.post(url="users", verify=False, catch_response=True) as resp:
            print(resp.status_code)
