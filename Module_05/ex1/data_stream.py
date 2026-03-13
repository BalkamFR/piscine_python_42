from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count: int = 0
        self.stream_type: str = "Unknown"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        filtered_list: List[Any] = [dat for dat in data_batch if dat is not None]
        return filtered_list

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats_dict: Dict[str, Union[str, int, float]] = {
            "stream_id": self.stream_id,
            "processed": self.processed_count
        }
        return stats_dict


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        data_list: List[Any] = []
        try:
            data_list = [dat for dat in data_batch if isinstance(dat, (int, float))]
            self.processed_count = self.processed_count + len(data_list)
            
            sum_val: float = sum(data_list)
            avg: float = 0.0
            if len(data_list) > 0:
                avg = sum_val / len(data_list)
                
            data_return: str = "Sensor analysis: " + str(len(data_list)) + " readings processed, avg temp: " + str(avg) + "°C"
            return data_return
        except BaseException:
            return "Error processing sensor data"

    def execut_all(self, data: List[Any]) -> None:
        print("Initializing Sensor Stream...")
        print("Stream ID: " + str(self.stream_id) + ", Type: " + str(self.stream_type))
        print(f"Processing sensor batch: {data}")
        result = self.process_batch(data)
        print(result)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        data_list: List[Any] = []
        try:
            data_list = [dat for dat in data_batch if isinstance(dat, (int, float))]
            self.processed_count = self.processed_count + len(data_list)
            
            net_flow: float = sum(data_list)
            data_return: str = "Transaction analysis: " + str(len(data_list)) + " operations, net flow: +" + str(net_flow) + " units"
            return data_return
        except BaseException:
            return "Error processing transaction data"

    def execut_all(self, data: List[Any]) -> None:
        print("Initializing Transaction Stream...")
        print("Stream ID: " + str(self.stream_id) + ", Type: " + str(self.stream_type))
        print(f"Processing transaction batch: {data}")
        result = self.process_batch(data)
        print(result)


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        data_list: List[Any] = []
        error_list: List[Any] = []
        try:
            data_list = [dat for dat in data_batch if isinstance(dat, str)]
            self.processed_count = self.processed_count + len(data_list)
            
            error_list = [e for e in data_list if e == "error"]
            data_return: str = "Event analysis: " + str(len(data_list)) + " events, " + str(len(error_list)) + " error detected"
            return data_return
        except BaseException:
            return "Error processing event data"

    def execut_all(self, data: List[Any]) -> None:
        print("Initializing Event Stream...")
        print("Stream ID: " + str(self.stream_id) + ", Type: " + str(self.stream_type))
        print(f"Processing event batch: {data}")
        result = self.process_batch(data)
        print(result)


class StreamProcessor:
    def __init__(self) -> None:
        self.status = "Ready"

    def process_streams(self, streams: List[DataStream], batches: List[List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        
        i: int = 0
        data_result: str = ""
        while i < len(streams):
            data_result = streams[i].process_batch(batches[i])
            print("Batch " + str(i + 1) + " Results:\n" + data_result)
            i += 1
        print("\nAll streams processed successfully. Nexus throughput optimal.")


def nexus_stream_data() -> None:
    print("=== CODE NEXUS POLYMORPHIC STREAM SYSTEM ===\n")
    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")
    
    all_class: list = [sensor, transaction, event]
    all_data: list = [
        [22.5, 65, 1013],
        [100, -150, 75], 
        ["login", "error", "logout"]
    ]
    
    i: int = 0
    while i < len(all_class):
        all_class[i].execut_all(all_data[i])
        print()
        i += 1
        
    processor = StreamProcessor()
    processor.process_streams(all_class, all_data)

if __name__ == '__main__':
    nexus_stream_data()