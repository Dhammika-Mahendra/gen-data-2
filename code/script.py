import argparse
import json
from collections import Counter
from pathlib import Path


TARGET_KEYS = ["label_disclosure", "label_risk", "label_subcategory"]
DEFAULT_JSON_PATH = Path(r"C:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\code\sample_dataset.json")

 
def load_json_array(path: Path):
	with path.open("r", encoding="utf-8") as handle:
		data = json.load(handle)
	if not isinstance(data, list):
		raise ValueError("JSON root must be an array of objects")
	return data


def count_values(items, keys):
	counters = {key: Counter() for key in keys}
	for item in items:
		if not isinstance(item, dict):
			continue
		for key in keys:
			if key in item:
				counters[key][item[key]] += 1
	return counters


def print_counts(counters):
	for key, counter in counters.items():
		print(f"\n{key} ({len(counter)} distinct values)")
		for value, count in counter.most_common():
			print(f"  {value}: {count}")


def main():
	parser = argparse.ArgumentParser(
		description="Count distinct values and frequencies for label properties."
	)
	parser.add_argument(
		"json_path",
		nargs="?",
		default=None,
		help="Path to a JSON file with an array of objects.",
	)
	args = parser.parse_args()

	path = Path(args.json_path) if args.json_path else DEFAULT_JSON_PATH
	items = load_json_array(path)
	counters = count_values(items, TARGET_KEYS)
	print_counts(counters)


if __name__ == "__main__":
	main()
