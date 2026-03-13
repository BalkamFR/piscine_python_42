from abc import ABC, abstractmethod
from typing import Any, List, Optional


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> Optional[str]:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return "Output: " + result


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.data_list = None

    def process(self, data: Any) -> Optional[str]:
        data_list: List[Any] = []
        for dat in data:
            try:
                if type(dat) is not int:
                    return None
                int(dat)
                data_list.append(dat)
            except BaseException:
                return None
        data_return: str = "Processed " + str(
            len(data_list)) + " numeric values, sum=" + str(
            sum(data_list)) + ", avg=" + str(sum(data_list) / len(data_list))
        return data_return

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        return True

    def execut_all(self, data: Any) -> None:
        print("Initializing Numeric Processor...")
        print(f"Processing data: {data}")
        self.data_list = self.process(data)
        if self.validate(self.data_list) is False:
            print("Validation: numeric entry verified")
            print("Output: [ALERT] ERROR int detected: Conversion")
        else:
            print("Validation: Numeric data verified")
            print((self.data_list))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        self.data_verif = None

    def process(self, data: Any) -> Optional[str]:
        try:
            for dat in data:
                if type(dat) is not str:
                    return ""
        except BaseException:
            return None
        tmp = data.split()
        output: str = "Processed text: " + \
            str(len(data)) + " characters, " + str(len(tmp)) + " words"
        return output

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        return True

    def execut_all(self, data: Any) -> None:
        print("Initializing Text Processor...")
        self.data_list = self.process(data)
        print(f"Processing data: \"{data}\"")
        if self.validate(self.data_list) is False:
            print("Validation: numeric entry verified")
            print("Output: [ALERT] ERROR level detected: Conversion")
        else:
            print("Validation: Numeric data verified")
            print(self.format_output(self.data_list))


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        self.data_verif = None

    def process(self, data: Any) -> Optional[str]:
        data_list = data.split(" ")
        data_return: Optional[str] = None
        for dat in data_list:
            if data_return is not None:
                data_return = data_return + " " + dat
            if dat == "ERROR:":
                data_return = "[ALERT] ERROR level detected:"
            if dat == "INFO:":
                data_return = "[INFO] INFO level detected:"
        return data_return

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        return True

    def execut_all(self, data: Any):
        print("Initializing Log Processor...")
        self.data_list = self.process(data)
        print(f"Processing data: \"{data}\"")
        if self.validate(self.data_list is not None):
            print("Validation: Log entry verified")
            print(self.format_output(self.data_list))
        else:
            print("Error is not log")


def nexus_data() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    log = LogProcessor()
    text = TextProcessor()
    numerique = NumericProcessor()
    all_class: List[Any] = [numerique, text, log]
    all_data: List[Any] = [[1, 2, 3, 4, 5],
                           "Hello Nexus World", "ERROR: Connection timeout"]
    i: int = 0
    while i < len(all_class):
        all_class[i].execut_all(all_data[i])
        print()
        i += 1


def polymorphic_data():
    print("=== Polymorphic Processing Demo ===\n")
    log = LogProcessor()
    text = TextProcessor()
    numerique = NumericProcessor()
    all_class: List[Any] = [numerique, text, log]
    all_data: List[Any] = [[1, 2, 3, 4, 5],
                           "Hello Nexus World", "ERROR: Connection timeout"]
    i: int = 0
    data_class: Optional[str] = ""
    print("Processing multiple data types through same interface...")
    while i < len(all_class):

        data_class = all_class[i].process(all_data[i])
        print(f"Result {i + 1}: {data_class}")
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == '__main__':
    nexus_data()
    polymorphic_data()
