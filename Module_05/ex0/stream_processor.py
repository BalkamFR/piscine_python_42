from abc import ABC, abstractmethod

class DataProcessor:
	@abstractmethod
	def process(self,data: Any) -> str:
		pass
	@abstractmethod
	def validate(self, data : Any) -> bool:
		pass

	def format_output(self, result:str) -> str:
		return(f"Output: {result}")

class NumericProcessor(DataProcessor):
	def __init__(self, data:int):
		print("Initializing Numeric Processor...")
		self.data_list = process(data)
		print(f"Processing data: {self.data_list}")

	def process(self, data:any) -> list:
		data_list:list = []
		for i in data:
			try:
				data_list.append(int(i))
			except Exception as a:
				print(f"Error: {a}")
		return (data_list)

	def validate(self, data:any) -> bool:
		for i in data:
			try:
				int(i)
			except:
				print("Error converstion")
				return False
		return True


def main()->None:
	pass

if __name__ == '__main__':
	print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
	main()
	print("\n=== Polymorphic Processing Demo ===")