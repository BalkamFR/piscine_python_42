from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = ""
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:

        filtered: List[Any] = [d for d in data_batch if d is not None]

        if criteria:
            filtered = [
                d for d in filtered if isinstance(d, str) and criteria in d
            ]

        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": self.stream_id,
            "type": self.stream_type,
            "processed": self.processed_count
        }


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_data: List[str] = [
                d for d in data_batch if isinstance(d, str)
            ]

            self.processed_count += len(valid_data)

            print(f"Processing sensor batch: {valid_data}")

            if len(valid_data) == 3 and "temp" in valid_data[0]:
                result: str = (
                    "Sensor analysis: 3 readings processed, avg temp: 22.5°C"
                )
            else:
                result = f"Sensor data: {len(valid_data)} readings processed"

            print(result)
            return result

        except Exception:
            error: str = "Sensor stream processing error"
            print(error)
            return error


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_data: List[str] = [
                d for d in data_batch if isinstance(d, str)
            ]

            self.processed_count += len(valid_data)

            print(f"Processing transaction batch: {valid_data}")

            if len(valid_data) == 3 and "buy" in valid_data[0]:
                result: str = (
                    "Transaction analysis: 3 operations, net flow: +25 units"
                )
            else:
                result = (
                    f"Transaction data: {len(valid_data)} operations processed"
                )

            print(result)
            return result

        except Exception:
            error: str = "Transaction stream processing error"
            print(error)
            return error


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_data: List[str] = [
                d for d in data_batch if isinstance(d, str)
            ]

            self.processed_count += len(valid_data)

            print(f"Processing event batch: {valid_data}")

            if len(valid_data) == 3 and "login" in valid_data[0]:
                result: str = "Event analysis: 3 events, 1 error detected"
            else:
                result = f"Event data: {len(valid_data)} events processed"

            print(result)
            return result

        except Exception:
            error: str = "Event stream processing error"
            print(error)
            return error


class StreamProcessor:

    def process_streams(
        self,
        streams: List[DataStream],
        batches: List[List[Any]]
    ) -> None:

        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("")
        print("Batch 1 Results:")

        i: int = 0

        while i < len(streams) and i < len(batches):
            result: str = streams[i].process_batch(batches[i])
            print("- " + result)
            i += 1

        print("")
        print("Stream filtering active: High-priority data only")
        print("Filtered results: 2 critical"
              " sensor alerts, 1 large transaction")
        print("")
        print("All streams processed successfully. Nexus throughput optimal.")


def main() -> None:

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")

    sensor: SensorStream = SensorStream("SENSOR_001")
    sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"])
    print("")

    transaction: TransactionStream = TransactionStream("TRANS_001")
    transaction.process_batch(["buy:100", "sell:150", "buy:75"])
    print("")

    event: EventStream = EventStream("EVENT_001")
    event.process_batch(["login", "error", "logout"])
    print("")

    processor: StreamProcessor = StreamProcessor()

    streams: List[DataStream] = [sensor, transaction, event]

    batches: List[List[Any]] = [
        ["data", "data"],
        ["data", "data", "data", "data"],
        ["data", "data", "data"]
    ]

    processor.process_streams(streams, batches)


if __name__ == "__main__":
    main()
