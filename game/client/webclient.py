from game.persistency import remote_save_url

class WebClient:
    base_url: str = remote_save_url()

    @property
    def post_miz():
        raise NotImplementedError
