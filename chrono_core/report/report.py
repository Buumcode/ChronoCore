class WorkflowReport:

    def __init__(self):

        self.data = {}


    def add(
        self,
        key,
        value
    ):

        self.data[key] = value


    def get(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )


    def __getitem__(
        self,
        key
    ):

        return self.data[key]


    def to_dict(self):

        return self.data


    @classmethod
    def from_dict(
        cls,
        data
    ):

        report = cls()

        report.data = data

        return report