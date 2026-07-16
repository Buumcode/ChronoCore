class WorkflowTimeline:
    """
    Преобразует историю snapshot
    в последовательность событий.
    """


    def __init__(
        self,
        history,
    ):

        self.history = history



    def build(self):

        snapshots = self.history.all()

        if not snapshots:
            return []


        events = []


        events.append(
            {
                "type": "created",
                "message": "Initial workflow",
                "snapshot": snapshots[0].id,
            }
        )


        for index in range(
            1,
            len(snapshots)
        ):

            previous = snapshots[index - 1]

            current = snapshots[index]


            diff = previous.compare(
                current
            )


            if diff:
                print("TIMELINE DIFF:", diff)
                events.append(
                    {
                        "type": "changed",
                        "snapshot": current.id,
                        "changes": self._normalize_diff(diff),
                    }
                )


        return events
        
    def _normalize_diff(
        self,
        diff,
    ):

        if "changed" in diff:
            return diff["changed"]


        return diff

    def events(self):

        return [
            event.to_dict()
            for event in self.history.events()
        ]       
        
    def stream(self):

        stream = []


        for event in self.history.events():

            stream.append(
                event.to_dict()
            )


        return sorted(
            stream,
            key=lambda item:
                item["created"]
        )        
        
    def filter(
        self,
        type=None,
        after=None,
        before=None
    ):

        items = self.stream()


        result = []


        for item in items:

            if type is not None:

                if item.get("type") != type:
                    continue


            created = item.get(
                "created"
            )


            if after is not None:

                if created <= after:
                    continue


            if before is not None:

                if created >= before:
                    continue


            result.append(
                item
            )


        return result        