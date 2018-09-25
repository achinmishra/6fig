from fake_useragent import UserAgent


class FakeUserAgentGeneration:
    def __init__(self):
        self.previous_agents = []
        self.current_random_agent = None
        self.user_agents = UserAgent()

    def load_fake_user_agent(self):
        self.current_random_agent = self.user_agents.chrome

        while self. current_random_agent in self.previous_agents:
            self.current_random_agent = self.user_agents.random

        return self.current_random_agent


