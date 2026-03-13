from typing import Any, List, Union, Protocol
from abc import ABC, abstractmethod
import collections

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...

class InputStage:
    def __init__(self) -> None:
        self.stage_info = "Input stage ready"

    def process(self, data: Any) -> Any:
        data_return: Any = data
        return data_return

class TransformStage:
    def __init__(self) -> None:
        self.stage_info = "Transform stage ready"

    def process(self, data: Any) -> Any:
        try:
            if type(data) is list:
                data_return = [str(dat) + " (Transformed)" for dat in data]
                return data_return
            if type(data) is dict:
                return str(data) + " Enriched with metadata"
            data_return = str(data) + " (Transformed)"
            return data_return
        except BaseException:
            return None

class OutputStage:
    def __init__(self) -> None:
        self.stage_info = "Output stage ready"

    def process(self, data: Any) -> Any:
        data_return: str = "Final Output: " + str(data)
        return data_return

class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        current_data: Any = data
        i: int = 0
        try:
            while i < len(self.stages):
                current_data = self.stages[i].process(current_data)
                i += 1
            data_return: str = "JSON Pipeline " + str(self.pipeline_id) + " processed: " + str(current_data)
            return data_return
        except BaseException:
            return "Error in JSON pipeline"

class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        current_data: Any = data
        i: int = 0
        try:
            while i < len(self.stages):
                current_data = self.stages[i].process(current_data)
                i += 1
            data_return: str = "CSV Pipeline " + str(self.pipeline_id) + " processed: " + str(current_data)
            return data_return
        except BaseException:
            return "Error in CSV pipeline"

class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        current_data: Any = data
        i: int = 0
        try:
            while i < len(self.stages):
                current_data = self.stages[i].process(current_data)
                i += 1
            data_return: str = "Stream Pipeline " + str(self.pipeline_id) + " processed: " + str(current_data)
            return data_return
        except BaseException:
            return "Error in Stream pipeline"

class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def run_all(self, data_list: List[Any]) -> None:
        print("\nMulti-Format Data Processing")
        i: int = 0
        data_result: str = ""
        while i < len(self.pipelines) and i < len(data_list):
            print(f"Processing data through pipeline {i+1}...")
            data_result = self.pipelines[i].process(data_list[i])
            print("Output: " + str(data_result))
            print()
            i += 1


def nexus_enterprise_data() -> None:
    print("=== CODE NEXUS ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    
    manager = NexusManager()
    
    json_pipe = JSONAdapter("PIPE_JSON_1")
    csv_pipe = CSVAdapter("PIPE_CSV_1")
    stream_pipe = StreamAdapter("PIPE_STREAM_1")
    
    all_pipes: list = [json_pipe, csv_pipe, stream_pipe]
    
    input_s = InputStage()
    transform_s = TransformStage()
    output_s = OutputStage()
    
    i: int = 0
    while i < len(all_pipes):
        all_pipes[i].add_stage(input_s)
        all_pipes[i].add_stage(transform_s)
        all_pipes[i].add_stage(output_s)
        manager.add_pipeline(all_pipes[i])
        i += 1
        
    all_data: list = [
        {"sensor": "temp", "value": 23.5},
        "user, action, timestamp",
        "Real-time sensor stream"
    ]
    
    manager.run_all(all_data)
    print("Nexus Integration complete. All systems operational.")

if __name__ == '__main__':
    nexus_enterprise_data()