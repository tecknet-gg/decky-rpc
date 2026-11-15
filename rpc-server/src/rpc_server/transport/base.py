class BaseDiscovery:
    def candidate_directories(self):
        raise NotImplementedError()

    def candidate_filenames(self):
        raise NotImplementedError()

