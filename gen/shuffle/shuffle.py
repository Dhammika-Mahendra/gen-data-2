from __future__ import annotations

from pathlib import Path


# Hardcoded directory containing the source .txt files.
SOURCE_DIR = Path(
	r"C:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\docs\categories\3_low"
)
TARGET_FILE_NAME = "Z.txt"
OUTPUT_FILE = Path(__file__).resolve().parent / "shuffled.txt"


def read_sentences(txt_path: Path) -> list[str]:
	lines = [line.strip() for line in txt_path.read_text(encoding="utf-8").splitlines()]
	return [line for line in lines if line]


def interleave_round_robin(groups: list[list[str]]) -> list[str]:
	# Round-robin merge: A1, B1, C1, A2, B2, C2, ...
	merged: list[str] = []
	max_len = max((len(group) for group in groups), default=0)
	for index in range(max_len):
		for group in groups:
			if index < len(group):
				merged.append(group[index])
	return merged


def main() -> None:
	if not SOURCE_DIR.exists():
		raise FileNotFoundError(f"Source directory not found: {SOURCE_DIR}")

	txt_files = sorted(
		path
		for path in SOURCE_DIR.rglob("*.txt")
		if path.is_file() and path.name == TARGET_FILE_NAME
	)
	if not txt_files:
		raise FileNotFoundError(f"No .txt files found in: {SOURCE_DIR}")

	sentence_groups = [read_sentences(path) for path in txt_files]
	merged_sentences = interleave_round_robin(sentence_groups)

	OUTPUT_FILE.write_text("\n".join(merged_sentences) + "\n", encoding="utf-8")


if __name__ == "__main__":
	main()
