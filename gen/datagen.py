import json
import re


INPUT_PATH = r"c:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\gen\rawdata.txt"
OUTPUT_PATH = r"c:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\gen\data.json"


LABEL_RE = re.compile(r"^\s*\[(.+?)\]\s*$")


def parse_labeled_sentences(text: str) -> list[dict[str, str]]:
	items: list[dict[str, str]] = []
	current_label: str | None = None

	for raw_line in text.splitlines():
		line = raw_line.strip()
		if not line:
			continue

		label_match = LABEL_RE.match(line)
		if label_match:
			current_label = label_match.group(1).strip()
			continue

		if current_label is None:
			continue

		items.append({"text": line, "category": current_label})

	return items


def main() -> None:
	with open(INPUT_PATH, "r", encoding="utf-8") as handle:
		content = handle.read()

	data = parse_labeled_sentences(content)

	with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
		json.dump(data, handle, ensure_ascii=False, indent=2)


if __name__ == "__main__":
	main()
