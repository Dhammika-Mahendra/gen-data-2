from __future__ import annotations

from collections import Counter
from pathlib import Path


TXT_FILE_PATH = Path(
	r"C:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\docs\categories\2_mid\SIN\E.txt"
)


def read_sentences(path: Path) -> list[str]:
	if not path.exists():
		raise FileNotFoundError(f"File not found: {path}")

	with path.open("r", encoding="utf-8") as handle:
		lines = [line.strip() for line in handle]

	# Keep non-empty lines only.
	return [line for line in lines if line]


def find_duplicates(sentences: list[str]) -> Counter[str]:
	counts = Counter(sentences)
	return Counter({sentence: count for sentence, count in counts.items() if count > 1})


def main() -> None:
	sentences = read_sentences(TXT_FILE_PATH)
	duplicates = find_duplicates(sentences)

	if not duplicates:
		print("No duplicate sentences found.")
		return

	print(f"Found {len(duplicates)} duplicate sentences:\n")
	for sentence, count in duplicates.most_common():
		print(f"{count}x | {sentence}")


if __name__ == "__main__":
	main()
